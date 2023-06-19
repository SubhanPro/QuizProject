from django.urls import path
from quiz import views

urlpatterns = [
    path("questions/<int:id>/<int:number>/", views.quiz_questions, name = "questions"),
    path("results/<int:topic_id>/", views.results, name = "results")
]