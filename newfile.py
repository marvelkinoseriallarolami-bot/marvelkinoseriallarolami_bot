import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot

# --- WEB SERVER (Render uyquga ketmasligi uchun) ---
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
BOT_TOKEN = "8960435272:AAFU3dzzcjc32r8Fj613TBpphD07EK2egnU"
CHANNEL_ID = -1004366871518

bot = telebot.TeleBot(BOT_TOKEN)

# Kinolar ro'yxati (kod va xabar ID'lari)
MOVIES = {
    "1": [2, 3, 4, 5, 6, 7, 8, 9, 10],
    "2": [11, 12, 13, 14],
    "3": [15],
    "4": [16, 17, 18, 19, 20, 21, 22, 23, 24],
    "5": [25],
    "6": [26, 27, 28],
    "7": [29, 30, 31, 32, 33, 34]
}

@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.reply_to(message, "Xush kelibsiz! Kino kodini yuboring:")

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
    # Bot qotib qolmasligi va o'z-o'zidan tiklanishi uchun infinity_polling ishlatamiz
    bot.infinity_polling(timeout=60, long_polling_timeout=60)
