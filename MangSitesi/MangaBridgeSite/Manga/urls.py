from xml.etree.ElementInclude import include
from django.urls import path
from . import views

app_name = "manga"

urlpatterns=[
    path("manga/", views.IndexView.as_view(), name='index' ),
    path("manga/<int:pk>/", views.MangaView.as_view(), name="details"),
    path("", views.MainPageView.as_view(), name="mainpage")
]

