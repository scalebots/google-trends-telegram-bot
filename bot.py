import os

from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get("TELEGRAM_TOKEN")
PORT = int(os.environ.get('PORT', '8443'))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

def start(update, context):
    update.message.reply_text(f"Update: {update},\nContext: {context}")

dp.add_handler(CommandHandler("start", start))

updater.start_webhook(
    listen="0.0.0.0", port=PORT, url_path=TOKEN
)
updater.bot.set_webhook(f"https://{HEROKU_APP_NAME}.herokuapp.com/{TOKEN}")
updater.idle()