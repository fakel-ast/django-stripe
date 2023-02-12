from django.urls import path

from stripe_app import views

urlpatterns = [
    path('buy/<int:id>/', views.ItemBuy.as_view(), name='item-buy'),
    path('item/<int:id>/', views.ItemDetail.as_view(), name='item-detail'),
    path('success/', views.SuccessBuy.as_view(), name='item-success-buy'),
]
