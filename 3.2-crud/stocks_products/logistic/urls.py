from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)  # ???
router.register('stocks', StockViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('api/v1/products/', 'api/v1/stocks/'),
#     path('api/v1/products/', 'api/v1/stocks/')
# ] + router.urls




# /api/v1/stocks/