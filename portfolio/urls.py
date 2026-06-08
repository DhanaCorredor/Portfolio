from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from core import views as core_views
from core.sitemaps import StaticViewSitemap

sitemaps = {'static': StaticViewSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('__reload__/', include('django_browser_reload.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', core_views.robots_txt, name='robots'),
]

urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    prefix_default_language=False,
)
