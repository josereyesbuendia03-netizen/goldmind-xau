from telegram import Update
from telegram.ext import ContextTypes
from database import cursor

async def ranking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cursor.execute(
        "SELECT username, points FROM users ORDER BY points DESC LIMIT 10"
    )
    rows = cursor.fetchall()

    text = "🏆 *Top 10 Ranking*\n\n"
    for i, r in enumerate(rows, 1):
        text += f"{i}. @{r[0]} — {r[1]} pts\n"

    await update.callback_query.edit_message_text(
        text, parse_mode="Markdown"
    )
