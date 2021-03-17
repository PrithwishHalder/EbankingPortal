from django.urls import path
from user import views

urlpatterns = [
    path('dash/', views.dashboard, name="usr_dashboard"),
    path('accounts/', views.transaction, name="usr_transaction"),
    path('transfer/', views.transfer, name="usr_transfer"),
    path('profile/', views.profile, name="usr_profile"),

]
