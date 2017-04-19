from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from user_profiles.forms import UserForm
from django.contrib.auth.models import User
from user_profiles.models import create_user_profile
from workout_programs.models import get_program_instance


def create_new_user(request):
    session = request.session
    form = UserForm()
    if request.method == "POST":
        user = UserForm(request.POST)
        if user.is_valid():
            program = get_program_instance(program_pk=session["program_pk"])
            user = user.save()
            create_user_profile(user=user, program=program)
            login(request, user)
            return redirect(
                'profiles:user_profile',
                username=user.username
            )
    return render(
        request,
        'user_profiles/registration.html',
        {'user_form': form}
    )


@login_required(login_url='/user_profiles/login/')
def get_profile(request, username=None):
    curr_user = request.user
    if not username:
        return redirect('profiles:user_profile', username=curr_user.username)
    user = get_object_or_404(User, username=username)
    if request.user == user:
        return render(
            request,
            'user_profiles/profile_detail.html',
            {'user': user}
        )
    else:
        return redirect('profiles:user_profile', username=curr_user.username)
