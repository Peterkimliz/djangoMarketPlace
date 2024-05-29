from django.shortcuts import render


def home(request):
    return render(request,'eccommerce/home.html')

def contact(request):
    return render(request,"eccommerce/contact.html")