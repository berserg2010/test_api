from django.db import models

from page.models.mixins import CommonFieldsMixin


class AudioContent(CommonFieldsMixin):
    """AudioContent Model.

    """
    bitrate = models.PositiveIntegerField(null=True, blank=True, verbose_name='bitrate, bps')
