from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("<int:id>/", views.detail, name="detail"),
]