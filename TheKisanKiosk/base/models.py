from django.utils import timezone
from django.db import models
from .timehandling import itemage
from django.contrib.auth.models import User


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    postid = models.ForeignKey(
        'Post', models.CASCADE, db_column='postid', blank=True, null=True,related_name='comment')
    content = models.CharField(max_length=1000)
    listingid = models.ForeignKey(
        'Listing', models.CASCADE, db_column='listingid', blank=True, null=True,related_name='comment')
    profileid = models.ForeignKey(
        'Profile', models.SET_NULL, db_column='profileid', null=True)
    commentid = models.ForeignKey(
        'Comment', models.CASCADE, db_column='commentid', null=True,related_name='comment')


    def __str__(self) -> str:
        return self.content

    def age(self):
        return itemage(self.created_at)

    class Meta:
        managed = True
        db_table = 'Comment'


class Credentials(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(
        max_length=255, unique=True, db_collation='utf8_bin')
    password = models.CharField(max_length=255, db_collation='utf8_bin')

    def __str__(self) -> str:
        return self.username

    def age(self):
        return itemage(self.created_at)
    class Meta:
        managed = True
        db_table = 'Credentials'


class Likeinfo(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    profileid = models.ForeignKey(
        'Profile', models.SET_NULL, db_column='profileid', null=True)
    likes = models.CharField(max_length=6, choices=[
                             ("YES", "YES"), ("NO", "NO"),("UNSURE","UNSURE")])
    likeid = models.ForeignKey('Like', models.CASCADE, db_column='likeid',related_name='likeinfo')

    def __str__(self) -> str:
        return self.likes

    def age(self):
        return itemage(self.created_at)
    class Meta:
        managed = True
        db_table = 'LikeInfo'


class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    sellerid = models.ForeignKey(
        'Profile', models.CASCADE, db_column='profileid')
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=True, null=True)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name

    def age(self):
        return itemage(self.created_at)
    class Meta:
        managed = True
        db_table = 'Listing'


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    profileid = models.ForeignKey(
        'Profile', models.SET_NULL, db_column='profileid', null=True)
    content = models.CharField(max_length=2000)
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    def age(self):
        return itemage(self.created_at)
    class Meta:
        managed = True
        db_table = 'Post'


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    postid = models.OneToOneField(
        Post, models.CASCADE, db_column='postid', null=True, related_name='like')
    listingid = models.OneToOneField(
        'Listing', models.CASCADE, db_column='listingid', null=True, related_name='like')
    commentid = models.OneToOneField(
        Comment, models.CASCADE, db_column='commentid', null=True, related_name='like')

    def __str__(self) -> str:
        return (str(self.like)+","+str(self.dislike))

    def age(self):
        return itemage(self.created_at)
    class Meta:
        managed = True
        db_table = 'Like'


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=6, choices=[(
        "Farmer", "Farmer"), ("Vendor", "Vendor"), ("Expert", "Expert"), ("Admin", "Admin")])
    profilepic = models.BooleanField(default=False)
    bio = models.CharField(max_length=255, null=True,default='Add a Bio')
    money = models.FloatField(default=0)
    credid = models.OneToOneField(User,models.CASCADE,related_name='profile',null=True)


    def __str__(self) -> str:
        return self.name

    def age(self):
        return itemage(self.created_at)
    class Meta:
        managed = True
        db_table = 'Profile'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    buyerid = models.ForeignKey(
        Profile, models.CASCADE, db_column='buyerid', related_name="buyer_id")
    listingid = models.ForeignKey(
        Listing, models.SET_NULL, db_column='listingid', null=True)
    status = models.CharField(max_length=11, choices=[("PENDING", "PENDING"), ("ORDERED", "ORDERED"), (
        "DELIVERED", "DELIVERED"), ("IN_TRANSIT", "IN_TRANSIT"), ("CANCELLED", "CANCELLED")])

    def __str__(self) -> str:
        return (str(self.buyerid.name+","+self.listingid.name)+","+str(self.status))

    def age(self):
        return itemage(self.created_at)
    class Meta:
        managed = True
        db_table = 'Order'


class RoleRequest(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    profileid = models.ForeignKey(
        'Profile', models.CASCADE, db_column='profileid', null=True)
    role = models.CharField(max_length=6, choices=[(
        "Vendor", "Vendor"), ("Expert", "Expert"), ("Admin", "Admin")])
    reason = models.CharField(max_length=1000, null=True)
    status = models.CharField(max_length=8, choices=[(
        'APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED'), ('PENDING', 'PENDING')])

    def __str__(self) -> str:
        return (self.profileid.name + ':'+self.role+':'+self.status)

    def age(self):
        return itemage(self.created_at)
    class Meta:
        managed = True
        db_table = 'RoleRequest'



# class Cart(models.Model):
#     id = models.AutoField(primary_key=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     profileid = models.ForeignKey(
#         'Profile', models.CASCADE, db_column='profileid', null=True)
#     listingid = models.ForeignKey(
#         Listing, models.SET_NULL, db_column='listingid', null=True)

#     def __str__(self) -> str:
#         return (self.profileid.name + ':'+self.listingid.name)

#     class Meta:
#         managed = True
#         db_table = 'Cart'


# class DeliveryAddress(models.Model):
#     id = models.AutoField(primary_key=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     profileid = models.ForeignKey(
#         'Profile', models.CASCADE, db_column='profileid', null=True)
#     address = models.CharField(max_length=1000)

#     def __str__(self) -> str:
#         return (self.profileid.name + ':'+self.address)

#     class Meta:
#         managed = True
#         db_table = 'DeliveryAddress'
