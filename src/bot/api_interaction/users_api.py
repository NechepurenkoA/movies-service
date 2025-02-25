from aiohttp import ClientResponse

from utils.api_requests import post_data

API_ROUTE = "users/"


async def post_user(**kwargs) -> dict:
    """
    User registration via bot.
    :param user_tg_id: telegram user id
    :return: api data
    """
    response: ClientResponse = await post_data(route=API_ROUTE, payload=kwargs)
    data: dict = await response.json()
    return data
