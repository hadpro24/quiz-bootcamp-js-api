from rest_framework import serializers

from .models import Quiz, Choice

class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = ('id', 'value')

class QuizSerializer(serializers.ModelSerializer):
	choices = ChoiceSerializer(many=True, read_only=True)
	class Meta:
		model = Quiz
		fields = ('id', 'title', 'image', 'answer', 'choices')


