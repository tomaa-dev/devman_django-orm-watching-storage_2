from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.visit_information import get_duration, format_duration, is_visit_long
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    visits = Visit.objects.all()
    non_leaved_at = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []

    for visit in non_leaved_at:
        duration = get_duration(visit)
        duration = format_duration(duration)
        suspection = is_visit_long(visit)

        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': duration,
            'is_strange': suspection
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)