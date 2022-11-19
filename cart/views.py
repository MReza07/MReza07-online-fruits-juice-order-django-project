from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from productapp.models import product
from django.contrib.auth.models import User
from .models import CartItem


# Create your views here.
@login_required()
def cartview(request):
    cart_items = CartItem.objects.filter(
        uid=request.session.get('user'), ordered=False)
    total = sum([float(item.price) for item in cart_items])
    deliveryCharge = sum([float(item.deliveryCharge) for item in cart_items])
    Grant_total = [float(total + deliveryCharge)]
    context = {
        'cart_items': cart_items,
        'cart_count': request.session.get('cart_count'),
        'total': total,
        'deliveryCharge': deliveryCharge,
        'Grant_total': Grant_total

    }
    return render(request, 'cart.html', context)


@login_required()
def add_to_cart(request):
    uid = request.session.get('user')
    pid = request.POST.get("pid")
    qty = request.POST.get("quantity")
    user = User.objects.get(id=uid)
    Product = product.objects.get(pid=pid)
    price = float(qty) * Product.price
    deliveryCharge = float(qty) * Product.deliveryCharge
    cart_item = CartItem(
        uid=user,
        pid=Product,
        price=price,
        deliveryCharge=deliveryCharge,
        qty=qty
    )
    cart_item.save()
    request.session['cart_count'] += 1
    return redirect('cartview')


@login_required()
def removeitem(request, id=id):
    item = CartItem.objects.get(cid=id)
    if item.delete():
        request.session['cart_count'] -= 1
        redirect('cartview')
    return redirect('cartview')
