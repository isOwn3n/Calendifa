from django.urls import path
from . import views


urlpatterns = [
    path("now/", views.NowView.as_view(), name="Now"),
    path("now/persian/", views.NowPersianDigitView.as_view(), name="NowPersianDigit"),
]
