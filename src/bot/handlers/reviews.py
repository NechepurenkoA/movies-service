from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from django.utils.text import slugify

from api_interaction.movies_api import check_movie_exists
from api_interaction.reviews_api import check_review_exists, delete_review, post_review
from create_bot import bot
from exceptions.reviews import NotAllValuesPassed, ReviewAlreadyExists
from keyboards.base import YES_NO_KEYBOARD
from keyboards.reviews import REVIEW_INIT_KEYBOARD
from messages.reviews import REVIEW_TEMPLATE

review_router = Router(name="reviews")


class ReviewStates(StatesGroup):
    """FSM states."""

    movie = State()
    text = State()
    rating = State()
    confirming_review = State()
    delete_or_not = State()
    review_id = State()


@review_router.message(Command("review"))
async def handle_review(message: types.Message, state: FSMContext) -> None:
    """Command for reviewing."""
    await state.clear()
    await message.answer(
        "Заполните обязательные поля, они выделены ❗️",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    await message.answer(
        "Хотите оставить отзыв? Укажите нужные параметры внизу:",
        reply_markup=REVIEW_INIT_KEYBOARD,
    )


async def continue_review(message: types.Message, state: FSMContext) -> None:
    """Continue review function."""
    review_data = await state.get_data()
    await message.answer(
        REVIEW_TEMPLATE.format(
            review_data.get("movie", "артикул-не-указан"),
            review_data.get("text", "Текст отсутствует"),
            review_data.get("rating", "N"),
        ),
        reply_markup=REVIEW_INIT_KEYBOARD,
        parse_mode=ParseMode.HTML,
    )


@review_router.callback_query(lambda c: c.data in ["movie", "text", "rating"])
async def process_callback(
    callback_query: types.CallbackQuery, state: FSMContext
) -> None:
    user_id = callback_query.from_user.id
    await callback_query.answer()
    if callback_query.data == "movie":
        await state.set_state(ReviewStates.movie)
        await bot.send_message(
            user_id,
            "Пожалуйста, введите артикул фильма:",
            reply_markup=types.ForceReply(selective=True),
        )
    elif callback_query.data == "text":
        await state.set_state(ReviewStates.text)
        await bot.send_message(
            user_id,
            "Пожалуйста, введите ваш отзыв:",
            reply_markup=types.ForceReply(selective=True),
        )
    elif callback_query.data == "rating":
        await state.set_state(ReviewStates.rating)
        await bot.send_message(
            user_id,
            "Пожалуйста, введите вашу оценку (от 1 до 10):",
            reply_markup=types.ForceReply(selective=True),
        )


@review_router.message(ReviewStates.movie)
async def process_movie(message: types.Message, state: FSMContext) -> None:
    slug = slugify(message.text, allow_unicode=True)
    if await check_movie_exists(slug):
        await state.update_data(movie=slug)
        await continue_review(message, state)
    else:
        await message.answer(
            "Такого артикула нет, пожалуйста перепроверьте правильность написания."
        )


@review_router.message(ReviewStates.text)
async def process_review(message: types.Message, state: FSMContext) -> None:
    await state.update_data(text=message.text)
    await continue_review(message, state)


@review_router.message(ReviewStates.rating)
async def process_rating(message: types.Message, state: FSMContext) -> None:
    try:
        rating = int(message.text)
        if 1 <= rating <= 10:
            await state.update_data(rating=rating)
        else:
            raise ValueError()
    except ValueError:
        await message.answer(
            "Пожалуйста, введите число от 1 до 10.",
            reply_markup=types.ForceReply(selective=True),
        )
    else:
        await continue_review(message, state)


@review_router.callback_query(lambda c: c.data == "submit")
async def submit_review(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback_query.from_user.id
    try:
        review_data = await state.get_data()
        review_data["telegram_user_id"] = user_id
        if not {"movie", "rating"}.issubset(review_data.keys()):
            raise NotAllValuesPassed
        review_id = await check_review_exists(review_data["movie"], user_id)
        if review_id:
            await state.update_data(review_id=review_id)
            raise ReviewAlreadyExists
        await state.clear()
        await post_review(**review_data)
        await callback_query.answer(
            "Отзыв успешно отправлен!",
        )
        await bot.send_message(
            user_id,
            "Спасибо за ваш отзыв!",
            reply_markup=types.ReplyKeyboardRemove(),
        )
    except NotAllValuesPassed:
        await callback_query.answer()
        await bot.send_message(
            user_id,
            "Не все обязательные поля были заполнены, "
            "пожалуйста, укажите все необходимые поля.",
            reply_markup=types.ReplyKeyboardRemove(),
        )
    except ReviewAlreadyExists:
        await callback_query.answer()
        await state.set_state(ReviewStates.delete_or_not)
        await bot.send_message(
            user_id,
            "Вы уже отправляли отзыв на этот фильм, хотите его удалить?",
            reply_markup=YES_NO_KEYBOARD,
        )
    except Exception:
        await callback_query.answer()
        await bot.send_message(
            user_id,
            "Что-то пошло не так, повторите попытку позже.",
            reply_markup=types.ReplyKeyboardRemove(),
        )
        await state.clear()


@review_router.message(ReviewStates.delete_or_not, F.text.casefold() == "да")
async def process_delete_yes(message: types.Message, state: FSMContext) -> None:
    review_data: dict = await state.get_data()
    await delete_review(review_data.pop("review_id"))
    await state.update_data(review_data)
    await message.reply(
        (
            "Ваш отзыв о фильме был удален, чтобы отправить этот - закончите "
            "заполнение формы и нажмите отправить."
        ),
        reply_markup=types.ReplyKeyboardRemove(),
    )
    await message.answer(
        REVIEW_TEMPLATE.format(
            review_data.get("movie", "артикул-не-указан"),
            review_data.get("text", "Текст отсутствует"),
            review_data.get("rating", "N"),
        ),
        reply_markup=REVIEW_INIT_KEYBOARD,
    )


@review_router.message(ReviewStates.delete_or_not, F.text.casefold() == "нет")
async def process_delete_no(message: types.Message, state: FSMContext) -> None:
    await state.update_data(movie=None)
    await message.reply(
        "Введите новый артикул для фильма.",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    await continue_review(message, state)


@review_router.callback_query(lambda c: c.data == "cancel")
async def cancel_review(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback_query.from_user.id
    await callback_query.answer("Отменено.")
    await state.clear()
    await bot.send_message(
        user_id,
        "Хорошо, если захотите оставить отзыв вновь напишите команду /review",
        reply_markup=types.ReplyKeyboardRemove(),
    )
