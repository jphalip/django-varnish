from django.db.models.signals import post_save
from django.db.models import get_model

from .manager import manager
from .settings import WATCHED_MODELS


def absolute_url_purge_handler(sender, **kwargs):
    gau = getattr(kwargs['instance'], 'get_absolute_url', False)

    if gau:
        manager.run('ban.url', r'^%s.*' % gau())


for model in WATCHED_MODELS:
    post_save.connect(absolute_url_purge_handler, sender=get_model(*model.split('.')))
