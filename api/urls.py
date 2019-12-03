from django.urls import path

from . import views

urlpatterns = [
	path('quiz', views.ListQuiz.as_view(), name='path-list-quiz'),
]
