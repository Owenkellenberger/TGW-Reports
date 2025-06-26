import os
from dotenv import load_dotenv
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread

# Load environment variables from .env file
load_dotenv()

SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
SHEET_NAME_1 = os.getenv("SHEET_NAME_1")
SHEET_NAME_2 = os.getenv("SHEET_NAME_2")

# Authenticate using gspread
gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)

# Open sheets by name from environment
sheet1 = gc.open(SHEET_NAME_1)
sheet2 = gc.open(SHEET_NAME_2)

# Sample data to upload
df = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age": [30, 25]
})

# Example: Upload to first sheet (Sheet1 tab)
worksheet1 = sheet1.sheet1
worksheet1.update([df.columns.values.tolist()] + df.values.tolist())

# Example: Upload to second sheet (Sheet1 tab)
worksheet2 = sheet2.sheet1
worksheet2.update([df.columns.values.tolist()] + df.values.tolist())

print("Both sheets updated successfully.")
