"""Setting up the main view for the app question/answer."""
# from django.shortcuts import render
from django.views.generic import ListView
from .models import Question


class QuestionListView(ListView):
    """Sets up view for questions page."""

    model = Question
    context_object_name = "questions"
    template_name = 'questions/questions_list.html'
