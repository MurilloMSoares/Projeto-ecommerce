from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import acesso_view


urlpatterns = [
    path('admin/', admin.site.urls),

    # A tela de acesso deve ser a primeira página do site.
    path('', acesso_view, name='acesso'),

    # A loja fica em /loja/.
    path('loja/', include('products.urls')),

    path('carrinho/', include('cart.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
