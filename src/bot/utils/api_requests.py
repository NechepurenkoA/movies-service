from urllib.parse import urljoin

import aiohttp
import aiohttp.client_exceptions
import aiohttp.web_exceptions
from aiohttp import ClientResponse

from config import INTERNAL_API_URL
from logger import logger


async def get_data(route: str) -> ClientResponse:
    """Function for API GET request."""
    async with aiohttp.ClientSession() as session:
        try:
            response: ClientResponse = await session.get(
                urljoin(INTERNAL_API_URL, route)
            )
            response_data = await response.json()
            response.raise_for_status()
            logger.info(
                f"API REQUEST - ROUTE: {response.url} | "
                f"METHOD: {response.method} | "
                f"STATUS: {response.status} | "
                f"RESPONSE DATA: {response_data} |"
            )
        except Exception:
            logger.error(
                f"API REQUEST - ROUTE: {response.url} | "
                f"METHOD: {response.method} | "
                f"STATUS: {response.status} | "
                f"RESPONSE DATA: {response_data} |"
            )
    return response


async def post_data(route: str, payload: dict) -> ClientResponse:
    """Function for API POST request."""
    async with aiohttp.ClientSession() as session:
        try:
            response: ClientResponse = await session.post(
                urljoin(INTERNAL_API_URL, route), json=payload
            )
            response_data = await response.json()
            response.raise_for_status()
            logger.info(
                f"API REQUEST - ROUTE: {response.url} | "
                f"METHOD: {response.method} | "
                f"STATUS: {response.status} | "
                f"REQUEST DATA: {payload} | "
                f"RESPONSE DATA: {response_data} |"
            )
        except Exception:
            logger.error(
                f"API REQUEST - ROUTE: {response.url} | "
                f"METHOD: {response.method} | "
                f"STATUS: {response.status} | "
                f"REQUEST_DATA: {payload} | "
                f"RESPONSE DATA: {response_data} |"
            )
        return response


async def patch_data(route: str, payload: dict) -> ClientResponse:
    """Function for API PATCH request."""
    async with aiohttp.ClientSession() as session:
        try:
            response: ClientResponse = await session.patch(
                urljoin(INTERNAL_API_URL, route), json=payload
            )
            response_data = await response.json()
            response.raise_for_status()
            logger.info(
                f"API REQUEST - ROUTE: {response.url} | "
                f"METHOD: {response.method} | "
                f"STATUS: {response.status} | "
                f"REQUEST DATA: {payload} | "
                f"RESPONSE DATA: {response_data} |"
            )
        except Exception:
            logger.error(
                f"API REQUEST - ROUTE: {response.url} | "
                f"METHOD: {response.method} | "
                f"STATUS: {response.status} | "
                f"REQUEST_DATA: {payload} | "
                f"RESPONSE DATA: {response_data} |"
            )
        return response


async def delete_data(route: str) -> ClientResponse:
    """Function for API DELETE request."""
    async with aiohttp.ClientSession() as session:
        try:
            response: ClientResponse = await session.delete(
                urljoin(INTERNAL_API_URL, route)
            )
            response_data = await response.json()
            response.raise_for_status()
            logger.info(
                f"API REQUEST - ROUTE: {response.url} | "
                f"METHOD: {response.method} | "
                f"STATUS: {response.status} | "
                f"RESPONSE DATA: {response_data} |"
            )
        except Exception:
            logger.error(
                f"API REQUEST - ROUTE: {response.url} | "
                f"METHOD: {response.method} | "
                f"STATUS: {response.status} | "
            )
        return response
