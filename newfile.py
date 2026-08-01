import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot

# --- WEB SERVER (Render porti uchun) ---
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot ishlamoqda!")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# --- BOT KODI ---
BOT_TOKEN = "8960435272:AAEnFZT4NQrkEXjs0vjImqSZstcxNM_Agj8"
CHANNEL_ID = -1004366871518

bot = telebot.TeleBot(BOT_TOKEN)

MOVIES = {
    "1": [2, 3, 4, 5, 6, 7, 8, 9, 10],
    "2": [11, 12, 13, 14],
    "3": [15]
}

@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.reply_to(message, "Xush kelibsiz! Kino kodini yuboring (masalan: 1):")

@bot.message_handler(func=lambda msg: True)
def handle_text(message):
    code = message.text.strip()
    if code in MOVIES:
        for msg_id in MOVIES[code]:
            try:
                bot.forward_message(message.chat.id, CHANNEL_ID, msg_id)
            except Exception as e:
                print(f"Xatolik: {e}")
    else:
        bot.reply_to(message, "Bunday kodli kino topilmadi.")

if __name__ == "__main__":
    bot.infinity_polling()
                                                

