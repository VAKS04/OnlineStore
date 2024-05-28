from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "form"
urlpatterns = [
    path('register/',views.register,name="register"),
    path('auth/',views.LoginUser.as_view(),name="auth"),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/',views.profile,name="profile")
]