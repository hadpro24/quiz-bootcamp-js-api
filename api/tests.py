from django.test import TestCase

from .models import Quiz, Choice

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.

class ModelsTestCase(TestCase):

    def setUp(self):
        q1 = Quiz.objects.create(title='Quiz 1', answer='Quiz 1')
        q2 = Quiz.objects.create(title='Quiz 2', answer='Quiz 2')

        c1 = Choice.objects.create(question=q1, value='What is QUESTION 1')
        c2 = Choice.objects.create(question=q2, value='What is QUESTION 2')

    def test_quiz_count(self):
        self.qs  = Quiz.objects.all().count()
        self.assertEquals(self.qs, 2)

    def test_choices_count(self):
        self.choices  = Choice.objects.all().count()
        self.assertEquals(self.choices, 2)

    def test_delete_model_choices(self):
        Choice.objects.get(pk=1).delete()
        self.choices  = Choice.objects.all().count()
        self.assertEquals(self.choices, 1)

    def test_delete_model_quizs(self):
        Quiz.objects.get(pk=1).delete()
        self.quizs  = Quiz.objects.all().count()
        self.assertEquals(self.quizs, 1)

    def test_edit_model_choices(self):
        q = Choice.objects.get(pk=2)
        q.value = 'Value Test'
        q.save()
        self.choices  = Choice.objects.get(pk=2)
        self.assertEquals(self.choices.value, 'Value Test')
    def test_edit_model_quiz(self):
        q = Quiz.objects.get(pk=2)
        q.title = 'Value Test'
        q.save()
        quiz  = Quiz.objects.get(pk=2)
        self.assertEquals(quiz.title, 'Value Test')


class ListQuizTest(APITestCase):
    def test_list_quiz(self):
        url = reverse('path-list-quiz')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
