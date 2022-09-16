from django.http import JsonResponse
from django.shortcuts import redirect, render
from base.models import Comment, Like, Listing, Post, Profile
from base.sessions import sessiondetails, sessionprofile
from .nonviews import fetchcomments
from rest_framework.views import APIView
from .anotherserializers import SerializedMainComment
from rest_framework.parsers import JSONParser


def createcomment(request, id, type):
    newcomment = Comment()
    newcomment.content = request.POST['comment']
    newcomment.profileid = sessionprofile(request)
    if(type == 'post'):
        newcomment.postid = Post.objects.get(id=id)
    elif(type == 'listing'):
        newcomment.listingid = Listing.objects.get(id=id)
    else:
        newcomment.commentid = Comment.objects.get(id=id)
    newcomment.save()
    Like(commentid=newcomment).save()
    if(type == 'post'):
        return redirect('singlepost', id=id)
    elif(type == 'listing'):
        return redirect('singlelisting', id=id)
    else:
        return redirect('singlecomment',id=id)

def singlecomment(request,id):
    comment = Comment.objects.get(id=id)
    return render(request,'comment.html',sessiondetails(request,{'mcomment':comment,'comments':fetchcomments(comment,'comment')}))

class commentapi(APIView):

    def get(self,request):
        id = request.GET.get('id')
        comment = SerializedMainComment(Comment.objects.get(id=id))
        return JsonResponse(comment.data,safe=False)

    def post(self,request):
        comment = JSONParser().parse(request)
        newcomment = Comment(content = comment['comment'],profileid = Profile.objects.get(id = comment['user']))
        id = comment['id']
        type = comment['type']
        if(type == 'post'):
            newcomment.postid = Post.objects.get(id=id)
        elif(type == 'listing'):
            newcomment.listingid = Listing.objects.get(id=id)
        else:
            newcomment.commentid = Comment.objects.get(id=id)
        newcomment.save()
        Like(commentid=newcomment).save()
        return JsonResponse({},status=200)