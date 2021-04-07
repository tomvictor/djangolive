from .models import AccessLog
from django.utils import timezone


class DjangoliveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            if AccessLog.objects.filter(user=request.user).exists():
                activity_object = AccessLog.objects.get(user=request.user)
                activity_object.timestamp = timezone.now()
                activity_object.save()
            else:
                AccessLog.objects.create(user=request.user)

        return response
