from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.urls import reverse
from authentication.models import Profile
from django.utils.text import slugify
from binary_plan.models import BinaryWallet
from shortuuid.django_fields import ShortUUIDField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    short_description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

class Product(models.Model):
    # product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        ("Price"),
        decimal_places=2,
        max_digits=12,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to="product_images/ecommerce/", blank=True, null=True
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    shop_name = models.ForeignKey("Shop", on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=100, null=True)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="", null=True, blank=True, unique=True)
    likes = models.IntegerField(default=0)
    business_volume = models.FloatField(default=0)

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ecommerce:product", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("ecommerce:add-to-cart", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("ecommerce:remove-from-cart", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # if shop is instance of Shop
        if not self.slug and isinstance(self.shop_name, Shop):
            self.slug = slugify(self.name + " " + self.shop_name.shop)

        super().save(*args, **kwargs)


class Customer(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    email_address = models.EmailField(blank=False, null=False, default='hhhdsfha@chikna.com')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    landmark = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.pk}-{self.user.first_name}"

class Order(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    )
    order_id = ShortUUIDField(length=10, max_length=20, prefix="#", alphabet="aBcDeFg1234", primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="OrderItem")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.customer}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.price * self.quantity


class Shop(models.Model):
    shop = models.CharField(max_length=100)
    address = models.TextField()
    items = models.ManyToManyField("Product", blank=True)

    def __str__(self):
        return self.shop


class Cart(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="CartItem")

    def __str__(self):
        return f"Cart for {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in cart for {self.cart.user}"


class BusinessVolumeLog(models.Model):
    transaction_id = models.CharField(max_length=100, primary_key=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="business_volume_log"
    )
    user = models.ForeignKey(
        BinaryWallet, on_delete=models.CASCADE, related_name="business_volume_log"
    )
    business_volume = models.FloatField(default=0)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_time = models.DateTimeField(auto_now=True)
    tag = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user.user.user_id}#{self.transaction_id}"
