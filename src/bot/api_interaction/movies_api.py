from urllib.parse import urljoin

from requests import Response

from utils.api_requests import get_data

API_ROUTE: str = "movies/"


async def check_movie_exists(slug: str) -> bool:
    """
    GET movie via bot.
    :param slug: slug of a movie
    :return: bool variable, depends on movie existence
    """
    response: Response = await get_data(route=urljoin(API_ROUTE, slug))
    try:
        response.raise_for_status()
    except Exception:
        return False
    return True
