from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class Movie(models.Model):
    name=models.CharField(max_length=36,null=True)
    auto_reg_no=models.CharField(max_length=10,blank=False,unique=True)
    mobile=models.IntegerField(unique=True)
    city=models.CharField(max_length=36,null=False,blank=False)
    regular_stand=models.CharField(max_length=36,null=False)
    profile_pic=models.ImageField(upload_to='uploads/',blank=True)

    def no_of_ratings(self):
        ratings=Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum=0
        ratings=Rating.objects.filter(movie=self)
        for rating in ratings:
            sum +=rating.stars
        if len(ratings) > 0:
            return sum /len(ratings)
        else:
            return 0

    def __str__(self):
        return self.name


class Rating(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together=(('user','movie'),)
        index_together=(('user','movie'),)

    def __str__(self):
        return self.user

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)