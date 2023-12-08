from django.urls import path

from topic import views
from topic.views import index


urlpatterns = [
    path("", index, name="index"),
]

app_name = "topic"
