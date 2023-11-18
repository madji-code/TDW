from django.urls import path
from django.contrib import admin
from .views import (
    home,
    view_products,
    view_this_product,
)
from .cart import (
    cart,
    add_to_cart,
    add_to_cart_success,
    delete_from_cart,
)
from .checkout import (
    CreateCheckoutSessionView,
    SuccessView,
    CancelView,
    ProductLandingPageView,
    stripe_webhook
)

app_name='sale_point'

urlpatterns = [
    path('', home, name="home"),
    path('boutique', view_products, name="view-products"),
    path('view-this-product/<int:id>', view_this_product, name="view-this-product"),

    path('cart/', cart, name="cart"),
    path('delete-from-cart/<int:item_id>', delete_from_cart, name="delete-from-cart"),
    path('add-to-cart/<int:product_id>', add_to_cart, name="add-to-cart"),
    path('add-to-cart-success/<int:product_id>', add_to_cart_success, name="add-to-cart-success"),

    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('landing/', ProductLandingPageView.as_view(), name='landing'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhooks'),
]
