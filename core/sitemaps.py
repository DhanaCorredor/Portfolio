from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    """Sitemap for the portfolio's static, public pages.

    No Sites framework: the sitemap view falls back to RequestSite, so the
    absolute URLs use the actual request host (works on any Vercel domain).
    """

    protocol = 'https'
    changefreq = 'monthly'

    def items(self):
        return ['core:index', 'core:cv_marketing']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return 1.0 if item == 'core:index' else 0.7
