from django.shortcuts import render, redirect
from user.models import User, Transaction
from .models import Clerk

# Create your views here.


def user(accno):
    user = User.objects.get(acc_no=accno)
    return user


def clrk_dashboard(request, id):

    context = {}

    if request.method == 'GET':
        if request.session.has_key('clerkid'):

            # id = request.session['clerkid']
            # clerk = Clerk.objects.get(id=id)
            # context['clerk'] = clerk

            # userCount = User.objects.count()
            # transCount = Transaction.objects.count()
            # print(userCount, transCount)

            return render(request, "cdashboard.html", {})
        else:
            return redirect('clerk')


def clrk_adduser(request, id):

    flag = 1
    context = {}

    if request.method == 'POST':
        name = request.POST['name']
        uname = request.POST['uname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        password = request.POST['password']
        accType = request.POST['accType']
        amount = request.POST['amount']

        if User.objects.filter(username=uname).exists():
            flag = 0
            context['unameerror'] = "Username Already Exists"

        if User.objects.filter(email=email).exists():
            flag = 0
            context['emailerror'] = "Email Already Exists"

        if User.objects.filter(mobile=mobile).exists():
            flag = 0
            context['mobileerror'] = "Mobile No. Already Exists"

        if flag:
            last = User.objects.last()
            accno = str(int(last.acc_no) + 1)

            tran = Transaction()
            tran.info = "Opening Balance Deposit"
            tran.accountno = accno
            tran.credit = amount
            tran.debit = 0
            tran.balance = amount
            tran.save()

            nuser = User()
            nuser.fullname = name
            nuser.username = uname
            nuser.email = email
            nuser.mobile = mobile
            nuser.address = address
            nuser.password = password
            nuser.acc_type = accType
            nuser.balance = amount
            nuser.acc_no = accno

            nuser.save()
            context['success'] = "User Registered!"

        return render(request, "adduser.html", context)

    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "adduser.html", context)
        else:
            return redirect('clerk')


def clrk_searchUser(request, id):
    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "searchuser.html", {})
        else:
            return redirect('clerk')


def ajaxSearch(request, accno):
    context = {}

    user = User.objects.get(acc_no=accno)
    context['data'] = user

    if request.method == 'GET':

        return render(request, 'ajaxsearch.html', context)


def clrk_updateUser(request, id):

    context = {}

    if request.method == "POST":
        address = request.POST['address']
        email = request.POST['email']
        mobile = request.POST['mobile']
        uname = request.POST['uname']
        password = request.POST['password']
        accno = request.POST['accno']

        user = User.objects.get(acc_no=accno)
        user.address = address
        user.email = email
        user.mobile = mobile
        user.username = uname
        user.password = password
        user.save()

        context['success'] = "Update Successful!"

        return render(request, 'updateuser.html', context)

    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "updateuser.html", context)
        else:
            return redirect('clerk')


def ajaxUpdate(request, accno):

    context = {}

    user = User.objects.get(acc_no=accno)
    context['data'] = user

    if request.method == 'GET':

        return render(request, 'ajaxupdate.html', context)


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

    context = {}
    if request.method == 'POST':

        accno = request.POST['accno']
        amount = request.POST['amount']
        try:
            user = User.objects.get(acc_no=accno)
        except:
            context['message'] = "Invalid Account Number!"
        else:
            bal = user.balance-int(amount)
            user.balance = bal
            user.save()

            trans = Transaction()
            trans.accountno = accno
            trans.info = "Withdraw from Bank"
            trans.credit = amount
            trans.debit = 0
            trans.balance = bal
            trans.save()
            context['message'] = "Money Withdrawn!"

        return render(request, "cashwithdrawl.html", context)

    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "cashwithdrawl.html", context)
        else:
            return redirect('clerk')


def ajaxWithdraw(request, accno):

    context = {}

    user = User.objects.get(acc_no=accno)
    context['data'] = user

    if request.method == "GET":
        return render(request, "ajaxwithdraw.html", context)


def ajaxDeposit(request, accno):

    context = {}

    user = User.objects.get(acc_no=accno)
    context['data'] = user

    if request.method == "GET":
        return render(request, "ajaxdeposit.html", context)


def clrk_Deposit(request, id):

    context = {}
    if request.method == 'POST':

        accno = request.POST['accno']
        amount = request.POST['amount']
        try:
            user = User.objects.get(acc_no=accno)
        except:
            context['message'] = "Invalid Account Number!"
        else:
            bal = user.balance+int(amount)
            user.balance = bal
            user.save()

            trans = Transaction()
            trans.accountno = accno
            trans.info = "Deposit to Bank"
            trans.credit = 0
            trans.debit = amount
            trans.balance = bal
            trans.save()
            context['message'] = "Money Deposited!"

        return render(request, "deposit.html", context)

    if request.method == 'GET':
        if request.session.has_key('clerkid'):
            return render(request, "deposit.html", context)
        else:
            return redirect('clerk')


def clrk_Transfer(request, id):

    if request.method == 'POST':
        saccno = request.POST['saccno']
        raccno = request.POST['raccno']
        amount = request.POST['amount']
        reason = request.POST['reason']

        print(saccno, raccno, amount, reason)

        return render(request, "moneytransfer.html", {})

    if request.method == 'GET':
        if request.method == 'POST':
            saccno = request.POST['saccno']
            raccno = request.POST['raccno']
            amount = request.POST['amount']
            reason = request.POST['reason']

            print(saccno, raccno, amount, reason)

            return render(request, "moneytransfer.html", {})

        if request.session.has_key('clerkid'):
            return render(request, "moneytransfer.html", {})
        else:
            return redirect('clerk')


def sender(request, accno):

    context = {}

    context['sender'] = user(accno)

    return render(request, "fetchsender.html", context)


def reciever(request, accno):

    context = {}

    context['reciever'] = user(accno)

    return render(request, "fetchreciever.html", context)


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
