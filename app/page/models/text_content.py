from django.db import models

from page.models.mixins import CommonFieldsMixin


class TextContent(CommonFieldsMixin):
    """TextContent Model.

    """
    text = models.TextField(verbose_name='text')
