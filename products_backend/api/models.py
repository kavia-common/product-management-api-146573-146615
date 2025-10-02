from django.db import models


class TimeStampedModel(models.Model):
    """Abstract base class with created/updated timestamps."""
    created_at = models.DateTimeField(auto_now_add=True, help_text="Record creation timestamp")
    updated_at = models.DateTimeField(auto_now=True, help_text="Record last update timestamp")

    class Meta:
        abstract = True


class Product(TimeStampedModel):
    """Product represents a sellable item with price and stock quantity."""
    name = models.CharField(max_length=255, db_index=True, help_text="Product name")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Product price")
    quantity = models.PositiveIntegerField(default=0, help_text="Available stock quantity")

    def __str__(self) -> str:
        return f"{self.name} (${self.price})"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Product"
        verbose_name_plural = "Products"
