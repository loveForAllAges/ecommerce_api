from django.urls import path

from .views import ItemDetailView, BuyView, success, OrderView, OrderBuyView


urlpatterns = [
    path('item/<int:pk>', ItemDetailView.as_view(), name='item_detail'),
    path('buy/<int:pk>', BuyView.as_view(), name='buy'),
    path('order/<int:pk>', OrderView.as_view(), name='order_view'),
    path('order/buy/<int:pk>', OrderBuyView.as_view(), name='order_buy'),
    path('success', success, name='success'),
]
