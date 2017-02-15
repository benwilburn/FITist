from django.contrib import admin
from questions.models import Answer
from questions.models import Question

admin.site.register(Question)
admin.site.register(Answer)
