from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import sys
import os

# 実行ファイル内でのchromedriverのパスを設定
if getattr(sys, 'frozen', False):  # 実行ファイルとして動作しているかを確認
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
else:  # 通常のスクリプト実行
    # Windowsの場合のchromedriverのパスを指定
    chromedriver_path = r"C:\Users\km-shin\Documents\chromedriver-win64\chromedriver.exe"  # ここを実際のパスに修正

# Chromeの設定
service = Service(chromedriver_path)
options = webdriver.ChromeOptions()

# ヘッドレスモードを無効にしてブラウザを表示
# options.add_argument('--headless')  # この行を削除またはコメントアウト

# ブラウザを開く
try:
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.rakuten.co.jp/")  # 楽天市場にアクセス
    print("楽天市場にアクセスしました。")

    time.sleep(5)  # 5秒待機

finally:
    if 'driver' in locals():
        driver.quit()  # ブラウザを閉じる
    print("ブラウザを閉じました。")
