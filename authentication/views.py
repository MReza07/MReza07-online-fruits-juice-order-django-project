from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from .models import contact_info
from cart.models import CartItem
from productapp.models import product,review_rating

# Create your views here.
def index(request):
    items=product.objects.all()
    categories = {item.category.title() for item in items}

    context={
        'items': items,
        'categories': categories,
        'cart_count': request.session.get('cart_count'),
        'order_count': request.session.get('order_count'),

    }
    return render(request, 'index.html',context)


########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################

            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form, 'title': 'register here'})


################ login forms###################################################
def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            request.session['user']=user.id
            cart_count=CartItem.objects.filter(uid=user.id,ordered=False).count()
            request.session['cart_count']=cart_count
            order_count = CartItem.objects.filter(uid=user.id, ordered=True).count()
            request.session['order_count'] = order_count
            messages.success(request, f' welcome {username} !!')
            return redirect(index)
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})


def Logout(request):
    logout(request=request)
    request.session['user']=0
    request.session['cart_count'] = 0
    return redirect('index')


def contact(request):
    title = 'Contact '
    contactdese = 'Please contact here for Query'
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        my_data = contact_info(cname=name, cemail=email, csubject=subject, cmessage=message)
        my_data.save()

    return render(request, 'contact.html', {'title': title, 'contactdese': contactdese})
