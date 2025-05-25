import os
import json
from flask import Flask, render_template
import gspread
from google.oauth2 import service_account
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ดึงข้อมูลจาก Environment Variable
creds_info = json.loads(os.environ["GOOGLE_CREDS_JSON"])
creds = service_account.Credentials.from_service_account_info(creds_info)
client = gspread.authorize(creds)

SHEET_ID = os.environ.get("SHEET_ID", "")
sheet = client.open_by_key(SHEET_ID).sheet1

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list")
def list_view():
    records = sheet.get_all_records()
    return render_template("list.html", records=records)

if __name__ == "__main__":
    app.run(debug=True)