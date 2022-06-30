from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # App urls
    path('', include('App.urls')),

    # Path to Login/Logout
    path('inbox/', include('django.contrib.auth.urls')),

    # Django JET URLS
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard', include('jet.dashboard.urls', 'jet-dashboard')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)