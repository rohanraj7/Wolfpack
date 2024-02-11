from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns=[
    path('',views.getRoutes),
    path('token/', views.MyTokenObtainPairview.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/',views.sign_up,name='signup'),
]