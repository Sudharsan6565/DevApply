package main

import (
	"context"
	"encoding/csv"
	"fmt"
	"os"
 
	"google.golang.org/api/option"
	"google.golang.org/api/sheets/v4"
	"golang.org/x/oauth2/google"
    "devapply/parser"




)

type App struct {
	ctx context.Context
}

func NewApp() *App {
	return &App{}
}

func (a *App) startup(ctx context.Context) {
	a.ctx = ctx
}

type Result struct {
	Name    string `json:"Name"`
	Role    string `json:"Role"`
	Company string `json:"Company"`
	Email   string `json:"Email"`
}

func (a *App) StartScan(jobSource string, useHunter bool, useApollo bool) []parser.Prospect {

	if jobSource == "LinkedIn" {
		results, err := parser.ParseLinkedIn()
		if err != nil {
			fmt.Println("❌ LinkedIn Parse Error:", err)
			return nil
		}
		return results
	}
	// fallback or YC/HN logic here
	return nil
}


func (a *App) ExportToCSV(results []Result) error {
	file, err := os.Create("devapply_results.csv")
	if err != nil {
		return err
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	headers := []string{"Name", "Role", "Company", "Email"}
	writer.Write(headers)

	for _, r := range results {
		row := []string{r.Name, r.Role, r.Company, r.Email}
		writer.Write(row)
	}

	return nil
}

func (a *App) ExportToSheets(results []Result) error {
	b, err := os.ReadFile("devapply-creds.json")
	if err != nil {
		return fmt.Errorf("failed to read credentials: %v", err)
	}

	config, err := google.JWTConfigFromJSON(b, sheets.SpreadsheetsScope)
	if err != nil {
		return fmt.Errorf("failed to parse JWT config: %v", err)
	}

	client := config.Client(context.Background())
	srv, err := sheets.NewService(context.Background(), option.WithHTTPClient(client))
	if err != nil {
		return fmt.Errorf("unable to retrieve Sheets client: %v", err)
	}

	sheetID := "1lnVfwP8adyMxlCjP9XOHPnd-j9Qk_54hzbNO2wAgTZ8"
	writeRange := "Sheet1!A2"

	var values [][]interface{}
	for _, r := range results {
		values = append(values, []interface{}{r.Name, r.Role, r.Company, r.Email})
	}

	rb := &sheets.ValueRange{Values: values}

	_, err = srv.Spreadsheets.Values.Append(sheetID, writeRange, rb).ValueInputOption("USER_ENTERED").Do()
	if err != nil {
		return fmt.Errorf("failed to write data to sheet: %v", err)
	}

	return nil
}

