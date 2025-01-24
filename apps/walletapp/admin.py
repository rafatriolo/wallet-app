from django.contrib import admin
from .models import User, Wallet, Transfer


admin.site.register(User)
admin.site.register(Wallet)
admin.site.register(Transfer)
