from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    # Individual product page
    path('product/<slug:slug>/', views.product_info, name='product-info'),

    # List of products in a category
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),

    ]
