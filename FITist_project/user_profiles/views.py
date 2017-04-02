from django.shortcuts import render
from django.shortcuts import redirect
# from django.shortcuts import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from user_profiles.forms import UserForm
from django.contrib.auth.models import User
from user_profiles.models import Profile
from workout_programs.models import Program


# Create your views here.
def create_new_user(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user_password = new_user.password
            new_user.set_password(new_user.password)
            new_user.save()
            program = get_object_or_404(Program,
                                        pk=request.session["program_pk"]
                                        )
            Profile.objects.create(
                user=new_user,
                program_selected=program
            )
            # might not be needed but added authentication in here as well
            authenticated_user = authenticate(
                                    username=new_user.username,
                                    password=new_user_password
                                )
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect(
                    'profiles:user_profile',
                    permanent=True,
                    username=new_user.username
                )
            else:
                return redirect('profiles:new_user')
    return render(
        request,
        'user_profiles/registration.html',
        {'user_form': form}
    )


@login_required(login_url='/user_profiles/login/')
def get_profile(request, username=None):
    if username is None:
        return redirect(
            'profiles:user_profile',
            permanent=True,
            username=request.user.username,
            )
    user = get_object_or_404(User, username=username)
    if request.user == user:
        return render(
            request,
            'user_profiles/profile_detail.html',
            {'user': user}
        )
    else:
        return redirect(
            'profiles:user_profile',
            permanent=True,
            username=request.user.username,
        )
