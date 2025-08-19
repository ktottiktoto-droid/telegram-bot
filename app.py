# app.py
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# === 8432529632:AAEJVSEF7a9MN9lx-Fp8vcsKv5WRPLS2NcA ===
TOKEN = os.getenv("BOT_TOKEN", "8432529632:AAEJVSEF7a9MN9lx-Fp8vcsKv5WRPLS2NcA")
URL = f"https://api.telegram.org/bot{TOKEN}/"

def send_message(chat_id, text):
    url = URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Ошибка отправки:", e)

@app.route('/')
def home():
    return "<h1>🤖 Бот работает на Render!</h1><p>Не закрывай вкладку. Вебхук уже настроен.</p>"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data:
        return "No data", 400

    if 'message' in data:
        message = data['message']
        chat_id = message['chat']['id']
        text = message.get('text', '')
        user = message['from'].get('first_name', 'Аноним')

        if text == '/start':
            send_message(chat_id, f"Привет, {user}! 🚀 Бот работает на <b>Render.com</b>!")
        elif text == '/help':
            send_message(chat_id, "Пока я умею только /start и /help")
        else:
            send_message(chat_id, f"Ты написал: <b>{text}</b>\n\nЯ получил твоё сообщение!")

    return "ok", 200