from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('product/<int:id>', views.product, name='product'),
    path('user-purchase/', views.user_purchase, name='user_purchase'),
    path('purchase/', views.purchase, name='purchase'),
    # path('cancel-user-purchase/<int:id>', views.cancel_user_purchase, name = 'cancel_user_purchase'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
