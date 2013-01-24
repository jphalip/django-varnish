from atexit import register
from varnish import VarnishManager
from .settings import MANAGEMENT_ADDRS, SECRET


manager = VarnishManager(MANAGEMENT_ADDRS, SECRET)
register(manager.close)
