from telegram.ext import Application, CommandHandler
import os

BOT_TOKEN = os.getenv("8365594240:AAHWgX27vCQdPEefWZQwvCLTbmf-M9qcOxc")

async def start(update, context):
    await update.message.reply_text(
        "🤖 GoldMind XAU activo.\n\nUsa /price para ver el precio del oro."
    )

async def price(update, context):
    await update.message.reply_text(
        "📊 Precio XAU/USD próximamente conectado."
    )

def main():
    app = Application.builder().token(8365594240:AAHWgX27vCQdPEefWZQwvCLTbmf-M9qcOxc).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))

    print("🤖 Bot iniciado y en ejecución")

    # 🔥 ESTA LÍNEA ES LA CLAVE
    app.run_polling()

if __name__ == "__main__":
    main()
