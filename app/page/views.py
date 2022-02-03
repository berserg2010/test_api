from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Page
from .serializer import PageSerializer, PageDetailSerializer
from .tasks import increase_counter


class PageViewSet(ReadOnlyModelViewSet):
    """Pages API.

    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = []

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PageDetailSerializer
        return PageSerializer

    def retrieve(self, request, *args, **kwargs):
        page_id = kwargs.get('pk')
        increase_counter(page_id)
        return super().retrieve(request, *args, **kwargs)
