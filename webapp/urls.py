from django.urls import path

from webapp.views import IndexView, DetailProductView, CreateProductView, UpdateProductView, DeleteProductView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', DetailProductView.as_view(), name="product_detail"),
    path('product/add/', CreateProductView.as_view(), name="product_create"),
    path('product/<int:pk>/update/', UpdateProductView.as_view(), name="product_update"),
    path('product/<int:pk>/delete/', DeleteProductView.as_view(), name="product_delete")
]
