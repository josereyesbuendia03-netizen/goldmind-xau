from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler
)

from config import BOT_TOKEN
from handlers.start import start
from handlers.play import play, predict
from handlers.ranking import ranking

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(play, pattern="^play$"))
    app.add_handler(CallbackQueryHandler(predict, pattern="^(up|down)_"))
    app.add_handler(CallbackQueryHandler(ranking, pattern="^ranking$"))

    print("🤖 GoldMind XAU iniciado")
    app.run_polling()

if __name__ == "__main__":
    main()
