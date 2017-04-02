from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from user_profiles.views import create_new_user
from user_profiles.views import get_profile
from user_profiles.forms import LoginForm


urlpatterns = [
    url(r'^login/$',
        login,
        {
            'template_name': 'user_profiles/login.html',
            'authentication_form': LoginForm
        },
        name='login'
        ),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^registration/$', create_new_user, name='new_user'),
    # The following url makes both param & slash optional (due to ?(s))
    url(r'^(?P<username>\w+)?/?$',
        get_profile,
        name='user_profile'),
]
