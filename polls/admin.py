# Correct way to register models in the admin
from django.contrib import admin
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)