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
ADMIN_ID = 8735850351

bot = telebot.TeleBot(BOT_TOKEN)

# Kinolar ro'yxati (o'zgartirilmadi)
MOVIES = {
    "1": [2, 3, 4, 5, 6, 7, 8, 9, 10],
    "2": [11, 12, 13, 14],
    "3": [15],
    "4": [16, 17, 18, 19, 20, 21, 22, 23, 24],
    "5": [25],
    "6": [26, 27, 28],
    "7": [29, 30, 31, 32, 33, 34],
    "8": [35, 36, 37, 38],
    "9": [39, 40, 41, 42, 43, 44],
    "10": [45, 46, 47, 48, 49, 50],
    "11": [51, 53, 54, 55],
    "12": [56, 57],
    "13": [58, 59],
    "14": [60],
    "15": [61, 62, 63],
    "16": [64],
    "17": [65],
    "18": [66, 67, 68, 69, 70, 71, 72, 73],
    "19": [75],
    "20": [76, 77]
}

# Foydalanuvchini faylga yozib borish funksiyasi
def save_user(user_id):
    try:
        with open("users.txt", "a+") as f:
            f.seek(0)
            users = f.read().splitlines()
            if str(user_id) not in users:
                f.write(f"{user_id}\n")
    except Exception as e:
        print(f"Xatolik: {e}")

# /start buyrug'i
@bot.message_handler(commands=['start'])
def start_cmd(message):
    save_user(message.chat.id)
    bot.reply_to(message, "Xush kelibsiz! Kino kodini yuboring:")

# /stat buyrug'i (faqat siz uchun ishlaydi)
@bot.message_handler(commands=['stat'])
def show_stats(message):
    if message.chat.id == ADMIN_ID:
        try:
            with open("users.txt", "r") as f:
                users = set(f.read().splitlines())
            bot.send_message(message.chat.id, f"📊 Jami foydalanuvchilar: {len(users)} ta")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "📊 Hozircha foydalanuvchilar yo'q.")

# Kino kodlarini qabul qilish (har doim eng pastda turishi shart)
@bot.message_handler(func=lambda msg: True)
def handle_text(message):
    save_user(message.chat.id)
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
    bot.infinity_polling(timeout=60, long_polling_timeout=60)


