from django.urls import path
from people import views

app_name = "people"

urlpatterns = [
    path("list_people/", views.list_people, name="list_people"),
]
