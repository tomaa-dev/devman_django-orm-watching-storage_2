from django.utils import timezone


SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600


def get_duration(visit):
    if visit.leaved_at:
        duration = visit.leaved_at - visit.entered_at
    else:
        duration = timezone.now() - visit.entered_at
    return duration


def format_duration(delta):
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // SECONDS_IN_HOUR
    minutes = (total_seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    seconds = total_seconds % SECONDS_IN_MINUTE
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def is_visit_long(visit, minutes=SECONDS_IN_MINUTE):
    duration = get_duration(visit)
    duration_minutes = duration.total_seconds() / SECONDS_IN_MINUTE
    return duration_minutes > minutes