from django.contrib import admin
from questions.models import Answer
from questions.models import Question


class AnswerInline(admin.StackedInline):
    """Extends form under question for answers in admin."""

    model = Answer
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    """Question base form that extends for each inline."""

    inlines = [AnswerInline, ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
