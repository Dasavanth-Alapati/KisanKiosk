from django import template
from base.models import Comment

register = template.Library()

def commentinception(clist):
    if not clist.count() == 0:
        count = clist.count()
        for cclist in clist:
            count +=commentinception(Comment.objects.filter(commentid=cclist))
        return count
    else:
        return 0
    pass

@register.simple_tag
def commentcount(id,type):
    if type == 'post':
        commentlist = Comment.objects.filter(postid=id)
    elif type == 'listing':
        commentlist = Comment.objects.filter(listingid=id)
    else:
        commentlist = Comment.objects.filter(commentid=id)
    count = 0
    count +=commentinception(commentlist)
    return count