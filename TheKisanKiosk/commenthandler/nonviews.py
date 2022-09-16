from email.policy import default
from base.models import Comment
from django.db.models import Case, When


def fetchcomments(id, type):
    if type == 'post':
        comments = Comment.objects.filter(postid=id).annotate(rolevalue=Case(When(
            profileid__role='Expert', then=0), default=1)).order_by('rolevalue', '-like__like', 'like__dislike')
    elif type == 'listing':
        comments = Comment.objects.filter(listingid=id).order_by('-like__like', 'like__dislike')
    else:
        comments = Comment.objects.filter(commentid=id).order_by('-like__like', 'like__dislike')
    return comments
