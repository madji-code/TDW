from django.urls import path
from django.contrib import admin
from .views import (
    home,
    view_products,
    view_this_product,
    cart,
    add_to_cart,
    add_to_cart_success,
    CreateCheckoutSessionView,
    SuccessView,
    CancelView,
    ProductLandingPageView
)

app_name='sale_point'

urlpatterns = [
    path('', home, name="home"),
    path('boutique', view_products, name="view-products"),
    path('view-this-product/<int:id>', view_this_product, name="view-this-product"),
    path('cart/', cart, name="cart"),
    path('add-to-cart/<int:product_id>', add_to_cart, name="add-to-cart"),
    path('add-to-cart-success/<int:product_id>', add_to_cart_success, name="add-to-cart-success"),
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('landing', ProductLandingPageView.as_view(), name='landing'),
]
