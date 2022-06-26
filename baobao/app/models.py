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

class love_bao(models.Model):
    user_account_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    url_def = models.CharField(max_length = 100)
    banner_pic = models.ImageField(upload_to='images/',blank=True,null=True)
    left_bao_pic = models.ImageField(upload_to='images/',blank=True,null=True)
    left_bao_ig = models.CharField(max_length= 200,blank=True,null=True)
    left_bao_des = models.CharField(max_length = 500,blank=True,null=True)
    right_bao_pic = models.ImageField(upload_to='images/',blank=True,null=True)
    right_bao_ig = models.CharField(max_length = 200,blank=True,null=True)
    rights_bao_des = models.CharField(max_length = 500,blank=True,null=True)
    bao_together_date = models.DateTimeField()
    bao_bao_talk = models.CharField(max_length = 500,blank=True,null=True)
    bao_big_thing_date1 = models.DateTimeField(blank=True,null=True)
    bao_big_thing_des1 = models.CharField(max_length = 50,blank=True,null=True)
    bao_big_thing_date2 = models.DateTimeField(blank=True,null=True)
    bao_big_thing_des2 = models.CharField(max_length = 50,blank=True,null=True)
    bao_big_thing_date3 = models.DateTimeField(blank=True,null=True)
    bao_big_thing_des3 = models.CharField(max_length= 50,blank=True,null=True)
    bao_big_thing_date4 = models.DateTimeField(blank=True,null=True)
    bao_big_thing_des4 = models.CharField(max_length = 50,blank=True,null=True)
    bao_six_pic1 = models.ImageField(upload_to='images/',blank=True,null=True)
    bao_six_pic2 = models.ImageField(upload_to='images/',blank=True,null=True)
    bao_six_pic3 = models.ImageField(upload_to='images/',blank=True,null=True)
    bao_six_pic4 = models.ImageField(upload_to='images/',blank=True,null=True)
    bao_six_pic5 = models.ImageField(upload_to='images/',blank=True,null=True)
    bao_six_pic6 = models.ImageField(upload_to='images/',blank=True,null=True)


    

