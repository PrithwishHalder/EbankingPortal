from django.shortcuts import render, redirect
from user.models import User, Transaction
from .models import Clerk

# Create your views here.


def clrk_dashboard(request, id):

    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "cdashboard.html", {})
        else:
            return redirect('clerk')


def clrk_adduser(request, id):
    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "adduser.html", {})
        else:
            return redirect('clerk')


def clrk_searchUser(request, id):
    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "searchuser.html", {})
        else:
            return redirect('clerk')


def clrk_updateUser(request, id):
    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "updateuser.html", {})
        else:
            return redirect('clerk')


def clrk_userTransaction(request, id):
    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "usertransaction.html", {})
        else:
            return redirect('clerk')


def clrk_ajaxTransaction(request, accno):

    context = {}

    tran = list(Transaction.objects.filter(accountno=accno))
    if tran:
        context['trans'] = tran
    else:
        context['transerror'] = "Account No Invalid!"

    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "ajaxtransaction.html", context)
        else:
            return redirect('clerk')


def clrk_Withdrawl(request, id):
    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "cashwithdrawl.html", {})
        else:
            return redirect('clerk')


def clrk_Deposit(request, id):
    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "deposit.html", {})
        else:
            return redirect('clerk')


def clrk_Transfer(request, id):
    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "moneytransfer.html", {})
        else:
            return redirect('clerk')


def clrkprofile(request, id):

    context = {}

    clerk = Clerk.objects.get(id=id)
    context['data'] = clerk

    if request.method == 'POST':
        opass = request.POST['opassword']
        npass = request.POST['npassword']
        cpass = request.POST['cpassword']
        if npass == cpass:
            try:
                clerk = Clerk.objects.get(id=id, password=opass)
            except:
                context['profilemsg'] = "Old Password did not match!"
            else:
                clerk.password = npass
                clerk.save()
                context['profilemsg'] = "Password Changed!"
        else:
            context['profilemsg'] = "New Password did not match!"

        return render(request, "clerkprofile.html", context)

    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "clerkprofile.html", context)
        else:
            return redirect('clerk')


def clogout(request):
    try:
        del request.session['clerkid']
    except:
        pass
    return redirect("home")
