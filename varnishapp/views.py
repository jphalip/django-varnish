from django.http import Http404
from django.core.urlresolvers import NoReverseMatch
from django.shortcuts import render, redirect

from .manager import manager
from .settings import MANAGEMENT_ADDRS


def get_stats():
    stats = [x[0] for x in manager.run('stats')]
    return zip(MANAGEMENT_ADDRS, stats)


def management(request):
    if not request.user.is_superuser:
        try:
            return redirect('admin:index')
        except NoReverseMatch:
            raise Http404

    if 'command' in request.POST:
        kwargs = dict(request.POST.items())
        manager.run(*str(kwargs.pop('command')).split(), **kwargs)
        return redirect(request.path)

    try:
        stats = get_stats()
        errors = {}
    except Exception, e:
        stats = None
        errors = {
            "stats": "Error accessing the stats : %s" % str(e)
        }

    context = {
        'stats': stats,
        'errors': errors
    }
    return render(request, 'varnish/report.html', context)
