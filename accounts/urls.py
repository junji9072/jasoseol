from django.urls import path,include
from .views import signup, MyLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('accounts/',include('allauth.urls')),
]