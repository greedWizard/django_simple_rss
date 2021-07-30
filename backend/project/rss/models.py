from django.db import models


class RSSFeed(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
    )
    rss_url = models.TextField(unique=True)

    def __repr__(self) -> str:
        return f'<Feed {self.name}>'


class RSSFeedItem(models.Model):
    feed = models.ForeignKey('RSSFeed', related_name='items', on_delete=models.CASCADE)

    timestamp = models.DateTimeField()
    title = models.TextField()
    url = models.URLField(unique=True)
    thumbnail = models.URLField(null=True, blank=True)

    def __repr__(self) -> str:
        return f'<FeedItem "{self.title[:50]}">'
