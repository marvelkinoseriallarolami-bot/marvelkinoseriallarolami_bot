import time
import requests

BOT_TOKEN = "8960435272:AAH67OLzLHOiqyBe0izLpmwvEVu-GjdJENc"
CHANNEL_ID = -1004366871518

MOVIES = {
    "1": [2, 3, 4, 5, 6, 7, 8, 9, 10],  # Bu yerga kerakli post raqamlarini yozasiz
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
    res = requests.post(url, json=data).json()
    return res.get("ok", False)

def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates?timeout=30"
    if offset:
        url += f"&offset={offset}"
    try:
        response = requests.get(url, timeout=35)
        return response.json().get("result", [])
    except Exception:
        return []

print("Bot muvaffaqiyatli ishga tushdi!")

last_update_id = None

while True:
    updates = get_updates(last_update_id)
    for update in updates:
        last_update_id = update["update_id"] + 1
        
        message = update.get("message")
        if not message:
            continue
            
        chat_id = message["chat"]["id"]
        text = message.get("text", "").strip()

        if text == "/start":
            send_message(chat_id, "Assalomu alaykum! Kinoning kodini yuboring:")
        elif text in MOVIES:
            post_ids = MOVIES[text]
            send_message(chat_id, f"Kino qismlari yuklanmoqda ({len(post_ids)} ta qism)... ⏳")
            for post_id in post_ids:
                success = forward_message(chat_id, CHANNEL_ID, post_id)
                time.sleep(1)
        elif text.isdigit():
            success = forward_message(chat_id, CHANNEL_ID, int(text))
            if not success:
                send_message(chat_id, "Bunday kodli kino topilmadi! ❌")

    time.sleep(1)
