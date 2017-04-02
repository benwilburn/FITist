"""Main project views."""
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from workout_programs.models import Program


def landing_page(request):
    """View for the page everyone visits first."""
    return render(request, 'landing.html')


def grab_program_that_matches_criteria(request):
    """Query the database for the answers to screening.

    This query should only grab one program.
    """
    form_data = request.POST
    available_equipment = form_data.getlist('equipment_available')
    selected_program = Program.objects.filter(
        tags__text=form_data['gender']
    ).filter(
        tags__text=form_data['goal']
    ).filter(
        tags__text=form_data['experience']
    ).filter(
        tags__text=form_data['length']
    ).filter(
        tags__text=form_data['per_week']
    ).filter(
        tags__text__in=available_equipment
    ).first()
    if selected_program is None:
        return render(request,
                      'workout.html',
                      {
                        'selected_program': {
                            'name': None,
                            'total_weeks': None,
                            'tags': [],
                            'completed': None
                        }
                      })
    else:
        request.session['program_pk'] = selected_program.pk
        print('CURRENT USER', request.user)
        if request.user.is_anonymous():
            print("THERE IS NO USER!!!!!!")
            return redirect(reverse('profiles:new_user'))
        else:
            print("YOU ARE THE ONLY USER!!!!!!!")
            return render(request,
                          'workout.html',
                          {'selected_program': selected_program}
                          )
