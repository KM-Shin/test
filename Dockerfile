# 基本のイメージを指定
FROM python:3.13-slim

# 必要なパッケージと依存関係をインストール
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && apt-get clean

# seleniumとその他の依存パッケージをインストール
RUN pip install selenium webdriver-manager

# アプリケーションのファイルをコンテナ内にコピー
COPY chrome.py /app/

# chromedriverをコンテナ内にコピー
COPY path/to/your/chromedriver /usr/local/bin/chromedriver

# 作業ディレクトリを設定
WORKDIR /app

# コンテナ実行時のデフォルトコマンド
CMD ["python", "chrome.py"]
