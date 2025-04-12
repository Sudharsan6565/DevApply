package parser


import (
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
)

type Prospect struct {
	Name         string `json:"name"`
	Role         string `json:"role"`
	Email        string `json:"email"`
	Company      string `json:"company"`
	Posted       string `json:"posted"`
	Remote       string `json:"remote"`
	CompanyEmail string `json:"company_email"`
	LinkedIn     string `json:"linkedin"`
	Twitter      string `json:"twitter"`
}

func ParseLinkedIn() ([]Prospect, error) {
	cmd := exec.Command("python3", "scraper/scraper.py")
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	err := cmd.Run()
	if err != nil {
		return nil, fmt.Errorf("❌ Python script failed: %v", err)
	}

	file, err := os.ReadFile("linkedin_results.json")
	if err != nil {
		return nil, fmt.Errorf("❌ Could not read output file: %v", err)
	}

	var results []Prospect
	if err := json.Unmarshal(file, &results); err != nil {
		return nil, fmt.Errorf("❌ Failed to parse JSON: %v", err)
	}

	return results, nil
}

