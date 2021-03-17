from django.shortcuts import render, redirect
from clerk.models import Clerk
from user.models import User

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def user(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')

        try:
            user_l = User.objects.get(username=username, password=password)
        except Exception:
            context['error'] = "Login Failed!"
            return render(request, 'user.html', context)
        else:
            context = user_l
            if user_l is not None:
                # login(request, username)
                return redirect("usr_dashboard")

    return render(request, 'user.html', context)


def clerk(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('clerk')
        password = request.POST.get('password')

        try:
            user_l = Clerk.objects.get(username=username, password=password)
        except Exception:
            context['error'] = "Login Failed!"
            return render(request, 'user.html', context)
        else:
            # context = user_l
            if user_l is not None:
                print("y")
                # login(request, username)
                return redirect("clrk_dashboard")

    return render(request, 'clerk.html', context)
