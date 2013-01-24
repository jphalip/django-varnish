from atexit import register
from varnish import VarnishManager

from .settings import MANAGEMENT_ADDRS, SECRET


class DjangoVarnishManager(VarnishManager):
    """
    A subclass that sends the secret on every run.
    """
    def run(self, *commands, **kwargs):
        kwargs.setdefault('secret', SECRET)
        return super(DjangoVarnishManager, self).run(*commands, **kwargs)


manager = DjangoVarnishManager(MANAGEMENT_ADDRS)
register(manager.close)
