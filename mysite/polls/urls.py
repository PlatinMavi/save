from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("Question.id/", views.DetailView.as_view(), name="details"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("<int:question_id>/results/", views.ResultsView.as_view(), name="results"),
] 