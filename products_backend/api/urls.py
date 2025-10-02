from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import health, ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('health/', health, name='Health'),
    path('', include(router.urls)),
]
