from django.urls import path
from product.api.views import CategoryViewSet, ProductsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductsViewSet, basename='product')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = router.urls
    #path('product/', views.ProductsList.as_view(), name='product_list'),


