from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import employees

from django_daraja.mpesa import utils
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime
from django.shortcuts import render

cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'

def index_page(request):
    data = employees.objects.all()
    context = {'data': data}
    return render(request, "index.html", context)


def edit_page(request):
    return render(request, "edit.html")


def homepage(request):
    return render(request, "homepage.html")


def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        number = request.POST.get('number')
        ethnicity = request.POST.get('ethnicity')
        Amount = request.POST.get('Amount')

        query = employees(name=name, email=email, age=age, gender=gender, number=number, ethnicity=ethnicity, Amount=Amount)
        query.save()
        return redirect("/")

        return render(request, "index.html")


def deleteData(request, id):
    d = employees.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        Name = request.POST.get('Name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        number = request.POST.get('number')
        ethnicity = request.POST.get('ethnicity')
        Amount = request.POST.get('Amount')

        update_info = employees.objects.get(id=id)
        update_info.Name = Name
        update_info.email = email
        update_info.age = age
        update_info.gender = gender
        update_info.phone = phone
        update_info.number = number
        update_info.ethnicity = ethnicity
        update_info.Amount = Amount

        update_info.save()
        return redirect("/")

    d = employees.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)

def pay(request, id):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_reference = 'STONES'
        transaction_desc = 'STK Push Description'
        callback_url = stk_push_callback_url
        r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return JsonResponse(r.response_description, safe=False)

    return render(request, 'index.html')