import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
from telebot import TeleBot

# Render xatolik bermasligi uchun fon rejimida ishlaydigan veb-server
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
            self.send_response(200)
                    self.end_headers()
                            self.wfile.write(b"Bot 24/7 ishlamoqda!")

                            def run_server():
                                port = int(os.environ.get("PORT", 8080))
                                    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
                                        server.serve_forever()

                                        # Serverni fonda yurgizish
                                        threading.Thread(target=run_server, daemon=True).start()

                                        # --- TELEGRAM BOT KODI ---
                                        BOT_TOKEN = "7963283259:AAGx1o5X3M4xN-9m2i92O0I0H6k1P2Q3R4S"
                                        bot = TeleBot(BOT_TOKEN)

                                        # Kino kodlari va havolalari
                                        MOVIES = {
                                            "1": "https://t.me/c/2455589578/3",  # 1-kod uchun havola
                                                "2": "https://t.me/c/2455589578/4",  # 2-kod uchun havola
                                                }

                                                @bot.message_handler(commands=['start'])
                                                def send_welcome(message):
                                                    bot.reply_to(message, "Xush kelibsiz! Kino kodini yuboring (masalan: 1 yoki 2):")

                                                    @bot.message_handler(func=lambda message: True)
                                                    def handle_message(message):
                                                        code = message.text.strip()
                                                            if code in MOVIES:
                                                                    bot.reply_to(message, f"Siz so'ragan kino havolasi:\n{MOVIES[code]}")
                                                                        else:
                                                                                bot.reply_to(message, "Kechirasiz, bunday kodli kino topilmadi.")

                                                                                print("Bot muvaffaqiyatli ishga tushdi...")
                                                                                bot.infinity_polling()
                                                                                import os
                                                                                from http.server import HTTPServer, BaseHTTPRequestHandler
                                                                                import threading
                                                                                from telebot import TeleBot

                                                                                # Render xatolik bermasligi uchun fon rejimida ishlaydigan veb-server
                                                                                class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
                                                                                    def do_GET(self):
                                                                                            self.send_response(200)
                                                                                                    self.end_headers()
                                                                                                            self.wfile.write(b"Bot 24/7 ishlamoqda!")

                                                                                                            def run_server():
                                                                                                                port = int(os.environ.get("PORT", 8080))
                                                                                                                    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
                                                                                                                        server.serve_forever()

                                                                                                                        # Serverni fonda yurgizish
                                                                                                                        threading.Thread(target=run_server, daemon=True).start()

                                                                                                                        # --- TELEGRAM BOT KODI ---
                                                                                                                        BOT_TOKEN = "7963283259:AAGx1o5X3M4xN-9m2i92O0I0H6k1P2Q3R4S"
                                                                                                                        bot = TeleBot(BOT_TOKEN)

                                                                                                                        # Kino kodlari va havolalari
                                                                                                                        MOVIES = {
                                                                                                                            "1": "https://t.me/c/2455589578/3",  # 1-kod uchun havola
                                                                                                                                "2": "https://t.me/c/2455589578/4",  # 2-kod uchun havola
                                                                                                                                }

                                                                                                                                @bot.message_handler(commands=['start'])
                                                                                                                                def send_welcome(message):
                                                                                                                                    bot.reply_to(message, "Xush kelibsiz! Kino kodini yuboring (masalan: 1 yoki 2):")

                                                                                                                                    @bot.message_handler(func=lambda message: True)
                                                                                                                                    def handle_message(message):
                                                                                                                                        code = message.text.strip()
                                                                                                                                            if code in MOVIES:
                                                                                                                                                    bot.reply_to(message, f"Siz so'ragan kino havolasi:\n{MOVIES[code]}")
                                                                                                                                                        else:
                                                                                                                                                                bot.reply_to(message, "Kechirasiz, bunday kodli kino topilmadi.")

                                                                                                                                                                print("Bot muvaffaqiyatli ishga tushdi...")
                                                                                                                                                                bot.infinity_polling()
                                                                                                                                                                
