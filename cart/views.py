from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart, CartProduct


@login_required
def add_to_cart_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_product.quantity += 1
        cart_product.save()
    return redirect('cart_detail')


@login_required
def cart_detail_view(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_products = cart.cartproduct_set.all()
    cart_total = 0
    for cart_product in cart_products:
        pr = cart_product.product.price * cart_product.quantity
        cart_total += pr
        cart_product.product.total_price = pr
    context = {
        'cart': cart,
        'cart_products': cart_products,
        'cart_total': str(cart_total)
    }
    return render(request, 'cart/cart_detail.html', context)


def get_cart_data(user):
    cart_products = CartProduct.objects.filter(cart__user=user)
    cart_total = 0
    for cart_product in cart_products:
        cart_total += cart_product.product.price * cart_product.quantity
    return {
        'cart_products': cart_products,
        'cart_total': cart_total,
    }


@login_required
def delete_cart_product_view(request, cart_product_id):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_product = get_object_or_404(CartProduct, id=cart_product_id, cart=cart)
    if cart_product.quantity > 1:
        cart_product.quantity -= 1
        cart_product.save()
    else:
        cart_product.delete()
    return redirect('cart_detail')
