from django.contrib import admin

from profiles.inlines import ProfileInLine
from profiles.models import TelegramUser
from reviews.inlines import ReviewInLine


class TelegramUserAdmin(admin.ModelAdmin):
    inlines = [ReviewInLine, ProfileInLine]
    list_display = [
        "telegram_id",
        "join_date",
    ]
    readonly_fields = ["telegram_id", "join_date"]
    empty_value_display = "N/A"

    class Meta:
        model = TelegramUser
        fields = ["telegram_id", "join_date"]


admin.site.register(TelegramUser, TelegramUserAdmin)
