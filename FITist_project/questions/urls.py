"""Urls for inital questions customers will have to answer."""
from django.conf.urls import url

from questions.views import QuestionListView

urlpatterns = [
    url(r'^$', QuestionListView.as_view(), name='list'),
]
