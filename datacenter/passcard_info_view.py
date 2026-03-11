from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from datacenter.visit_information import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_information = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    
    for visit in passcard_information:
        duration = get_duration(visit)
        duration = format_duration(duration)
        suspection = is_visit_long(visit) 

        this_passcard_visits.append(
            {
                'entered_at': timezone.localtime(visit.entered_at),
                'duration': duration,
                'is_strange': suspection
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)