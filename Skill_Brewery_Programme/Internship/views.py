from django.shortcuts import render
from django import forms
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
def page_1(request):
    app = Details(request.POST)
    return render(request, "Internship/Data_Science_Fastrack.html", {
        "app": app
    })


def page_2(request):
    app = Details(request.POST)
    return render(request, "Internship/Cybersecurity_Live.html", {
        "app": app
    })
def page_3(request):
    return render(request, "Internship/Termsandconditions.html")