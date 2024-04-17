from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'order-items', views.OrderItemViewSet)
router.register(r'carts', views.CartViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'categorys', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
