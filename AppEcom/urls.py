from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    #Path Admin
    path('admin/', admin.site.urls),
    #Path base
    path('', include('base.urls')),
    #Path Store
    path('', include('store.urls')),
     #Path Cart
    path('', include('cart.urls')),
    # Path Accounts
    path('', include('accounts.urls')),
    
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)