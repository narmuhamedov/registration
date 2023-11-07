from .models import Link


def get_original_url(short_url):
    try:
        link = Link.objects.get(short_url=short_url)
        return link.original_url
    except Link.DoesNotExist:
        return None
