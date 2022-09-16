from django.shortcuts import redirect
from base.models import RoleRequest
from base.sessions import sessionprofile

def createrolerequest(request,role):
    if(not role == 'Farmer'):
        rolereq = RoleRequest(
            role=role, reason='', profileid=sessionprofile(request), status='PENDING')
        rolereq.save()
        request.session['roleid'] = rolereq.id
        return redirect('rolerequest')
    else:
        prof = sessionprofile(request)
        prof.role = role
        prof.save()
        return redirect('homepage') 