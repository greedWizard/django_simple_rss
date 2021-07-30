from django.urls import path
from .views import RSSFeedItemDetailView, RSSFeedItemListView, RSSFeedItemListView

urlpatterns = [
    path('', RSSFeedItemListView.as_view(), name='home'),
    path('articles/<pk>', RSSFeedItemDetailView.as_view(), name='feed-item-detail')
]