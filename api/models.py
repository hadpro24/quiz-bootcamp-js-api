from django.db import models

# Create your models here.
class Quiz(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='quiz/', null=True, blank=True)
	answer = models.CharField(max_length=100)

	def __str__(self):
		return self.title


class Choice(models.Model):
	question = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='choices')
	value = models.CharField(max_length=100)

	def __str__(self):
		return self.value

