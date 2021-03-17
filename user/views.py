from django.shortcuts import render


# Create your views here.


def dashboard(request):

    return render(request, 'dashboard.html', {})


def transaction(request):
    return render(request, 'transaction.html', {})


def transfer(request):
    return render(request, 'transfer.html', {})


def profile(request):
    return render(request, 'profile.html', {})
