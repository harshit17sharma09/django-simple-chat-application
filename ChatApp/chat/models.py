# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name ='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length =100)
    timestamp = models.DateTimeField(auto_now_add = True)
    is_read = models.BooleanField(default = False)
    

    def __str__(self):
        return self.message
    
    class Meta:
        ordering = ('timestamp',)
