from django.db import models
from django.conf import settings


class AccessLog(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        related_name="user_access_log",
        unique=True,
    )
    timestamp = models.DateTimeField(null=False, blank=False)
    last_updated = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "djangolive_access_log"
        verbose_name = "Access log"
        verbose_name_plural = "Access log"
        ordering = ["-id"]

    def __str__(self):
        return str(self.user)

    @classmethod
    def last_active_log(cls, user):
        qs = cls.objects.filter(user=user)
        if qs.exists():
            return True, qs.get(user=user)
        else:
            return False, None
