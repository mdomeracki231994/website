from django.shortcuts import render
from .models import *
from django.core.mail import send_mail


def index(request):
    data = Services.objects.all()
    context = {'data': data}
    return render(request, 'Home/index.html', context)


def portfolio(request):
    data = Portfolio.objects.all()
    context = {'data': data}
    return render(request, 'Home/portfolio.html', context)


def about(request):
    return render(request, 'Home/about.html')


def team(request):
    data = Employee.objects.all()
    context = {'data': data}
    return render(request, 'Home/team.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        phone_number = request.POST.get('user_phone_number')
        message = request.POST.get('user_message')
        UserInfo.objects.create(name=name, email=email, phone_number=phone_number, message=message)
        # alert_email(message,email)
    return render(request, 'Home/contact.html')


