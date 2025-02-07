from django.contrib import admin

from profiles.inlines import ProfileInLine
from profiles.models import Profile, TelegramUser
from reviews.inlines import ReviewInLine


class TelegramUserAdmin(admin.ModelAdmin):
    inlines = [ReviewInLine, ProfileInLine]
    list_display = [
        "telegram_id",
        "join_date",
        "id",
    ]
    readonly_fields = [
        "telegram_id",
        "join_date",
    ]
    empty_value_display = "N/A"

    class Meta:
        model = TelegramUser
        fields = ["telegram_id", "join_date"]

    def get_queryset(self, request):
        return TelegramUser.objects.all().select_related("profile")


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["telegram_account__telegram_id", "username", "id"]
    readonly_fields = ["username", "telegram_account", "id"]
    empty_value_display = "N/A"

    class Meta:
        model = TelegramUser
        fields = ["username", "telegram_account"]

    def get_queryset(self, request):
        return Profile.objects.all().select_related("telegram_account")


admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(Profile, ProfileAdmin)
