from django.http import JsonResponse
from django.shortcuts import redirect, render
from base.models import Listing, Order, Profile
from base.sessions import sessiondetails, sessionprofile
from rest_framework.views import APIView
from .serializers import SerializedOrder
from rest_framework.parsers import JSONParser

def startorder(request, id):
    neworder = Order()
    neworder.buyerid = sessionprofile(request)
    neworder.listingid = Listing.objects.get(id=id)
    neworder.status = 'PENDING'
    neworder.save()
    return render(request, 'order.html', sessiondetails(request, {'order': neworder}))


def myorders(request):
    orders = Order.objects.filter(buyerid=sessionprofile(
        request)).exclude(status='CANCELLED')
    return render(request, 'myorders.html', sessiondetails(request, {'orders': orders}))


def continueorder(request, id):
    prevorder = Order.objects.get(id=id)
    return render(request, 'order.html', sessiondetails(request, {'order': prevorder}))


def orderstatus(request, id):

    order = Order.objects.get(id=id)
    if request.POST['status'] == 'ORDERED':
        user = sessionprofile(request)
        user.money = user.money - order.listingid.price
        user.save()
        merchant = order.listingid.sellerid
        merchant.money = merchant.money + order.listingid.price
        merchant.save()
    if request.POST['status'] == 'CANCELLED' and order.status == 'ORDERED':
        user = sessionprofile(request)
        user.money = user.money + order.listingid.price
        user.save()
        merchant = order.listingid.sellerid
        merchant.money = merchant.money - order.listingid.price
        merchant.save()
    if request.POST['status'] == '':
        return redirect('merchantorders')
    order.status = request.POST['status']
    order.save()
    if not request.headers['Referer'].find('merchantorders') == -1:
        return redirect('merchantorders')
    elif not request.headers['Referer'].find('myorders') == -1 or not request.headers['Referer'].find('reorder') == -1:
        return redirect('myorders')
    elif not request.headers['Referer'].find('order/order') == -1:
        return redirect('marketplace')


def merchantorders(request):
    user=  sessionprofile(request)
    if not user.role == 'Vendor':
        return render(request,'401.html',sessiondetails(request))
    orders = Order.objects.filter(listingid__sellerid=sessionprofile(
        request)).exclude(status='CANCELLED').exclude(status='PENDING')
    return render(request, 'merchantorders.html', sessiondetails(request, {'orders': orders}))


class myordersapi(APIView):

    def get(self,request):
        id = request.GET.get('id')
        orders = SerializedOrder(Order.objects.filter(buyerid__id=id).exclude(status='CANCELLED'),many=True)
        return JsonResponse(orders.data,safe=False)


class merchantordersapi(APIView):

    def get(self,request):
        id = request.GET.get('id')
        orders = SerializedOrder(Order.objects.filter(listingid__sellerid__id=id).exclude(status='CANCELLED').exclude(status='PENDING'),many=True)
        return JsonResponse(orders.data,safe=False)


class orderapi(APIView):

    def post(self,request):
         orderreq = JSONParser().parse(request)
         listing = Listing.objects.get(id = orderreq['order'])
         user = Profile.objects.get(id = orderreq['user'])
         neworder = Order(buyerid = user,listingid = listing,status = orderreq['status'])
         user.money -= listing.price
         listing.sellerid.money += listing.price
         listing.sellerid.save()
         user.save()
         neworder.save()
         return JsonResponse({},status=200)

    def put(self,request):
        update = JSONParser().parse(request)
        order = Order.objects.get(id = update['order'])
        order.status = update['status']
        if order.status == 'CANCELLED':
            order.listingid.sellerid.money -=order.listingid.price
            order.listingid.sellerid.save()
            order.buyerid.money+=order.listingid.price
            order.buyerid.save()
        order.save()
        return JsonResponse({},status = 200)

