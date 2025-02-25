from aiogram import types

SETTINGS_KEYBOARD = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text="Изменить юзернейм профиля ✏️", callback_data="change_username"
            )
        ]
    ],
)
