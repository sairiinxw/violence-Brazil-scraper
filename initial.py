import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("creds.json",scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1Yrhk75x-urOaxERNbACSQgT6oh-iZEEnxuP3O3Djsh0"
workbook = client.open_by_key(sheet_id)
sheet = workbook.worksheet("Manual Data Scraping (Initial Reference)")

values_list = sheet.row_values(1)
print(values_list)
# gc = gspread.service_account(filename = 'creds.json')
# sh = gc.open('violence_Brazil_dataset').sheet1


# sh.update("B1", "Test update")