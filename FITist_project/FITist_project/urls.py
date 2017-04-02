"""FITist_project URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from FITist_project import views

urlpatterns = [
    url(r'^screening/', include('questions.urls', namespace='questions')),
    url(r'^user_profiles/',
        include('user_profiles.urls',
                namespace='profiles')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.landing_page, name='landing'),
    url(r'^grab_workout/',
        views.grab_program_that_matches_criteria, name='get_program')
]
