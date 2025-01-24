FROM python:3.12-slim
WORKDIR /app
COPY . /app
ENV TELEGRAM_BOT_TOKEN "7111576325:AAEQ6wXGmlnfg6GZzfooLiBN5PWv7S1V9tg"
ENV DATABASE_PATH "reminder.db"
RUN pip install -r requirements.txt