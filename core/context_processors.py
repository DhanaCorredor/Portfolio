from django.conf import settings


def site_globals(request):
    """Expose a few public site settings to every template."""
    return {
        'GA4_MEASUREMENT_ID': settings.GA4_MEASUREMENT_ID,
    }
