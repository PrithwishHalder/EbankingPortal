from django.shortcuts import render, redirect

# Create your views here.


def clrk_dashboard(request, id):
    return render(request, "cdashboard.html", {})


def clogout(request):
    try:
        del request.session['clerkid']
    except:
        pass
    return redirect("home")
