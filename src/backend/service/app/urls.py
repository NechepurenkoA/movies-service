import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from dotenv import load_dotenv

load_dotenv()


urlpatterns = [
    path("admin/", admin.site.urls),
]

if os.getenv("DEBUG") == "True":
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
