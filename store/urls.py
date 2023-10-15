from django.urls import path 
from store.views import Store, Orderconfirmation, OrderPaymentConfirmation, StoreLanding
from store import views
app_name = 'store'
urlpatterns = [
    path("", StoreLanding.as_view(), name='store'),
    path("store-products/", Store.as_view(), name="store-products"),
    path("search/", views.search, name="search"),
    path('order-confirmation/<int:pk>', Orderconfirmation.as_view(), name="order-confirmation"),
    path('payment-confrimation/', OrderPaymentConfirmation.as_view(), name="payment-submitted" ),
]
