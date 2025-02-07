from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from dotenv import load_dotenv
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from movies import views

load_dotenv()


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("profiles.urls")),
    path("api/", include("directors.urls")),
    path("api/", include("actors.urls")),
    path("api/", include("movies.urls")),
    path("api/", include("reviews.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("movies/", views.movies_list, name="movies"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + debug_toolbar.toolbar.debug_toolbar_urls()
    )
