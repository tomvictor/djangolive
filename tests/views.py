from django.http import JsonResponse
from django.views.generic import View


class TestView(View):
    def get(self, *args, **kwargs):
        data = {"key": "test"}
        return JsonResponse(data, status=200)
