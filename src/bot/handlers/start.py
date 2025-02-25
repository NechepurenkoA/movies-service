from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from api_interaction.users_api import post_user

start_router = Router()


@start_router.message(CommandStart())
async def handle_start(message: Message) -> None:
    """/start command handler."""
    payload = {
        "telegram_id": message.from_user.id,
    }
    data: dict = await post_user(**payload)
    try:
        await message.answer(
            f"Вы были успешно зарегестрированы! Ваш ник {data["username"]} "
            "Воспользуйтесь меню для последующих действий."
        )
    except Exception:
        await message.answer("Вы уже зарегестрированы.")
