
def links(request):
    from .models import Link
    from .views import init_links
    # links = init_links(request.resolver_match.url_name)
    links = Link.objects.all()
    return {'links': links}
