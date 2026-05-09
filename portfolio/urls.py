from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('__reload__/', include('django_browser_reload.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    prefix_default_language=False,
)
