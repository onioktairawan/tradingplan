import asyncio
import logging
from telethon import TelegramClient, events
from telegram import Bot
from telegram.error import TelegramError

# Konfigurasi logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# API ID & API HASH dari my.telegram.org
API_ID = 23581804  # Ganti dengan API ID-mu
API_HASH = "49fd7d9ac9aecb487c343a0c1156f8d2"  # Ganti dengan API HASH-mu

# Token bot dari BotFather (PASTIKAN TOKEN BARU)
BOT_TOKEN = "7500495219:AAGiGwm4yFkH79jE_kpxTdHg4d2M8DKfKzE"

# ID Channel sumber (format -100XXXXXXXXXX)
CHANNEL_SOURCE_ID = -1002156702383  # ID channel sumber

# ID Grup atau Channel tujuan (format -100XXXXXXXXXX)
TARGET_CHAT_ID = -1002325511325  # ID grup/channel tujuan

# Inisialisasi Telethon Client
client = TelegramClient("session_name", API_ID, API_HASH)
bot = Bot(token=BOT_TOKEN)

@client.on(events.NewMessage(chats=CHANNEL_SOURCE_ID))
async def forward_message(event):
    """ Mengambil pesan dari channel sumber dan meneruskannya ke tujuan """
    message = event.message.text
    if message:
        logging.info(f"Pesan diterima dari {CHANNEL_SOURCE_ID}: {message}")
        try:
            await bot.send_message(chat_id=TARGET_CHAT_ID, text=message)
            logging.info(f"✅ Pesan berhasil diteruskan ke {TARGET_CHAT_ID}")
        except TelegramError as e:
            logging.error(f"❌ Gagal mengirim pesan ke {TARGET_CHAT_ID}: {e}")

async def main():
    """Menjalankan bot"""
    logging.info("🚀 Bot berjalan, menunggu pesan baru...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
