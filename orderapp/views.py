from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import order
from .serializers import OrderSerializer
from rest_framework.views import APIView, Response, status
from django.http import Http404
from rest_framework import generics


# Create your views here.
@login_required()
def checkout(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        email = request.POST['email']
        addr = request.POST['addr']
        phone = request.POST['phone']
        user = request.session['user']
        count = 0
        cartitems = CartItem.objects.filter(uid=user)
        for item in cartitems:
            Order = order(
                cartitem=item,
                first_name=first_name,
                email=email,
                addr=addr,
                phone=phone,
                uid=user,
            )
            Order.save()
            item.ordered = True
            item.save()
            count += 1
        request.session['order_count'] += count
        request.session['cart_count'] = 0

        return redirect('cartview')

    cart_items = CartItem.objects.filter(
        uid=request.session.get('user'), ordered=False)
    total = sum([float(item.price) for item in cart_items])
    deliveryCharge = sum([float(item.deliveryCharge) for item in cart_items])
    Grant_total = [float(total + deliveryCharge)]
    context = {
        'total': total,
        'deliveryCharge': deliveryCharge,
        'Grant_total': Grant_total,
    }

    return render(request, 'checkout.html')


@login_required()
def myorder(request, id=int):
    Order = order.objects.filter(uid=id)
    context = {
        'Order': Order,
    }
    return render(request, 'myorder.html', context)


def cancel(request, oid=int):
    Order = order.objects.get(oid=oid)
    Order.status = 'Canceled'
    Order.save()
    return redirect(myorder, request.session['user'])


"""
# REST API
class OrderApiView(APIView):
    def get(self, request, format=None):
        ords = order.objects.all()
        serializer = OrderSerializer(ords, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('order has been created', status=status.HTTP_201_CREATED)
            # order has been created or serializer.data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderAPIDetail(APIView):
    def get_object(self, oid):
        try:
            return order.objects.get(oid=oid)
        except order.DoesNotExist:
            raise Http404

    def get(self, request, oid, format=None):
        ords = self.get_object(oid=oid)
        serializer = OrderSerializer(ords)
        return Response(serializer.data)

    def put(self, request, oid, format=None):
        ord = order.objects.get(oid=oid)
        serializer = OrderSerializer(data=request.data, instance=ord)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, oid, format=None):
        ord = order.objects.get(oid=oid)
        serializer = OrderSerializer(data=request.data, instance=ord, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, oid, format=None):
        ord = order.objects.get(oid=oid)
        ord.delete()
        return Response('order has been successfully delete', status=status.HTTP_204_NO_CONTENT)
        """


class OrderApiView(generics.ListCreateAPIView):
    queryset = order.objects.all()
    serializer_class = OrderSerializer


class OrderAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = order.objects.all()
    serializer_class = OrderSerializer
