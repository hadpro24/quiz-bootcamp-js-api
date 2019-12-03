from django.contrib import admin
from .models import Quiz, Choice

from django.contrib.admin.sites import AdminSite

AdminSite.site_header = 'API QUIZES'
AdminSite.site_title = 'QUIZ'
AdminSite.index_title = 'TABLEAU DE BORD'

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Choice)
