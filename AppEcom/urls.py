from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.i18n import set_language

urlpatterns = [
    #Path Admin
    path('admin/', admin.site.urls),
    #Path Store
    path('', include('store.urls')),
    
    
    # Path de Idioma
    path('set-language/', set_language, name='set_language'),  
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)