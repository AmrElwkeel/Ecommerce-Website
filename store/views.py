from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import storeSerializers


def store(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'store.html', context)


def cart(request):

    if request.user.is_authenticated: 
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer= customer, complete= False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items' : 0 }
       

    context = {'items':items , 'order':order }
    return render(request, "cart.html", context)


def checkout(request):

    if request.user.is_authenticated: 
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer= customer, complete= False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items' : 0 }
       

    context = {'items':items , 'order':order }
    return render(request, "checkout.html", context)


def main(request):
    context = {}
    return render(request, "main.html", context)



@api_view(['GET'])
def StoreApi(request):
    query_api = Product.objects.all()
    data = StoreSerializers(query_api, many=True).data
    return Response({'data': data})