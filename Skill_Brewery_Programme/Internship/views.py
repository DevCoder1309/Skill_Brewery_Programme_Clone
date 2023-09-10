from django.shortcuts import render,HttpResponseRedirect, redirect
from django import forms
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.
#creating a class for the django form
class Details(forms.Form):
    name = forms.CharField(max_length=100)
    degree = forms.CharField(
        max_length=100)
    current_semester = forms.CharField(
        max_length=100)
    track = forms.CharField(
        max_length=100, widget=forms.Select(choices=[
            ('ant', '"------------"'),
            ('op', 'Web Dev'),
            ('in', 'App Dev'),
            ('pp', 'Product Management'),
            ('nn', 'Computer Vision'),
            ('ds', 'Data Science'),
            ('db', 'DBMS'),
            ('cb', 'Cybersecurity')
        ]))
    email = forms.CharField(
        max_length=100)
    verification_code = forms.IntegerField()
    phone_number = forms.IntegerField()


def index(request):
    app = Details(request.POST)
    return render(request, "Internship/index.html",{
        "app": app
    }) 
def page_1(request):
    app = Details(request.POST)
    return render(request, "Internship/datasc.html", {
        "app": app
    })


def page_2(request):
    app = Details(request.POST)
    return render(request, "Internship/cyber.html", {
        "app": app
    })
def page_3(request):
    return render(request, "Internship/t&s.html")

def email(request):
    if request.method== "POST":
        form = Details(request.POST)
        if form.is_valid():
            print('hello')
            subject = 'Codevita Skill-Brewery Internship Program'
            message = f'testing purpose ke liye bheja email'
            email_from = settings.EMAIL_HOST_USER
            ap = form.cleaned_data["email"]
            oo = form.cleaned_data["track"]
            qm = form.cleaned_data["name"]
            if(oo=='op'):
                message = f'Hello there {qm}! Thank you for filling your inerest as Web Dev please go through the google form sent to you fill this and submit this! thankyou! https://forms.gle/sYsj6wvFBQ6pX41s6'
            if (oo == 'in'):
                message = f'Hello there {qm}! Thank you for filling your inerest as App Dev please go through the google form sent to you fill this and submit this! thankyou! https://forms.gle/9GwAnpaChgAX5Syn9'
            if (oo == 'pp'):
                message = f'Hello there {qm}! Thank you for filling your inerest as Product Management please go through the google form sent to you fill this and submit this! thankyou! https://forms.gle/ye8b2nx4pgdCFeLV9'
            if (oo == 'nn'):
                message = f'Hello there {qm}! Thank you for filling your inerest as Computer Vision please go through the google form sent to you fill this and submit this! thankyou! https://forms.gle/Ybz3LNXx7q6cFbFi7'
            if (oo == 'ds'):
                message = f'Hello there {qm}! Thank you for filling your inerest as Data Science please go through the google form sent to you fill this and submit this! thankyou! https://forms.gle/PdrkeeBr6iufyGY76'
            if (oo == 'db'):
                message = f'Hello there {qm}! Thank you for filling your inerest as DBMS please go through the google form sent to you fill this and submit this! thankyou! https://forms.gle/DmYojpj5EnaGh6cg6'
            if (oo == 'cb'):
                message = f'Hello there {qm}! Thank you for filling your inerest as Cybersecurity please go through the google form sent to you fill this and submit this! thankyou! https://forms.gle/5XCCkxn3uceAGYGV8'
            recipient_list = [ap,]
            send_mail(subject, message, email_from, recipient_list)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "Internship/index.html", {
                "app": form
            })
    return render(request, "Internship/index.html", {
        "app": Details()
    })
