from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Like, LikeProduct


@login_required
def add_to_like_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    like, created = Like.objects.get_or_create(user=user)
    like_product, created = LikeProduct.objects.get_or_create(like=like, product=product)
    if not created:
        like_product.quantity += 1
        like_product.save()
    return redirect('like_detail')


@login_required
def like_detail_view(request):
    user = request.user
    like = Like.objects.get(user=user)
    like_products = like.cartproduct_set.all()
    context = {
        'like': like,
        'like_products': like_products,
        'like_total': len(like_products)
    }
    return render(request, 'like/like_detail.html', context)


def get_like_data(user):
    like_products = LikeProduct.objects.filter(cart__user=user)
    return {
        'like_total': len(like_products),
    }


@login_required
def delete_like_product_view(request, like_product_id):
    user = request.user
    like = Like.objects.get(user=user)
    like_product = get_object_or_404(LikeProduct, id=like_product_id, like=like)
    if like_product.quantity > 1:
        like_product.quantity -= 1
        like_product.save()
    else:
        like_product.delete()
    return redirect('like_detail')
