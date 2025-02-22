from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enlace al dashboard web
DASHBOARD_URL = "https://tu-servidor.com/dashboard"

# Comando /start para iniciar el bot
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Ver Dashboard de Criptomonedas", url=DASHBOARD_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "¡Hola! Haz clic en el botón de abajo para ver tu dashboard de criptomonedas.",
        reply_markup=reply_markup
    )

# Configuración del bot
def main():
    # Usa el token de tu bot de Telegram
    TOKEN = 'BOT_TOKEN'
    
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
