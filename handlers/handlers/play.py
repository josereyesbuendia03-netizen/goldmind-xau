import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from prices import get_xau_price
from database import cursor, conn

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [[
        InlineKeyboardButton("📈 Sube", callback_data="up_5"),
        InlineKeyboardButton("📉 Baja", callback_data="down_5")
    ]]

    await query.edit_message_text(
        "¿Qué hará XAU/USD en los próximos *5 minutos*?",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    direction, tf = query.data.split("_")
    price = get_xau_price()

    cursor.execute(
        """INSERT INTO predictions
        (telegram_id, direction, price_open, timeframe, timestamp)
        VALUES (?,?,?,?,?)""",
        (query.from_user.id, direction, price, int(tf)*60, int(time.time()))
    )
    conn.commit()

    await query.edit_message_text(
        f"📌 Predicción registrada\n\n"
        f"Dirección: *{'SUBE' if direction=='up' else 'BAJA'}*\n"
        f"Precio actual: `{price}`",
        parse_mode="Markdown"
    )
