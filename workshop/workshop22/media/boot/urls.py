from django.urls import path
from . import views

app_name = "boots"

urlpatterns = [
    path("", views.list, name="list"),
]