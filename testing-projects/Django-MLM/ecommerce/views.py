from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem, Order, OrderItem, Customer, Shop
from authentication.models import Profile
from django.views import generic
from django.contrib.auth.decorators import login_required
from ecommerce import models
from django.core.paginator import Paginator
from decimal import Decimal
from .forms import CheckoutForm


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "ecommerce/product-detail.html"
    context_object_name = "product"
    slug_url_kwarg = "slug"


def cart_view(request, user_id):
    user = get_object_or_404(Profile, user_id=user_id)
    cart = get_object_or_404(Cart, user=user)
    cart_items = cart.cartitem_set.all()

    context = {"cart": cart, "cart_items": cart_items}
    return render(request, "ecommerce/cart.html", context)


@login_required
def add_to_cart(request, slug):
    user_profile = get_object_or_404(Profile, user_id=request.user.id)
    cart, created = Cart.objects.get_or_create(user=user_profile)
    product = get_object_or_404(Product, slug=slug)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()

    return redirect("cart")


def list_products(request):
    # product list page
    products = models.Product.objects.all()
    print(products.count())
    # pagination
    products = Paginator(products, 4)
    page_number = request.GET.get("page")
    products = products.get_page(page_number)

    iterator = range(
        products.number, min(products.number + 5, products.paginator.num_pages)
    )

    return render(
        request,
        "ecommerce/product_list.html",
        {"products": products, "iterator": iterator},
    )


def search_products(request):
    # search product page
    serch_query = request.GET.get("search", "")
    filtered_products = models.Product.objects.filter(name__icontains=serch_query)

    # pagination
    products = Paginator(filtered_products, 4)
    page_number = request.GET.get("page")
    products = products.get_page(page_number)

    iterator = range(
        products.number, min(products.number + 5, products.paginator.num_pages)
    )

    return render(
        request,
        "ecommerce/product_list.html",
        {"products": products, "iterator": iterator, "search_query": serch_query},
    )


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    print(product)
    # prodtct details page
    return render(request, "ecommerce/product_detail.html", {"product": product})

@login_required
def orders(request):
    # order history page
    user = Profile.objects.get(user_id=request.user.user_id)
    customers = Customer.objects.filter(user=user)
    orders_list = []
    for customer in customers:
        orders_list += Order.objects.filter(customer=customer)
        
    # return render(request, "ecommerce/orders.html")
    return render(request, "ecommerce/orders.html", {'orders': orders_list, 'customer': customers})

@login_required
def checkout(request, pk):
    # checkout page
    if request.method == "GET":
        # returns if user exists
        user = []
        customers = []
        customer_exists = Customer.objects.filter(user=request.user).exists()
        product = get_object_or_404(Product, pk=pk)
        user = get_object_or_404(Profile, user_id=request.user.user_id)

        if customer_exists:  # checking if user exists in Customer
            customers = Customer.objects.filter(user=request.user).first()
            return render(
                request,
                "ecommerce/checkout.html",
                {"user": user, "customers": customers, "product": product},
            )

        else:
            return render(
                request, "ecommerce/checkout.html", {"user": user, "product": product }
            )

    if request.method == "POST":
        product = get_object_or_404(Product, pk=pk)
        price = product.price * Decimal(1)
        user = get_object_or_404(Profile, user_id=request.user.user_id)

        first_name = request.POST.get("first_name", None)
        email = request.POST.get("email", None)
        phone_number = request.POST.get("phone", None)
        country = request.POST.get("address", None)
        zip_code = request.POST.get("zip_code", None)
        landmark = request.POST.get("landmark", None)
        address = request.POST.get("address", None)
        
        if not Customer.objects.filter(phone_number=phone_number).exists() or not Customer.objects.filter(address=address).exists():
            customer = Customer.objects.create(
                user=user,
                name=first_name,
                email_address=email,
                phone_number=phone_number,
                zip_code=zip_code,
                landmark=landmark,
                address=address
            )
        else:
            print('key below printing ')
            print(request.POST.get("key", None))
            customer = Customer.objects.get(pk=request.POST.get("key", None))
        # Create a new Order record
        order = Order.objects.create(customer=customer, status="pending")

        # Create a new OrderItem record associated with the order and selected product
        order_item = OrderItem.objects.create(
            order=order, product=product, quantity=1, price=price
        )

        # Redirect the user to a success page or order summary page
        # You can also pass the order details to the template for displaying the order summary
        return redirect("orders")
