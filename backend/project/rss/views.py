from typing import Any, Dict
from django.views.generic import ListView, DetailView
from .models import RSSFeedItem
from .services import RSSFeedItemService


class RSSFeedItemListView(ListView):
    template_name = 'feed.html'
    context_object_name = 'news'
    service = RSSFeedItemService

    def get_queryset(self):
        return self.service().fetch()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        self.service().fetch_new()
        context['news'] = self.service().fetch()

        return context


class RSSFeedItemDetailView(DetailView):
    template_name = 'detail.html'
    context_object_name = 'item'
    service = RSSFeedItemService

    def get_queryset(self):
        return self.service().fetch()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['item'] = self.service().read(self.kwargs.get('pk'))

        return context
