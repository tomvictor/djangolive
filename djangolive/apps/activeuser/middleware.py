from .models import ActiveUserLog, UserActivityHistory
from django.utils import timezone
from django.conf import settings

ACTIVITY_HISTORY_ENABLED = getattr(settings, "ACTIVITY_HISTORY_ENABLED", True)


class ActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            if ActiveUserLog.objects.filter(user=request.user).exists():
                instance = ActiveUserLog.objects.get(user=request.user)
                instance.time = timezone.now()
                instance.save()
                self.log_activity(request)
            else:
                ActiveUserLog.objects.create(user=request.user, time=timezone.now())
                self.log_activity(request)

        return response

    def log_activity(self, request):
        context = {
            "user": request.user,
            "timestamp": timezone.now(),
            "request_path": request.path,
            "request_method": request.method,
            "request_scheme": request.scheme,
            "request_remote_addr": request.META.get("REMOTE_ADDR"),
            "request_user_agent": request.META.get("HTTP_USER_AGENT"),
            "request_origin": request.META.get("HTTP_ORIGIN"),
        }
        if ACTIVITY_HISTORY_ENABLED:
            UserActivityHistory.objects.create(**context)
