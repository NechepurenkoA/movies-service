from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from api_interaction.profiles_api import patch_profile
from create_bot import bot
from keyboards.base import YES_NO_KEYBOARD
from keyboards.settings import SETTINGS_KEYBOARD

settings_router = Router()


class SettingsState(StatesGroup):
    username = State()
    set_username = State()


@settings_router.message(Command("settings"))
async def handle_settings(message: Message, state: FSMContext) -> None:
    """/settings command handler."""
    await state.clear()
    await message.answer(
        "Доступные вам настройки.", reply_markup=types.ReplyKeyboardRemove()
    )
    await message.answer(
        "⚙️ Настройки 🛠",
        reply_markup=SETTINGS_KEYBOARD,
    )


@settings_router.callback_query(lambda c: c.data == "change_username")
async def change_username(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(SettingsState.username)
    await callback_query.answer()
    await bot.send_message(
        callback_query.from_user.id,
        "Введите свой новый юзернейм.",
        reply_markup=types.ForceReply(selective=True),
    )


@settings_router.message(SettingsState.username)
async def process_movie(message: types.Message, state: FSMContext) -> None:
    await state.update_data(username=message.text)
    await state.set_state(SettingsState.set_username)
    await message.reply(
        "Вы точно хотите установить этот ник?",
        reply_markup=YES_NO_KEYBOARD,
    )


@settings_router.message(SettingsState.set_username, F.text.casefold() == "да")
async def submit_review(message: types.Message, state: FSMContext) -> None:
    payload = {
        "telegram_id": str(message.from_user.id),
        "username": await state.get_value("username"),
    }
    data = await patch_profile(**payload)
    await message.answer(
        f"Ваш юзернейм успешно изменен. Теперь вы *{data["username"]}*!",
        reply_markup=types.ReplyKeyboardRemove(),
        parse_mode=ParseMode.MARKDOWN,
    )


@settings_router.message(SettingsState.set_username, F.text.casefold() == "нет")
async def process_change_username(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "Изменение было отменено.",
        reply_markup=types.ReplyKeyboardRemove,
    )
