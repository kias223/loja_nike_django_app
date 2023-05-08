from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.adminstration_view, name='adminstration-view'),
    path('new-product/', views.new_product.as_view(), name='new-product'),
    path('excluir_post/<int:id>', views.excluir_post, name = 'excluir_post'),
    path('edit-post/<int:pk>', views.editar_post.as_view(), name = 'editar_post'),
    path('purchase-apiview/', views.purchase_list.as_view(), name = 'purchase_props'),
    path('perfil-update/', views.user_perfil, name = 'perfil_update'),
    path('adminstration-purchases/', views.adminstration_purchases, name = 'adminstration_purchases'),
    path('adminstration-purchases-details/<int:id>', views.adminstration_purchases_details, name = 'adminstration_purchases_details'),
    path('page-admins', views.page_admins,name='page_admins'),
    path('create-admin', views.create_admin,name='create_admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

