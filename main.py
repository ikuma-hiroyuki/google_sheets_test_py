import os

import gspread
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

# 認証情報を取得
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(os.getenv('JSON_FILE_NAME'), scope)

# 操作権を取得
gc = gspread.authorize(credentials)

# ブックを取得
wb = gc.open_by_key(os.getenv('SHEET_KEY'))

# スプレッドシートを取得
ws = wb.worksheet('シート1')

# セルの値を取得
print(ws.acell('A1').value)

try:
    # 新しいシートを作成
    ws2 = wb.add_worksheet(title='シート2', rows='100', cols='20')

    # 新しいシートに書き込む
    ws2.update_acell('A1', 'Hello World!')
except gspread.exceptions.APIError:
    print('シート2はすでに存在しています')

# wsの最終行に値を書き込む
ws.append_row(['Hello', 'World'])
