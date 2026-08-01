      import os
import time
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot 24/7 ishlamoqda!")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

BOT_TOKEN = "8960435272:AAH67oLzLHOiqyBe0izLpm"
CHANNEL_ID = -1004366871518

MOVIES = {
    "1": [2, 3, 4, 5, 6, 7, 8, 9, 10],
    "2": [11, 12, 13, 14],
    "100": [4, 5, 6]
}

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(chat_id, text):
    requests.post(f"{BASE_URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })

def forward_message(chat_id, from_chat_id, message_id):
    url = f"{BASE_URL}/forwardMessage"
    data = {
        "chat_id": chat_id,
        "from_chat_id": from_chat_id,
        "message_id": message_id
    }
    requests.post(url, json=data)

def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates?timeout=30"
    if offset:
        url += f"&offset={offset}"
    response = requests.get(url)
    return response.json()

def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    offset = None
    while True:
        try:
            updates = get_updates(offset)
            if "result" in updates:
                for update in updates["result"]:
                    offset = update["update_id"] + 1
                    if "message" in update and "text" in update["message"]:
                        chat_id = update["message"]["chat"]["id"]
                        text = update["message"]["text"].strip()

                        if text == "/start":
                            send_message(chat_id, "Xush kelibsiz! Kino kodini yuboring (masalan: 1):")
                        elif text in MOVIES:
                            for msg_id in MOVIES[text]:
                                forward_message(chat_id, CHANNEL_ID, msg_id)
                        else:
                            send_message(chat_id, "Bunday kodli kino topilmadi.")
        except Exception as e:
            print(f"Xatolik: {e}")
            time.sleep(3)

if __name__ == "__main__":
    main()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
