from django.contrib import admin
from questions.models import Answer
from questions.models import Question

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
