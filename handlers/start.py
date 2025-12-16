from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database import cursor, conn

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    cursor.execute(
        "INSERT OR IGNORE INTO users (telegram_id, username) VALUES (?,?)",
        (user.id, user.username)
    )
    conn.commit()

    keyboard = [
        [InlineKeyboardButton("🎮 Jugar", callback_data="play")],
        [InlineKeyboardButton("📊 Ranking", callback_data="ranking")]
    ]

    await update.message.reply_text(
        "👋 Bienvenido a *GoldMind XAU*\n\n"
        "Predice el movimiento del oro y gana puntos.\n"
        "⚠️ Juego educativo, no asesoramiento financiero.",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )
