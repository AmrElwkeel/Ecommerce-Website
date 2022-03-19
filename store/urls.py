from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import store,StoreApi,api_view,cart,checkout

urlpatterns = [
    path('', store, name="store"),
    path('cart/', cart, name="cart"),
    path('product/api', StoreApi, name="product/api"),
    path('checkout/', checkout, name="checkout"),
]
if settings.DEBUG:

    if settings.DEBUG:
        urlpatterns += (
         static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        )
