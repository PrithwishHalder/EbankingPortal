from django.urls import path, include
from clerk import views
urlpatterns = [

    path('clrk/<id>', views.clrk_dashboard, name="clrk_dashboard"),
    path('clrk_addUser/<id>', views.clrk_adduser, name="addUser"),
    path('clrk_searchUser/<id>', views.clrk_searchUser, name="searchUser"),
    path('ajaxSearch/<accno>', views.ajaxSearch, name="ajaxSearch"),
    path('clrk_updateUser/<id>', views.clrk_updateUser, name="updateUser"),
    path('ajaxUpdate/<accno>', views.ajaxUpdate, name="ajaxUpdate"),
    path('clrk_userTransaction/<id>',
         views.clrk_userTransaction, name="userTransaction"),
    path('ajaxTransaction/<accno>',
         views.clrk_ajaxTransaction, name="ajaxTransaction"),
    path('clrk_Withdrawl/<id>', views.clrk_Withdrawl, name="clrkWithdrawl"),
    path('ajaxWithdraw/<accno>', views.ajaxWithdraw, name="ajaxWithdraw"),
    path('clrk_Deposit/<id>', views.clrk_Deposit, name="clrkDeposit"),
    path('ajaxDeposit/<accno>', views.ajaxDeposit, name="ajaxDeposit"),
    path('clrk_Transfer/<id>', views.clrk_Transfer, name="clrkTransfer"),
    path('sender/<accno>', views.sender, name="sender"),
    path('reciever/<accno>', views.reciever, name="reciever"),
    path('clrkprofile/<id>', views.clrkprofile, name="cprofile"),
    path('clrklogout/', views.clogout, name="clogout"),

]
