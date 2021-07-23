from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path("admin/", admin.site.urls),
               path('user/', include('store.urls.user_urls')),
               path('products/', include('store.urls.products_urls')),
               path('orders/', include('store.urls.orders_urls')),
               ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
