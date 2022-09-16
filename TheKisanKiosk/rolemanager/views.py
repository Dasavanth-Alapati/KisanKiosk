import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from base.sessions import sessiondetails, sessionprofile
from base.models import Profile, RoleRequest
from rest_framework.views import APIView
from .serializers import SerializedRoleRequest
from rest_framework.parsers import JSONParser


def rolerequest(request):
    if request.method == 'POST':
        req = RoleRequest.objects.get(id=request.session['roleid'])
        req.reason = request.POST['reason']
        req.save()
        del request.session['roleid']
        return redirect('homepage')
    else:
        return render(request, 'rolerequest.html', sessiondetails(request, {'rolereq': RoleRequest.objects.get(id=request.session['roleid']).role}))


def roledisplay(request):
    user = sessionprofile(request)
    if not user.role == 'Admin':
        return render(request, '401.html', sessiondetails(request))
    reqs = RoleRequest.objects.filter(status='PENDING')
    return render(request, 'requestdisplay.html', sessiondetails(request, {'reqs': reqs}))


def roleapproval(request, id=None):
    user = sessionprofile(request)
    if not user.role == 'Admin':
        return render(request, '401.html', sessiondetails(request))
    choice = request.POST['choice']
    req = RoleRequest.objects.get(id=id)
    req.status = choice
    if choice == 'APPROVED':
        req.profileid.role = req.role
    req.profileid.save()
    req.save()
    return redirect('requestdisplay')

class apirolerequest(APIView):
    def get(self,request):
        rolereqs = SerializedRoleRequest(RoleRequest.objects.filter(status='PENDING'),many=True)
        return JsonResponse(rolereqs.data,safe=False)

    def put(self,request):
        req = JSONParser().parse(request)
        requests = RoleRequest.objects.get(id = req['id'])
        requests.status = 'APPROVED'if req['decision'] else 'REJECTED'
        requests.save()
        if req['decision']:
            requests.profileid.role = requests.role
            requests.profileid.save()
        return JsonResponse({},status=200)

    def post(self,request):
        req = JSONParser().parse(request)
        newrequest = RoleRequest(profileid = Profile.objects.get(id = req['user']),role = req['role'],reason = req['reason'],status = 'PENDING').save()
        return JsonResponse({},status=200)
