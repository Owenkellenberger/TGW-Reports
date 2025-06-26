# Sellozo ProductVu csv to Google Sheets Report Uploader

This Python script reads data from Sellozo's ProductVu CSV, categorizes, formats into reports based on tags and uploads it to **two Google Sheets documents**, using `gspread` and Google Service Account credentials. It supports environment-based configuration using a `.env` file.

---

## 🔧 Requirements

- Python 3.7+
- Packages:
  - `pandas`
  - `gspread`
  - `google-auth`
  - `python-dotenv`

Install dependencies:
```bash
pip install pandas gspread google-auth python-dotenv
```

---

## 🔐 Setup Instructions

### 1. Place Your Service Account Credentials

Download your `service_account.json` file from Google Cloud Console and place it in the project directory.

### 2. Create a `.env` File

Copy `.env.example` and fill in the correct values:

```bash
cp .env.example .env
```

Then edit `.env`:
```
SERVICE_ACCOUNT_FILE=service_account.json
SHEET_NAME_1=TGW1 Report (2025)
SHEET_NAME_2=TGW2 Report (2025)
```

### 3. Run the Script

```bash
python TGWR3.py
```

---

## 📄 Environment Variables

| Variable              | Description                            |
|-----------------------|----------------------------------------|
| `SERVICE_ACCOUNT_FILE`| Path to your Google service account JSON file |
| `SHEET_NAME_1`        | Title of the first Google Sheet        |
| `SHEET_NAME_2`        | Title of the second Google Sheet       |

---

## 🛡️ Security Notes

- **Never commit `.env` or `service_account.json` to GitHub**.
- Use `.gitignore` to keep these files out of version control.

---

## 📁 File Naming

- `.env` – Local file with your real credentials (not committed)
- `.env.example` – Template file showing which variables need to be set (safe to commit)
