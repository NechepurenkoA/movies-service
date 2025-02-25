from http import HTTPStatus
from urllib.parse import urljoin

from aiohttp import ClientResponse

from api_interaction.movies_api import API_ROUTE as MOVIE_ROUTE
from utils.api_requests import delete_data, get_data, post_data

API_ROUTE = "reviews/"


async def post_review(**kwargs) -> dict:
    """
    POST user's review via bot.
    :param telegram_id: telegram user id
    :param data: review data {"slug": ..., "text": ..., "rating": ...}
    """
    response: ClientResponse = await post_data(route=API_ROUTE, payload=kwargs)
    data = await response.json()
    return data


async def delete_review(id: int) -> None:
    """
    DELETE user's review via bot.
    """
    print(urljoin(API_ROUTE, f"{str(id)}/"))
    await delete_data(route=urljoin(API_ROUTE, f"{str(id)}/"))


async def check_review_exists(slug: str, telegram_id: int) -> int | None:
    """
    GET user's review via bot.
    :param telegram_id: telegram user id
    :return: None
    """
    route_to_movie = urljoin(MOVIE_ROUTE, f"{slug}/")
    route_to_reviews = urljoin(route_to_movie, API_ROUTE)
    response: ClientResponse = await get_data(
        route=urljoin(route_to_reviews, str(telegram_id))
    )
    if response.status == HTTPStatus.OK:
        response: dict = await response.json()
        return response["id"]
    return None
