from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from .forms import profilereg
from base.forms import credentialsreg
from base.models import Profile, Credentials
from base.sessions import createsession
from django.core.files.storage import FileSystemStorage
from base.imagehandling import imageformatter
from rolemanager.roles import createrolerequest
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        creds = credentialsreg(data=request.POST)
        if creds.is_valid():
            creds.save()
        else:
            return render(request, 'register.html', {'deets': profilereg(), 'creds': credentialsreg(), 'err': 'Username already exists'})
        prof = profilereg(data=request.POST)
        if prof.is_valid():
            profs = Profile(name=prof.cleaned_data['name'], role='Farmer', credid=Credentials.objects.get(
                username=request.POST['username']))
            profs.save()
            createsession(request, profs.credid.id)
            try:
                pic = request.FILES['profilepic']
                dir_str = settings.MEDIA_ROOT/'ProfilePics/'
                fss = FileSystemStorage(location=dir_str, base_url=dir_str)
                pic.name = creds.cleaned_data['username'] + \
                    "."+pic.name.split(".")[1]
                fss.save(pic.name, pic)
                imageformatter(pic.name)
                fss.delete(pic.name)
                profs.profilepic = True
                profs.save()
            except Exception:
                pass
            return createrolerequest(request,prof.cleaned_data['role'])
    else:
        return render(request, 'register.html', {'deets': profilereg(), 'creds': credentialsreg()})

class apiregister(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        signupdeets = JSONParser().parse(request)
        creds = User.objects.create_user(signupdeets['username'],password=signupdeets['password'])
        prof = Profile()
        prof.name = signupdeets['name']
        prof.role = 'Farmer'
        prof.bio = 'Add a Bio'
        prof.money = 0
        prof.credid = creds
        prof.profilepic = False
        prof.save()
        return JsonResponse({},status = 200)

    def get(self,request):
        user = request.GET.get('username')
        if len(Profile.objects.filter(credid__username = user)) == 0:
            return JsonResponse({'exists':False})
        else:
            return JsonResponse({'exists':True})


