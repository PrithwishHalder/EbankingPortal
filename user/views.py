from django.shortcuts import render, redirect
from .models import User


# Create your views here.


def dashboard(request, id):
    context = {}
    user = User.objects.get(id=id)
    context['data'] = user
    # # for i in context:
    # print(context['data'].password)

    return render(request, 'dashboard.html', context)


def transaction(request, id):
    context = {}
    user = User.objects.get(id=id)
    context['data'] = user

    return render(request, 'transaction.html', context)


def transfer(request, id):
    context = {}
    user = User.objects.get(id=id)
    context['data'] = user

    return render(request, 'transfer.html', context)


def profile(request, id):
    context = {}
    user = User.objects.get(id=id)
    context['data'] = user

    return render(request, 'profile.html', context)


def logout(request):
    try:
        del request.session['id']
    except:
        pass
    return redirect("home")
