import json
from json import JSONDecodeError
from typing import Optional, Union

from django.http import JsonResponse
from django.views import View


class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if isinstance(response, (dict, list)):
            return self._response(response)
        return response

    @staticmethod
    def _response(data, *, status=200):
        return JsonResponse(
            data,
            status=status,
            safe=not isinstance(data, list),
        )

