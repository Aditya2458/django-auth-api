from django.urls import path
from .views import hello, logout_user

urlpatterns = [
    path('', hello),
]
from django.urls import path
from .views import hello, CustomAuthToken, protected_view

urlpatterns = [
    path('', hello),
    path('login/', CustomAuthToken.as_view(), name='api_login'),
    path('protected/', protected_view, name='protected'),
]
from django.urls import path
from accounts.views import hello, CustomAuthToken, protected_view, register_user

urlpatterns = [
    path('hello/', hello),
    path('login/', CustomAuthToken.as_view(), name='api_login'),
    path('protected/', protected_view, name='protected'),
    path('register/', register_user, name='register_user'),
    path('logout/', logout_user, name='logout_user'),

    
]
