from django.shortcuts import render, redirect, get_object_or_404
from .models import product, review_rating, User
from cart.models import CartItem


def trending(request):
    items = product.objects.all()
    categories = {item.category.title() for item in items}
    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'trending.html', context)


def filterByCategory(request, category=str):
    items = product.objects.filter(category=category)
    categories = {category, }
    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'trending.html', context)


def allfruitsByCategory(request, category=str):
    items = product.objects.filter(category=category)
    categories = {category, }
    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'all_fruits.html', context)


def get_product(request, pid):
    item = product.objects.get(pid=pid)
    review = review_rating.objects.filter(pid=pid)
    review_count = review_rating.objects.filter(pid=pid, review=True).count()
    request.session['review_count'] = review_count
    context = {
        'item': item,
        'reviews': review,
        'review_count': review_count

    }
    return render(request, 'product-details.html', context)


def search_product(request):
    keywords = request.POST.get('keywords').split(' ')
    items = product.objects.filter(title__icontains=keywords[0], description__icontains=keywords[0])
    for key in keywords[1:]:
        items = items.union(product.objects.filter(title__icontains=key, description__icontains=key))
    categories = {item.category for item in items}
    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'trending.html', context)


def review_show(request, pid):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        title = request.POST['title']
        review = request.POST['review']
        rate = request.POST['rate']
        uid = request.session.get('user')
        user = User.objects.get(id=uid)
        pid = request.POST['pid']
        Product = product.objects.get(pid=pid)
        Review = review_rating(
            uid=user,
            pid=Product,
            title=title,
            review=review,
            rate=rate,
        )
        Review.save()
        request.session['review_count'] += 1
        return redirect(url)

