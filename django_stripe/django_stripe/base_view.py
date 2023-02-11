import json
from json import JSONDecodeError
from typing import Optional, Union

from django.http import JsonResponse
from django.views import View
from pydantic import BaseModel


class BaseView(View):
    schema: Optional[BaseModel] = None

    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            return self._response({'errorMessage': str(e)}, status=400)

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

    def parse_schemas(self):
        if self.schema:
            return self.schema.parse_obj(self.parse_json())
        return None

    def parse_json(self) -> Union[dict, list]:
        return json.loads(self.request.body)
