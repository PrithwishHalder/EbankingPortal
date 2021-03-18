from django.shortcuts import render, redirect
from .models import User, Transaction


# Create your views here.


def dashboard(request, id):
    context = {}
    try:
        user = User.objects.get(id=id)
        context['data'] = user
    except:
        pass

    if request.method == 'GET':
        if request.session.has_key('userid'):
            return render(request, 'dashboard.html', context)
        else:
            return redirect('user')


def transaction(request, id):
    context = {}
    try:
        user = User.objects.get(id=id)
        context['data'] = user
    except:
        pass

    try:
        tran = list(Transaction.objects.filter(accountno=user.acc_no))
    except:
        pass
    else:
        context['trans'] = tran

    if request.method == 'GET':
        if request.session.has_key('userid'):
            return render(request, 'transaction.html', context)
        else:
            return redirect('user')


def transfer(request, id):
    context = {}
    try:
        user = User.objects.get(id=id)
        context['data'] = user
    except:
        pass

    if request.method == 'POST':
        accno = request.POST['account']
        name = request.POST['name']
        amount = int(request.POST['amount'])
        reason = request.POST['reason']

        if user.balance > (amount+500) and user.acc_no != accno:
            try:
                benif = User.objects.get(acc_no=accno, fullname=name)
            except:
                context['transfermsg'] = "Benifitiary Account Not Found!"
                return render(request, 'transfer.html', context)
            else:
                obj1 = Transaction()
                obj2 = Transaction()

                user_bal = user.balance-amount
                benif_bal = benif.balance+amount

                user.balance = user_bal
                user.save()

                benif.balance = benif_bal
                benif.save()

                uinfo = reason + " to " + name
                binfo = reason + " from " + user.fullname

                obj1.accountno = user.acc_no
                obj1.info = uinfo
                obj1.credit = 0
                obj1.debit = amount
                obj1.balance = user_bal
                obj1.save()

                obj2.accountno = benif.acc_no
                obj2.info = binfo
                obj2.credit = amount
                obj2.debit = 0
                obj2.balance = benif_bal
                obj2.save()

                print(uinfo, binfo)
                context['transfermsg'] = "Transfer Sucessfull!"
                return render(request, 'transfer.html', context)
        else:
            if user.acc_no == accno:
                context['transfermsg'] = "Self Transfer Not Possible!"
            else:
                context['transfermsg'] = "Inssuficient Fund!"
        return render(request, 'transfer.html', context)

    if request.method == 'GET':
        context['transfermsg'] = ""
        if request.session.has_key('userid'):
            return render(request, 'transfer.html', context)
        else:
            return redirect('user')


def profile(request, id):
    context = {}
    try:
        user = User.objects.get(id=id)
        context['data'] = user
    except:
        pass

    if request.method == 'POST':
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']

        user.email = email
        user.mobile = mobile
        user.address = address
        user.save()
        context['profilemsg'] = "Profile Updated!"
        return render(request, 'profile.html', context)

    if request.method == 'GET':
        context['profilemsg'] = ""
        if request.session.has_key('userid'):
            return render(request, 'profile.html', context)
        else:
            return redirect('user')


def logout(request):
    try:
        del request.session['userid']
    except:
        pass
    return redirect("home")
