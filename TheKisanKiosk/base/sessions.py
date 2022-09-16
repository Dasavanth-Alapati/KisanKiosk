from django.conf import settings
from .models import Profile


def createsession(request, userid):
    request.session['userid'] = userid


def purgesession(request):
    request.session.flush()


def sessiondetails(request, context={}):
    try:
        profile = Profile.objects.get(credid=request.session['userid'])
        return {"profile":profile,'name': profile.name, 'role': profile.role, 'image': settings.PROFILEPIC_ROOT+'default.jpeg' if (profile.profilepic == False) else settings.PROFILEPIC_ROOT+profile.credid.username+".jpeg",'STATIC_URL':settings.STATIC_URL, **context}
    except KeyError:
        return context

def sessionprofile(request):
    try:
        return Profile.objects.get(credid=request.session['userid'])
    except KeyError:
        return False
