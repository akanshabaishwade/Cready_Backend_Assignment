from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from .api import *


urlpatterns = [
    # After register call (api/token/) to get token
    path('register/', RegisterApi.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('movies/', GetAllMovie, name='GetAllMovie'),
    path('request-count/', session_hit_counter, name='GetAllMovie'),
]