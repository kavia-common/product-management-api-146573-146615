from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def health(request):
    """Simple health check endpoint."""
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet providing CRUD operations for products.

    list:
        Retrieve a paginated list of products. Supports search by name using `?search=<term>`.

    retrieve:
        Retrieve a product by its ID.

    create:
        Create a new product by providing name, price, and quantity.

    update:
        Replace an existing product.

    partial_update:
        Partially update fields for an existing product.

    destroy:
        Delete a product by its ID.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
