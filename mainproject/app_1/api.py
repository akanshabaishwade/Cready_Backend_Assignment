from urllib.request import Request
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from requests.auth import HTTPBasicAuth




# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


import requests
import json
from rest_framework.decorators import api_view


@api_view(('GET',))
def GetAllMovie(request):
    response_API = requests.get('https://demo.credy.in/api/v1/maya/movies/')
    all_data = response_API.text
    print(response_API.text)
    parse_json = json.loads(all_data)

    data = {
        'parse_json':parse_json,

    }

    return Response(data)
