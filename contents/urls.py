from django.urls import path
from . import views

app_name = "contents"
urlpatterns = [
    path('', views.index, name="index")
]