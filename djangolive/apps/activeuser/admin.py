from django.contrib import admin

from .models import ActiveUserLog, UserActivityHistory
from django.utils import timezone
import datetime


class ActiveUserLogFilter(admin.SimpleListFilter):
    title = "Activity Filter"

    parameter_name = "time"

    def lookups(self, request, model_admin):
        return (
            ("1", "1 Minutes"),
            ("5", "5 Minutes"),
            ("15", "15 Minutes"),
            ("30", "30 Minutes"),
            ("45", "45 Minutes"),
            ("60", "1 Hour"),
            (str(60 * 6), "6 Hour"),
            (str(60 * 12), "12 Hour"),
            (str(60 * 24), "24 Hour"),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value is None:
            return queryset
        return queryset.filter(
            time__gt=timezone.now() - datetime.timedelta(minutes=int(value))
        )


@admin.register(ActiveUserLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "time",
    ]

    list_display_links = ["id", "user"]
    search_fields = ["id", "user__first_name"]
    exclude = ["id"]

    list_filter = (ActiveUserLogFilter,)


@admin.register(UserActivityHistory)
class UserActivityHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "request_path",
        "request_method",
        "request_scheme",
        "timestamp",
    ]

    list_display_links = ["id", "user"]
    search_fields = ["id", "user__first_name"]
    exclude = ["id"]
