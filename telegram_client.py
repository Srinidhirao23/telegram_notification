import json

from telethon import TelegramClient

from app_config import AppConfig

app_conf = AppConfig()
api_id = app_conf.get_api_id()
api_hash = app_conf.get_hash_id()

client = TelegramClient('session_name', api_id, api_hash)


def send_telegram_message(message):
    parsed_message = json.loads(message)
    with TelegramClient("session_name", api_id, api_hash) as client:
        client.loop.run_until_complete(
            client.send_message(parsed_message['phone_no'], parsed_message['data'].get('message')))
