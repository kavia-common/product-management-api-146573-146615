from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import F, Sum
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

    total_balance (custom action):
        Returns the total inventory balance as the sum of (price * quantity) for all products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    # PUBLIC_INTERFACE
    @action(
        detail=False,
        methods=['get'],
        url_path='total_balance',
        permission_classes=[AllowAny]
    )
    def total_balance(self, request):
        """
        Calculate and return the total balance of goods in stock.

        This endpoint computes the sum of (price * quantity) for all Product records
        using a database-level aggregation for efficiency.

        Query params:
            None

        Returns:
            JSON response:
                {
                  "total_balance": "<decimal string>"
                }
        """
        agg = Product.objects.aggregate(
            total=Sum(F('price') * F('quantity'))
        )
        total = agg['total'] or 0
        # Convert to string to preserve decimal precision in JSON
        return Response({"total_balance": str(total)}, status=status.HTTP_200_OK)
