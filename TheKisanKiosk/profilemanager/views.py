from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from base.sessions import sessiondetails, sessionprofile
from .forms import editprofile, money
from django.conf import settings
from base.models import Profile
from rolemanager.roles import createrolerequest
from rest_framework.parsers import JSONParser
from .serializers import SerializedProfile
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


def profiledisplay(request, id=None):
    if id == None:
        user = sessionprofile(request)
    else:
        user = Profile.objects.get(id=id)
    return render(request, "profile.html", sessiondetails(request, {'prof': user, 'profimage': settings.PROFILEPIC_ROOT+'default.jpg' if (user.profilepic == False) else settings.PROFILEPIC_ROOT+user.credid.username+".jpeg"}))


def profileedit(request):
    if request.method == 'POST':
        user = sessionprofile(request)
        edit = editprofile(request.POST)
        if edit.is_valid():
            if not edit.cleaned_data['name'] == '':
                user.name = edit.cleaned_data['name']
            if not edit.cleaned_data['bio'] == '':
                user.bio = edit.cleaned_data['bio']
            user.save()
            role = edit.cleaned_data['role']
            if not role == '' and not role == user.role:
                return createrolerequest(request, role)
            return redirect('profiledisplay')
    else:
        return render(request, 'profileedit.html', sessiondetails(request, {'form': editprofile()}))


def addmoney(request):
    if request.method == 'POST':
        addition = money(request.POST)
        if addition.is_valid():
            print(addition.cleaned_data)
            profile = sessionprofile(request)
            profile.money = profile.money + addition.cleaned_data['amount']
            profile.save()
            if not request.session['Referer'].find('display') == -1:
                del request.session['Referer']
                return redirect('profiledisplay')
            else:
                del request.session['Referer']
                return redirect('myorders')
        else:
            return render(request, 'addmoney.html', sessiondetails(request, {'form': money()}))
    else:
        request.session['Referer'] = request.headers['Referer']
        return render(request, 'addmoney.html', sessiondetails(request, {'form': money()}))


class apiprofile(APIView):
    def get(self, request):
        res = JWTAuthentication().authenticate(request)
        user,token = res
        profile = Profile.objects.get(credid=user)
        if request.GET.get('token') != None:
            profile = Profile.objects.get(id=int(request.GET['token']))
        resuser = SerializedProfile(profile)
        return JsonResponse(resuser.data, status=200, safe=False)

    def put(self,request):
        editdata = JSONParser().parse(request)
        user = Profile.objects.get(id=editdata['user'])
        if not editdata['name'] == '':
            user.name = editdata['name']
        if not editdata['bio'] == '':
            user.bio = editdata['bio']
        if not editdata['role'] == '':
            user.role = editdata['role']
        user.save()
        return JsonResponse({},status = 200)

class apimoney(APIView):
    def post(self, request):
        money = JSONParser().parse(request)
        user = Profile.objects.get(id=money['user'])
        user.money += money['money']
        user.save()
        return JsonResponse({}, status=200)
