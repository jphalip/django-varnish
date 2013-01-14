from django.http import HttpResponseRedirect
from manager import manager
from django.views.generic.simple import direct_to_template
from .settings import MANAGEMENT_ADDRS


def get_stats():
    stats = [x[0] for x in manager.run('stats')]
    return zip(MANAGEMENT_ADDRS, stats)


def management(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/admin/')
    if 'command' in request.REQUEST:
        kwargs = dict(request.REQUEST.items())
        manager.run(*str(kwargs.pop('command')).split(), **kwargs)
        return HttpResponseRedirect(request.path)
    try:
        stats = get_stats()
        errors = {}
    except (Exception, ), e:
        stats = None
        errors = {
            "stats": "Error accessing the stats : %s" % str(e)
        }

    extra_context = {
        'stats': stats,
        'errors': errors
    }

    return direct_to_template(request, template='varnish/report.html',
                              extra_context=extra_context)
