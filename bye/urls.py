from django.urls import path
from bye import views

app_name="bye"

urlpatterns=[
    path("hello/",views.hello,name="hello"),
]