"""
Definition of models.
"""

from cProfile import label
from enum import unique
from pickle import FALSE
from pyexpat import model
from statistics import mode
from tokenize import blank_re
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class love_bao(models.Model):
    username = models.CharField(max_length = 100,blank=True,null=True)
    url_def = models.CharField(max_length = 100,unique=True)
    banner_pic = models.ImageField(upload_to='images/',blank=True,null=True)
    left_bao_name = models.CharField(max_length = 100,null=True)
    left_bao_pic = models.ImageField(upload_to='images/',blank=True,null=True)
    left_bao_ig = models.CharField(max_length= 200,blank=True,null=True)
    left_bao_des = models.CharField(max_length = 500,blank=True,null=True)
    right_bao_name = models.CharField(max_length = 100,null=True)
    right_bao_pic = models.ImageField(upload_to='images/',blank=True,null=True)
    right_bao_ig = models.CharField(max_length = 200,blank=True,null=True)
    right_bao_des = models.CharField(max_length = 500,blank=True,null=True)
    bao_together_date = models.DateTimeField()
    bao_bao_talk = models.CharField(max_length = 500,blank=True,null=True)
    bao_big_thing_title1 = models.CharField(max_length = 50,blank=True,null=True)
    bao_big_thing_date1 = models.DateTimeField(blank=True,null=True)
    bao_big_thing_des1 = models.CharField(max_length = 500,blank=True,null=True)

    bao_big_thing_title2 = models.CharField(max_length = 50,blank=True,null=True)
    bao_big_thing_date2 = models.DateTimeField(blank=True,null=True)
    bao_big_thing_des2 = models.CharField(max_length = 500,blank=True,null=True)

    bao_big_thing_title3 = models.CharField(max_length = 50,blank=True,null=True)
    bao_big_thing_date3 = models.DateTimeField(blank=True,null=True)
    bao_big_thing_des3 = models.CharField(max_length= 500,blank=True,null=True)

    bao_big_thing_title4 = models.CharField(max_length = 50,blank=True,null=True)
    bao_big_thing_date4 = models.DateTimeField(blank=True,null=True)
    bao_big_thing_des4 = models.CharField(max_length = 500,blank=True,null=True)
    bao_six_pic1 = models.ImageField(upload_to='images/',blank=True,null=True)
    bao_six_pic2 = models.ImageField(upload_to='images/',blank=True,null=True)
    bao_six_pic3 = models.ImageField(upload_to='images/',blank=True,null=True)
    bao_six_pic4 = models.ImageField(upload_to='images/',blank=True,null=True)
    bao_six_pic5 = models.ImageField(upload_to='images/',blank=True,null=True)
    bao_six_pic6 = models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self):
      return str(self.user)


    


