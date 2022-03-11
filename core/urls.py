from django.urls import path, include
from .views import user_create

urlpatterns = [
    path("api/", include("questions.urls")),
    path("api/users", user_create)
]