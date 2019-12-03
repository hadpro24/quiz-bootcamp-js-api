from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Quiz
from .serializers import QuizSerializer

# Create your views here.
class ListQuiz(APIView):
	def get(self, request):
		all_quiz = Quiz.objects.all()
		data = QuizSerializer(all_quiz, many=True).data
		return Response({'quiz': data})
		