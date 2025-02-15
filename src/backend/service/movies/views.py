from http import HTTPStatus

from django.shortcuts import redirect, render
from dotenv import load_dotenv

from movies import utils

load_dotenv()

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 3
REVIEWS_PAGE_SIZE = 5


def error_404(request, exception):
    return render(request, "errors/error_404.html", status=HTTPStatus.BAD_REQUEST)


def error_500(request):
    return render(
        request, "errors/error_500.html", status=HTTPStatus.INTERNAL_SERVER_ERROR
    )


def index(request):
    return redirect("movies")


def movies_list(request):
    kwargs = {
        "page": int(request.GET.get("page", DEFAULT_PAGE)),
        "page_size": int(request.GET.get("page_size", DEFAULT_PAGE_SIZE)),
        "search": request.GET.get("search", ""),
    }
    try:
        api_data = utils.fetch_paginated_data_from_api(
            **kwargs, url=utils.get_api_url(request)
        )
        context = {
            "links": api_data["links"],
            "results": api_data["results"],
            "total_pages": api_data["total_pages"],
            **kwargs,
        }
    except Exception as exc:
        return error_404(request, exception=exc)
    return render(request, "movies/movies.html", context=context, status=HTTPStatus.OK)


def movie_detail(request, slug: str):
    api_data_movie = utils.fetch_paginated_data_from_api(url=utils.get_api_url(request))
    kwargs = {  # kwargs for reviews api request
        "page": request.GET.get("page", DEFAULT_PAGE),
        "page_size": REVIEWS_PAGE_SIZE,
    }
    api_data_reviews = utils.fetch_paginated_data_from_api(
        url=utils.get_api_url(request, reviews=True),
        **kwargs,
    )
    api_data_reviews["page"] = int(kwargs["page"])
    context = {
        "movie": api_data_movie,
        "reviews": api_data_reviews,
    }
    return render(
        request, "movies/movie_detail.html", context=context, status=HTTPStatus.OK
    )
