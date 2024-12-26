# 使用するイメージ
FROM python:3.12-slim

# コンテナ内の作業ディレクトリを設定する
WORKDIR /app

COPY requirements.txt .

# poetryとプロジェクトの依存関係をインストールする
RUN pip install -r requirements.txt

# 残りのアプリケーションコードをコンテナにコピーする
COPY . /app

# アプリが動作するポートを公開する
EXPOSE 8080

# コンテナ起動時にapp.pyを実行する
CMD ["streamlit", "run", "--server.port", "8080", "aribayashi.py"]