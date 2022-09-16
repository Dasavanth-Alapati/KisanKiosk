from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.shortcuts import redirect, render
from base.forms import credentialsreg
from base.models import Credentials, Profile
from base.sessions import createsession, purgesession
from profilemanager.serializers import SerializedProfile
from rest_framework.views import APIView
from base.jwt import *
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        user = Profile.objects.filter(credid__username=request.POST['username'])
        if len(user) == 0:
            return render(request, 'login.html', {'creds': credentialsreg(), 'err': 'User doesn\'t exist'})
        # elif not user[0].credid.password == request.POST['password']:
        #     return render(request, 'login.html', {'creds': credentialsreg(), 'err': 'Enter the correct password'})
        else:
            createsession(request, user[0].credid.id)
            return redirect('homepage')
    else:
        return render(request, 'login.html', {'creds': credentialsreg()})


def logout(request):
    purgesession(request)
    return redirect('homepage')


class apilogin(APIView):
    permission_classes = [AllowAny]
    def post(self, request):

        cred = JSONParser().parse(request)
        user = User.objects.filter(username=cred['username'])
        if len(user) == 0:
            return JsonResponse({}, status=404)
        elif not user[0].password == cred['password']:
            return JsonResponse({}, status=403)
        resuser = SerializedProfile(Profile.objects.get(credid=user[0]))
        resuser = resuser.data
        resuser.update({'username':cred['username']})
        access_token = create_access_token(resuser)
        refresh_token = create_refresh_token(resuser)
        return JsonResponse(resuser, status=200, safe=False)
# {'access':access_token,'refresh':refresh_token}

