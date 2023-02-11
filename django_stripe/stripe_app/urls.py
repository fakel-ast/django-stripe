from django.urls import path, re_path

from stripe_app import views

urlpatterns = [
    path('buy/<int:id>/', views.ItemBuy.as_view())
]
