from django.urls import path

from kitchen import views

urlpatterns = [
    path("", views.index, name="index"),
]

app_name = "kitchen"