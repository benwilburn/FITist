from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from user_profiles.forms import UserForm
from django.contrib.auth.models import User
from user_profiles.models import create_user_profile
from workout_programs.models import get_program_instance
from workout_programs.models import ExerciseBlock
from workout_programs.models import ExerciseGroup
from workout_programs.models import Workout


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
    if curr_user == user:
        return render(
            request,
            'user_profiles/profile_detail.html',
            {'user': user}
        )
    else:
        return redirect('profiles:user_profile', username=curr_user.username)


@login_required(login_url='/user_profiles/login/')
def view_program(request, username=None):
    curr_user = request.user
    if not username:
        return redirect('profiles:user_profile', username=curr_user.username)
    user = get_object_or_404(User, username=username)
    workouts = Workout.objects.filter(program=user.profile.program_selected)
    exercise_groups = list()
    exercise_blocks = list()
    all_groups = ExerciseGroup.objects.all()
    all_blocks = ExerciseBlock.objects.all()
    for group in all_groups:
        if group.workout_in.program == user.profile.program_selected:
            exercise_groups.append(group)
    for block in all_blocks:
        if block.assigned_group in exercise_groups:
            exercise_blocks.append(block)
    print('WORKOUTS', workouts)
    print('EXERCISE_GROUPS', exercise_groups)
    print('EXERCISE_BLOCKS', exercise_blocks)
    if curr_user == user:
        return render(
            request,
            'user_profiles/program.html',
            {
                'program': user.profile.program_selected,
                'workouts': workouts,
                'exercise_groups': exercise_groups,
                'exercise_blocks': exercise_blocks
            }
        )
    else:
        return redirect('profiles:user_profile', username=curr_user.username)
