from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('core.urls')),
    path('accounts/', include('account.urls')),
    path('dashboard/', include('history.urls')),
]
urlpatterns += staticfiles_urlpatterns()
admin.site.index_title = "Bindu"
admin.site.site_header = "Bindu Admin Panel"