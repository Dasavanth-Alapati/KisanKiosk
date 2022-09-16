

from django import template
from base.models import Likeinfo

register = template.Library()

@register.simple_tag
def likefind(id,user):
    likedata = Likeinfo.objects.filter(likeid__id = id).filter(profileid__id = user)
    if not len(likedata) == 0:
        likedata=likedata[0]
        if likedata.likes == 'YES':
            return True
        else:
            return False
    else:
        return False

@register.simple_tag
def dislikefind(id,user):
    likedata = Likeinfo.objects.filter(likeid__id = id).filter(profileid__id = user)
    if not len(likedata) == 0:
        likedata=likedata[0]
        if likedata.likes == 'NO':
            return True
        else:
            return False
    else:
        return False
