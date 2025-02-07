from http import HTTPMethod

import requests
from django.shortcuts import render


def movies_list(request):
    data = requests.request(
        HTTPMethod.GET, "http://127.0.0.1:8000/api/v1/movies/"
    ).json()
    return render(request, "movies/movies.html", context={"data": data})
