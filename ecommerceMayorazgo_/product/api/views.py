from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from product.models import Products, Categories
from product.api.serializers import ProductSerializer, CategorySerializer
""""
class ProductsList(views.APIView):
    try:
        def get(self, request):
            products = Products.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        def post(self, request):
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(str(e))
"""

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=False)
    def get_products_by_category(self, request):
        category = self.request.query_params.get('category')
        products = Products.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    