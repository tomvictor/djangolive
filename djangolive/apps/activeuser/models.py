from django.db import models
from django.conf import settings
from core.models import CoreModel


class ActiveUserLog(CoreModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        related_name="activity_log",
        unique=True,
    )
    time = models.DateTimeField(null=False, blank=False)

    class Meta:
        db_table = "active_user_log"
        verbose_name = "Active User"
        verbose_name_plural = "Active users"
        ordering = ["-id"]

    def __str__(self):
        return str(self.user)


class UserActivityHistory(CoreModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        related_name="activity_history",
    )
    request_path = models.TextField(null=True)
    request_method = models.TextField(null=True)
    request_scheme = models.CharField(max_length=10240, blank=True, null=True)
    request_remote_addr = models.TextField(null=True)
    request_user_agent = models.TextField(null=True)
    request_origin = models.TextField(null=True)

    class Meta:
        db_table = "user_activity_history"
        verbose_name = "User Activity History"
        verbose_name_plural = "User Activity Histories"
        ordering = ["-id"]

    def __str__(self):
        return str(self.user)
