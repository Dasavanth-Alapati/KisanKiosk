from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import post
from base.sessions import sessiondetails, sessionprofile
from base.models import Like, Post, Profile
from commenthandler.nonviews import fetchcomments
from rest_framework.views import APIView
from .serializers import SerializedPost
from rest_framework.parsers import JSONParser


def createpost(request):
    if request.method == 'POST':
        newpost = post(request.POST)
        if newpost.is_valid():
            finalpost = newpost.save(commit=False)
            finalpost.profileid = sessionprofile(request)
            finalpost.save()
            Like(postid=finalpost).save()
            return redirect('postdisplay')
        else:
            return render(request, 'createpost.html', sessiondetails(request, {'post': post()}))
    else:
        return render(request, 'createpost.html', sessiondetails(request, {'post': post()}))


def postdisplay(request):
    return render(request, 'feed.html', sessiondetails(request, {'posts': Post.objects.all().order_by('-like__like', 'like__dislike')}))


def singlepost(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', sessiondetails(request, {'post': post, 'comments': fetchcomments(post, 'post')}))


class apifetchposts(APIView):
    def get(self, request):
        posts = SerializedPost(Post.objects.all().order_by(
            '-like__like', 'like__dislike'), many=True)
        return JsonResponse(posts.data, safe=False)


class apisinglepost(APIView):
    def get(self, request):
        id = request.GET.get('id')
        post = SerializedPost(Post.objects.get(id=id))
        return JsonResponse(post.data, safe=False)

    def post(self,request):
        post = JSONParser().parse(request)
        print(post)
        savepost = Post(title = post['title'],content = post['content'],profileid = Profile.objects.get(id = post['user']))
        savepost.save()
        Like(postid=savepost).save()
        return JsonResponse({},status = 200)

