from django.urls import path, include
from clerk import views
urlpatterns = [

    path('clrk/<id>', views.clrk_dashboard, name="clrk_dashboard"),
    path('clrklogout/', views.clogout, name="clogout"),

]
