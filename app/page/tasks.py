from celery import shared_task
from django.db.models import F

from page.models import Page


@shared_task
def increase_counter(page_id: int or str):
    page = Page.objects.get(pk=page_id)
    for reladed in dir(page):
        if reladed.endswith('_related'):
            try:
                getattr(page, reladed).all().update(counter=F('counter') + 1)
            except Exception as e:
                print(e)
