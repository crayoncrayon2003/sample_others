FROM python:3.11-slim

WORKDIR /app

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# ActivityWatchのダウンロード（最新版v0.13.2）
RUN curl -L https://github.com/ActivityWatch/activitywatch/releases/download/v0.13.2/activitywatch-v0.13.2-linux-x86_64.zip -o aw.zip \
    && unzip aw.zip \
    && rm aw.zip \
    && chmod +x activitywatch/aw-server/aw-server

EXPOSE 5600

# 0.0.0.0でバインドするように--hostオプションを指定
CMD ["./activitywatch/aw-server/aw-server", "--host", "0.0.0.0"]