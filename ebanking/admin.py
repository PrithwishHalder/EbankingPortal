from django.contrib import admin

from clerk.models import Clerk
from user.models import User

# Register your models here.
admin.site.register(Clerk)
admin.site.register(User)
