from django.shortcuts import render
from django import forms

from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
#creating a class for the django form
class Details(forms.Form):
    name = forms.CharField(max_length=100)
    degree = forms.CharField(
        max_length=100)
    current_semester = forms.CharField(
        max_length=100)
    choices = [
        ('ant', '"------------"'),
        ('op', 'Web Dev'),
        ('in', 'App Dev'),
        ('pp', 'Product Management'),
        ('nn', 'Computer Vision'),
        ('ds', 'Data Science'),
        ('db', 'DBMS'),
        ('cb', 'Cybersecurity')
    ]
    track = forms.CharField(
        max_length=100, widget=forms.Select(choices=choices))
    email = forms.CharField(
        max_length=100)
    verification_code = forms.IntegerField()

def index(request):
    app = Details(request.POST)
    return render(request, "Internship/home.html",{
        "app": app
    }) 

# verification of the form as mentioned in the skill brewery programme
def verification(request):
    pp = Details(request.POST)
    subject = 'welcome to GFG world'
    message = 'https://docs.google.com/forms/d/e/1FAIpQLSefbbbeRtyqv3c8Nqp3_BMFQC5hw4k1xPcgRa7shyFAYPqBFg/viewform?vc=0&c=0&w=1&flr=0'
    email_from = settings.EMAIL_HOST_USER
    ap = pp.cleaned_data["email"]
    recipient_list = ap
    send_mail( subject, message, email_from, recipient_list )
    return