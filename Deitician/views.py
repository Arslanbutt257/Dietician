from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .Deit_config import *


# Create your views here.
class DietSuggestion(APIView):
    def post(self, request):
        if 'age' in request.data:
            inputs = list(request.data.values())
            result = suggestions(inputs)
            return Response(result, status=status.HTTP_200_OK)
        else:
            Response('Invalid Json Format', status=status.HTTP_400_BAD_REQUEST)

