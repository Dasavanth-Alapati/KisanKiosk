from base.models import Likeinfo

def liked(id,user):
    likedata = Likeinfo.objects.filter(likeid__id = id).filter(profileid__id = user)
    if not len(likedata) == 0: 
        if likedata.likes == 'YES':
            return 1
        else:
            return -1
    else:
        return 0