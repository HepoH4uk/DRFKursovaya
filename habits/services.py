import requests
from config.settings import TELEGRAM_BOT_TOKEN


def send_telegram_message(message, tg_chat):
    """
    Отправка сообщения в TG
    """
    params = {"text": message, "chat_id": tg_chat}
    requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", params=params)
