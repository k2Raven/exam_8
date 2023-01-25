from django.urls import path

from webapp.views import IndexView, DetailProductView, CreateProductView, UpdateProductView, DeleteProductView, \
    CreateReviewView, UpdateReviewView, DeleteReviewView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', DetailProductView.as_view(), name="product_detail"),
    path('product/add/', CreateProductView.as_view(), name="product_create"),
    path('product/<int:pk>/update/', UpdateProductView.as_view(), name="product_update"),
    path('product/<int:pk>/delete/', DeleteProductView.as_view(), name="product_delete"),
    path('product/<int:pk>/review_add/', CreateReviewView.as_view(), name="review_create"),
    path('review/<int:pk>/update/', UpdateReviewView.as_view(), name="review_update"),
    path('review/<int:pk>/delete/', DeleteReviewView.as_view(), name="review_delete")
]
