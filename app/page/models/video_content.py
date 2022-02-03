from django.db import models

from page.models.mixins import CommonFieldsMixin


class VideoContent(CommonFieldsMixin):
    """VideoContent Model.

    """
    url = models.URLField(verbose_name='video url')
    subtitles_url = models.URLField(null=True, blank=True, verbose_name='subtitles url')
