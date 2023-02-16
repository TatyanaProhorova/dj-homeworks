from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [filters.SearchFilter]     # ??
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации

    def get_queryset(self):
        p = self.request.query_params.get('products')
        if p:
            q = Stock.objects.filter(products__in=p)
            return q
        return Stock.objects.all()

#filter_backends = [DjangoFislterBackend, SearchFilter, OrderingrFilter]
#filterset_fields = ['User',   ]
#search_fields = ['text', ]
#ordering_fields = ['id', 'user',  ]