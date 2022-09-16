from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from base.sessions import sessiondetails, sessionprofile
from .forms import listingform
from base.models import Like, Listing, Profile
from commenthandler.nonviews import fetchcomments
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .serializers import SerializedListing

def createlisting(request):
    if request.method == 'POST':
        newlisting = listingform(request.POST)
        if newlisting.is_valid():
            finallisting = newlisting.save(commit=False)
            finallisting.sellerid = sessionprofile(request)
            finallisting.save()
            Like(listingid=finallisting).save()
            return redirect('marketplace')
        else:
            return render(request, 'createlisting.html', sessiondetails(request, {'form': listingform()}))
    else:
        return render(request, 'createlisting.html', sessiondetails(request, {'form': listingform()}))


def marketplace(request):
    return render(request, 'marketplace.html', sessiondetails(request, {'listings': Listing.objects.all().order_by('-like__like', 'like__dislike')}))


def singlelisting(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, 'listing.html', sessiondetails(request, {'listing': listing, 'comments': fetchcomments(listing, 'listing')}))

class apimarketplace(APIView):
    def get(self,request):
        marketplace = SerializedListing(Listing.objects.all().order_by('-like__like', 'like__dislike'),many = True)
        return JsonResponse(marketplace.data,safe=False)

class apilisting(APIView):
    def get(self,request):
        id = request.GET.get('id')
        listing = SerializedListing(Listing.objects.get(id=id))
        return JsonResponse(listing.data,safe=False)

    def post(self,request):
        listing = JSONParser().parse(request)
        finallisting = Listing(name = listing['name'],description = listing['description'],price = listing['price'],sellerid = Profile.objects.get(id = listing['user']))
        finallisting.save()
        Like(listingid=finallisting).save()
        return JsonResponse({},status = 200)

