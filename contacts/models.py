from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re

class MessageManger(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    if len(postData['name']) < 2:
      errors['name'] = 'Name must be at least 2 characters'
    if not EMAIL_REGEX.match(postData['email']):
      errors['email'] = 'Not a valid email'
    if not postData['find_us']:
      errors['find_us'] = 'Please let us know how did you hear about us'
    if len(postData['message']) < 10:
      errors['message'] = 'Message needs to be at least 10 characters'

    return errors

# Create your models here.
class Message(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=200)
  find_us = models.CharField(max_length=20)
  news = models.BooleanField(default=False)
  message = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = MessageManger()

  def __str__(self):
    return f'{self.name}'
