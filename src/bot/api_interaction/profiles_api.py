from urllib.parse import urljoin

from aiohttp import ClientResponse

from utils.api_requests import patch_data

API_ROUTE = "profiles/"


async def patch_profile(**kwargs) -> dict:
    """
    Change profile username via bot.
    :return: api data
    """
    telegram_id = kwargs.pop("telegram_id")
    response: ClientResponse = await patch_data(
        route=urljoin(API_ROUTE, f"{telegram_id}/"),
        payload=kwargs,
    )
    data: dict = await response.json()
    return data
