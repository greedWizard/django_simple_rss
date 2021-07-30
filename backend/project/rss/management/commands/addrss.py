from django.core.management.base import BaseCommand, CommandError

from rss.services import RSSFeedService

class Command(BaseCommand):
    help = 'Add new RSS feed'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        RSSFeedService().create(
            options['url']
        )