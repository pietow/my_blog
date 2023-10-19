from django.core.management.base import BaseCommand
from django.urls import get_resolver

class Command(BaseCommand):
    help = 'Displays all of the URL patterns defined in your project.'

    def handle(self, *args, **kwargs):
        urlconf = get_resolver(None).url_patterns
        self.show_urls(urlconf)

    def show_urls(self, urlpatterns, prefix=''):
        for entry in urlpatterns:
            if hasattr(entry, 'url_patterns'):
                self.show_urls(entry.url_patterns, prefix + entry.pattern.regex.pattern)
            else:
                if not 'admin' in prefix:
                    full_url = prefix + entry.pattern.regex.pattern
                    self.stdout.write(f"{full_url}")

