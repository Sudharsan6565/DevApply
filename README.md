# 🧠 DevApply — Personal AI-Powered Job Application Assistant

**DevApply** is a cross-platform, native desktop app that automates your job hunt — from scraping hiring leads to exporting contact sheets and generating AI-enhanced cover letters.

> Built solo using Go, Wails, and Svelte — this is a **hands-on FinTech + DevTool experiment** aimed at automating the most annoying parts of tech job searching.

---

## ⚡ Highlights

- 🌐 Scrapes roles from **Y Combinator**, **Hunter.io**, and **Apollo**
- 📤 **Exports results to CSV + Google Sheets**
- ✍️ (WIP) AI-generated cover letters via OpenAI
- 🧾 Built-in config for choosing sources + toggling tools
- 🧱 Fully native desktop app — no Electron, no fluff
- 🌙 **Dark mode UI** with clean grid output
- 💾 Local-first logic — no server required

---

## 📸 Screenshots

| Config Panel | Exported Sheet | Results Table |
|--------------|----------------|----------------|
| ![Config](./screenshots/config.png) | ![Sheet](./screenshots/sheet.png) | ![Results](./screenshots/results.png) |

---

## 🛠️ Tech Stack

| Layer      | Tools Used             |
|------------|------------------------|
| **Frontend**  | Svelte, Tailwind      |
| **Backend**   | Go (Wails v2)         |
| **Exporting** | CSV, Google Sheets API |
| **AI (coming)** | OpenAI GPT-4        |

---

## 📦 Project Structure

```bash
DevApply/
├── main.go             # Wails entry point
├── app.go              # Core logic (Go bindings)
├── frontend/           # Svelte frontend (compiled to dist)
├── scraper/            # Contact + job source scraper logic
├── devapply_results.csv  # Exported data
├── screenshots/        # UI Preview


# Clone this beast
git clone https://github.com/Sudharsan6565/DevApply.git
cd DevApply

# Install Wails CLI if not installed
go install github.com/wailsapp/wails/v2/cmd/wails@latest

# Launch the desktop app (dev mode)
wails dev



🧩 Features Roadmap

Export scraped results to CSV

Push results to Google Sheets

Resume/CV parser (auto-match skill tags)

Cover letter generator via OpenAI

Bulk Apply to selected companies

Add filtering for location, tags, funding round

🧠 Why I Built This

Applying for cloud/dev jobs is brutal — tons of tabs, copy-pasting roles, writing cover letters that never get read.

DevApply was born from that pain.

It’s my personal project to:

    Automate repetition

    Try out Wails (Go-native desktop apps)

    Prototype smart tooling that saves real time

👤 Built By

Sudharsan V (aka Ghostanon17)
👨‍💻 Cloud Engineer • Serverless Architect • Infra Builder
🔗 LinkedIn | 🐙 GitHub
📧 sudharsan6565@gmail.com

