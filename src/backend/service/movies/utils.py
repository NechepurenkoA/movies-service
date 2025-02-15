import requests


def fetch_paginated_data_from_api(url: str, **kwargs) -> dict:
    response = requests.get(url, params=kwargs)
    if response.status_code == 200:
        return response.json()  # Assuming the API returns JSON
    return None


def get_api_url(
    request: requests.Request,
    reviews: bool = False,
) -> str:
    if not reviews:
        return f"http://{request.META["HTTP_HOST"]}/api/v1{request.path}"
    return f"http://{request.META["HTTP_HOST"]}/api/v1{request.path}/reviews"
