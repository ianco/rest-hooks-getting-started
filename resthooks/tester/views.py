### views.py ###
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseServerError

from rest_framework import viewsets

from rest_hooks.models import Hook

from .serializers import HookSerializer

import random


class HookViewSet(viewsets.ModelViewSet):
    """
    Retrieve, create, update or destroy webhooks.
    """
    queryset = Hook.objects.all()
    model = Hook
    serializer_class = HookSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@csrf_exempt
def echo_view(request):
    if request.method == 'POST':
        post_data = request.body
        print(post_data)
        return JsonResponse({"thanks": "you"})

    return JsonResponse({"method": "notsupported"})


@csrf_exempt
def error_view(request):
    if request.method == 'POST':
        post_data = request.body
        print(post_data)
        return HttpResponseServerError()

    return JsonResponse({"method": "notsupported"})


@csrf_exempt
def random_view(request):
    if request.method == 'POST':
        post_data = request.body
        print(post_data)
        if 0.5 < random.random():
            return JsonResponse({"thanks": "you"})
        else:
            return HttpResponseServerError()

    return JsonResponse({"method": "notsupported"})

