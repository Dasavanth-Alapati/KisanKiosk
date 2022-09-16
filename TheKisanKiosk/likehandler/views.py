from django.http import JsonResponse
from .forms import likedata
from base.models import Like, Likeinfo,Profile
from base.sessions import sessionprofile
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser


def process(request):
    data = likedata(request.POST)
    if data.is_valid():
        type = data.cleaned_data['type']
        id = data.cleaned_data['id']
        if type == 'post':
            likeobj = Like.objects.get(postid__id=id)
        elif type == 'listing':
            likeobj = Like.objects.get(listingid__id=id)
        else:
            likeobj = Like.objects.get(commentid__id=id)
        user = Likeinfo.objects.filter(likeid=likeobj).filter(
            profileid=sessionprofile(request))
        if len(user) == 0:
            newuser = Likeinfo(
                likeid=likeobj, profileid=sessionprofile(request), likes='UNSURE')
            newuser.save()
            user = newuser
        else:
            user = user[0]
        return [user, likeobj]


def like(request):
    if request.method == 'POST':
        user, likeobj = process(request)
        if user.likes == 'YES':
            user.likes = 'UNSURE'
            likeobj.like -= 1
        else:
            if user.likes == 'NO':
                likeobj.dislike -= 1
            user.likes = 'YES'
            likeobj.like += 1
        user.save()
        likeobj.save()
        return JsonResponse({}, status=200)


def dislike(request):
    if request.method == 'POST':
        user, likeobj = process(request)
        if user.likes == 'NO':
            user.likes = 'UNSURE'
            likeobj.dislike -= 1
        else:
            if user.likes == 'YES':
                likeobj.like -= 1
            user.likes = 'NO'
            likeobj.dislike += 1
        user.save()
        likeobj.save()
        return JsonResponse({}, status=200)


class LikeApi(APIView):
    def post(self,request):
        likedata = JSONParser().parse(request)
        like = Like.objects.get(id = likedata['like'])
        likeuser = Likeinfo.objects.filter(likeid = like).filter(profileid__id = likedata['user'])
        if likedata['status'] == 1:
            likes = 'YES'
        elif likedata['status'] == 0:
            likes = 'UNSURE'
        else:
            likes = 'NO'
        if len(likeuser) == 0:
            new = Likeinfo(likeid = like,profileid = Profile.objects.get(id = likedata['user']),likes = likes)
            new.save()
            if likes == 'YES':
                like.like += 1
            elif likes == 'NO':
                like.dislike +=1
            like.save()
        else:
            likeuser = likeuser[0]
            if likes == 'YES':
                like.like += 1
                if not likeuser.likes == 'UNSURE':
                    like.dislike -=1
            elif likes == 'NO':
                like.dislike +=1
                if not likeuser.likes == 'UNSURE':
                    like.like -=1
            elif likes == 'UNSURE':
                if likeuser.likes == 'YES':
                    like.like -=1
                else:
                    like.dislike -=1
            like.save()
            likeuser.likes = likes
            likeuser.save()
        return JsonResponse({}, status=200)


