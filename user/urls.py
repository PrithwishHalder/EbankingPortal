from django.urls import path
from user import views

urlpatterns = [
    path('dash/<id>', views.dashboard, name="usr_dashboard"),
    path('accounts/<id>', views.transaction, name="usr_transaction"),
    path('transfer/<id>', views.transfer, name="usr_transfer"),
    path('profile/<id>', views.profile, name="usr_profile"),

]
