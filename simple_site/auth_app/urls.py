from django.urls import path
from . import views

app_name = "form"
urlpatterns = [
    path('register',views.register,name="register"),
]