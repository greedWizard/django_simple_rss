from typing import Iterable, List
from django.db.models.base import Model
import feedparser
from project.base.services import BaseService
from .models import RSSFeedItem, RSSFeed
from django.db import IntegrityError

import requests
from datetime import datetime
from time import mktime


class RSSFeedService(BaseService):
    model = RSSFeed
    base_query_set = model.objects.all()
    parser_class = feedparser

    def create(self, url) -> Model:
        d = self.parser_class.parse(url)

        if len(d.entries) == 0:
            raise ValueError('Unavaliable url')

        data = {
            'name': d.feed.title,
            'rss_url': url,
        }

        return super().create(**data)


class RSSFeedItemService(BaseService):
    model = RSSFeedItem
    base_query_set = model.objects.order_by('-timestamp')
    parser_module = feedparser
    rss_feed_service = RSSFeedService

    def fetch_new(self) -> List[Model]:
        ''' Write new feeditems to database '''
        feeds = self.rss_feed_service().fetch()

        new_items = []

        if len(feeds) == 0:
            return

        for feed in feeds:
            try:
                d = self.parser_module.parse(feed.rss_url)

                for item in d.entries:
                    image = None
                    title = item.title
                    try:
                        url = item.links[0].href
                    except IndexError as e:
                        continue # на случай если по какой-то причине url отсутсвует

                    if len(self.fetch(url=url).all()) > 0:
                        continue

                    timestamp = datetime.fromtimestamp(mktime(item.published_parsed))

                    if len(item.links) > 1:
                        for link in item.links:
                            if str(link.type).find('image') >= 0:
                                image = link.href
                                break
                    
                    new_items.append(
                        super().create(
                            feed_id=feed.id,
                            timestamp=timestamp,
                            title=title,
                            url=url,
                            thumbnail=image,
                        )
                    )
            except requests.exceptions.RequestException as e:
                raise ValueError(detail=f'{feed.rss_link} - invalid link')
        return new_items