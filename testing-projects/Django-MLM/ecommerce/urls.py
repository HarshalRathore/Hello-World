from django.urls import path
import ecommerce.views as views

urlpatterns = [
    # path('products/', view=views.ProductView.as_view(), name='ecommerce-products'),
    path('product/detail/<slug:slug>/', view=views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/<slug:user_id>', view=views.cart_view, name='cart'),
    path('cart/add-to-cart/<slug>', view=views.add_to_cart, name='add-to-cart'),
    path('products/', views.list_products, name='ecommerce-products'),
    path('search-products/', views.search_products, name='search-products'),
    path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path('orders/', views.orders, name='orders'),
    path('checkout/<int:pk>', views.checkout, name='checkout'),
]
