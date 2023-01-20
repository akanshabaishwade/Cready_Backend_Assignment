from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import BasicAuthentication
from .serializer import RegisterSerializer, UserSerializer
from requests.adapters import HTTPAdapter, Retry
from rest_framework.response import Response
from rest_framework import generics
import requests
import json


# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


@authentication_classes([BasicAuthentication])
@api_view(('GET',))
def GetAllMovie(request):
    hit = request.session.get('hit')

    s = requests.Session()
    retries = Retry(total=5, backoff_factor=1,
                    status_forcelist=[502, 503, 504])
    s.mount('http://', HTTPAdapter(max_retries=retries))
    if not hit:
        request.session['hit'] = 1
    else:
        request.session['hit'] += 1

    # response_API = requests.get('https://demo.credy.in/api/v1/maya/movies/')
    response_API = s.get('https://demo.credy.in/api/v1/maya/movies/')

    all_data = response_API.text
    parse_json = json.loads(all_data)

    data = {
        'hit': hit,
        'parse_json': parse_json,

    }
    return Response(data)


@api_view(('GET',))
def session_hit_counter(request):
    hit = request.session.get('hit')
    if not hit:
        request.session['hit'] = 1
    else:
        request.session['hit'] += 1

    data = {
        'hit': hit,

    }

    return Response(data)
