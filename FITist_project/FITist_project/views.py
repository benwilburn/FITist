"""Main project views."""
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from workout_programs.models import Program


def landing_page(request):
    """View for the page everyone visits first."""
    return render(request, 'landing.html')


@require_POST
def grab_program_that_matches_criteria(request):
    """Query the database for the answers to screening.

    This query should only grab one program.
    """
    current_user = request.user
    form_data = request.POST
    # Added all items I wanted to filter selected_program by.
    all_tags_to_filter = [
        form_data['gender'],
        form_data['goal'],
        form_data['experience'],
        form_data['length'],
        form_data['per_week']
    ]
    # Grab the list from the screening form.
    available_equipment = form_data.getlist('equipment_available')
    # Loop through list of equipment and append it to all_tags_to_filter list.
    for equipment in available_equipment:
        all_tags_to_filter.append(equipment)
    # Adding a count field to all Programs; equals the number of tags it has.
    # then filter each program by the first item in all_tags_to_filter list.
    selected_program = Program.objects.annotate(
        count=Count('tags')
    ).filter(
        tags__text=available_equipment[0]
    )
    # loop through remaining items in all_tags_to_filter and add corresponding
    # filter.
    for equipment in available_equipment[1:]:
        selected_program = selected_program.filter(tags__text=equipment)
    # filter remaining programs for count value by len of all_tags_to_filter.
    # add filter for each remaining screening question (gender/goal/etc).
    selected_program = selected_program.filter(
        count=len(all_tags_to_filter)
    ).filter(
        tags__text=form_data['gender']
    ).filter(
        tags__text=form_data['goal']
    ).filter(
        tags__text=form_data['experience']
    ).filter(
        tags__text=form_data['length']
    ).filter(
        tags__text=form_data['per_week']
    ).first()
    print('selected_program', selected_program)
    if not selected_program:
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
        if current_user.is_anonymous():
            return redirect(reverse('profiles:new_user'))
        else:
            current_user.profile.program_selected = selected_program
            current_user.profile.save()
            return redirect(reverse('profiles:user_profile'))
