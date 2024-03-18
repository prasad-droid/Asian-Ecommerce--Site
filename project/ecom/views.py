from django.shortcuts import render, redirect
import requests
import json
from . import models
# Create your views here.


def homepage(req):

    return render(req, 'index.html')


def menchoice(req):
    return render(req, 'menchoose.html')


def mensport(req):
    repsonse = requests.get('https://api.jsonserve.com/qDE1Ke')
    result = repsonse.json()
    # here x is single json object only if the object.type === training
    arr = [x for x in result['data'] if x['type'] == 'training']
    return render(req, 'mensport.html', context={"datarr": arr})


def lifesty(req):
    res = requests.get('https://api.jsonserve.com/qDE1Ke')
    result = res.json()
    arr = [x for x in result['data'] if x['type'] == 'lifestyleshoes']
    return render(req, 'lifesty.html', context={"datarr": arr})


def walking(req):
    res = requests.get('https://api.jsonserve.com/qDE1Ke')
    result = res.json()
    arr = [x for x in result['data'] if x['type'] == 'walk']
    return render(req, 'walking.html', context={'datarr': arr})


def women(req):
    return render(req, 'women.html')


def womenstyle(req):
    res = requests.get('https://api.jsonserve.com/qDE1Ke')
    result = res.json()
    arr = [x for x in result['data'] if x['type'] == 'womensty']
    return render(req, 'womenstyle.html', context={'datarr': arr})


def womentrain(req):
    res = requests.get('https://api.jsonserve.com/qDE1Ke')
    result = res.json()
    arr = [x for x in result['data'] if x['type'] == 'trainw']
    return render(req, 'womentrain.html', context={'datarr': arr})


def womenwalk(req):
    res = requests.get('https://api.jsonserve.com/qDE1Ke')
    result = res.json()
    arr = [x for x in result['data'] if x['type'] == 'walkwo']
    return render(req, 'womenwalk.html', context={'datarr': arr})


def sandel(req):
    res = requests.get('https://api.jsonserve.com/qDE1Ke')
    result = res.json()
    arr = [x for x in result['data'] if x['type'] == 'sandel']
    return render(req, 'sandel.html', context={'datarr': arr})


def term(req):
    return render(req, 'term.html')


def refund(req):
    return render(req, 'refund.html')


def privacy(req):
    return render(req, 'privacy.html')


def kid(req):
    res = requests.get('https://api.jsonserve.com/qDE1Ke')
    result = res.json()
    arr = [x for x in result['data'] if x['type'] == 'kid']
    return render(req, 'kid.html', context={'datarr': arr})


def arrivals(req):
    res = requests.get('https://api.jsonserve.com/qDE1Ke')
    result = res.json()
    arr = [x for x in result['data'] if x['type'] == 'new']
    return render(req, 'arrivals.html', context={"datarr": arr})


def product(req, id):
    res = requests.get('https://api.jsonserve.com/qDE1Ke')
    result = res.json()
    arr = [x for x in result['data'] if x['id'] == id]
    return render(req, 'product.html', context={"dataarr": arr})


def login(req):
    if req.method == 'POST':
        email = req.POST['email']
        pwd = req.POST['password']
        user = models.Users.objects.all().filter(email=email, password=pwd)
        print(len(user))
        if len(user) == 1:
            return redirect('/', context={'user': user})
    return render(req, 'login.html')


def signup(req):
    if req.method == 'POST':
        user = req.POST['username']
        email = req.POST['email']
        pwd = req.POST['password']
        s1 = models.Users(username=user, email=email, password=pwd)
        s1.save()
        return redirect('/login')

    return render(req, 'signup.html')

