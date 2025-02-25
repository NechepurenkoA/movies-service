from aiogram import types

from config import SITE_URL

REVIEW_INIT_KEYBOARD = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="❗️Артикул❗️", callback_data="movie"),
            types.InlineKeyboardButton(text="❗️Оценка❗️", callback_data="rating"),
        ],
        [
            types.InlineKeyboardButton(text="Текст", callback_data="text"),
        ],
        [
            types.InlineKeyboardButton(text="Отправить ✅", callback_data="submit"),
        ],
        [
            types.InlineKeyboardButton(text="Отменить ❌", callback_data="cancel"),
        ],
        [
            types.InlineKeyboardButton(text="Все фильмы 🎥", url=SITE_URL),
        ],
    ]
)
