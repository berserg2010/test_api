from django.db import models


class CounterMixin(models.Model):
    """CounterMixin.

    """
    counter = models.PositiveIntegerField(default=0, blank=True, verbose_name='counter')

    class Meta:
        abstract = True


class TitleMixin(models.Model):
    """TitleMixin.

    """
    title = models.CharField(max_length=200, verbose_name='title')

    def __str__(self):
        return f'{self.title[:50]}...' if len(self.title) > 50 else self.title

    class Meta:
        abstract = True


class PageManyToManyMixin(models.Model):
    """PageManyToManyMixin.

    """
    pages = models.ManyToManyField('Page', related_name='%(class)s_related', verbose_name='pages')

    class Meta:
        abstract = True


class CommonFieldsMixin(TitleMixin, PageManyToManyMixin, CounterMixin):
    """CommonFieldsMixin.

    """

    class Meta:
        abstract = True
