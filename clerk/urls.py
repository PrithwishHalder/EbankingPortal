from django.urls import path, include
from clerk import views
urlpatterns = [

    path('clrk/', views.clrk_dashboard, name="clrk_dashboard"),

]
