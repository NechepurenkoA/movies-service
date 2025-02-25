from aiogram import types

YES_NO_KEYBOARD = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text="Да", callback_data="yes"),
            types.KeyboardButton(text="Нет", callback_data="no"),
        ],
    ],
    resize_keyboard=True,
)
