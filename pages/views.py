from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.mail import send_mail
from contacts.models import Message

# Create your views here.

def index(request):
  return render(request, 'pages/index.html')


def message(request):

  if request.method == "POST":

    try:
      name = request.POST['name'] 
      email = request.POST['email'] 
      find_us = request.POST['find-us'] 
      news = request.POST['news']
      if news == 'on':
        news = True
      message = request.POST['message']
    except:
      news = False 
      message = request.POST['message']

    postData = {
      'name': name,
      'email': email,
      'find_us': find_us,
      'news': news,
      'message': message
    }

    errors = Message.objects.basic_validator(postData)

    if len(errors) > 0:
      for key, value in errors.items(): 
        messages.error(request, value)
        return redirect('index')
    else:
      Message.objects.create(name=postData['name'],email=postData['email'],find_us=postData['find_us'],news=postData['news'],message=postData['message'])
      
      return redirect('email')

  return redirect('index')

def email(request):
  
  msg = Message.objects.last()

  send_mail(
    'Omnifood', 
    f'Hello, {msg.name}, thank-you for messaging us. We look forward to providing you with the healthiest food available.', 
    '', 
    [''],
    fail_silently=False)

  messages.success(request, 'Your message was successfully sent')

  return redirect('index')