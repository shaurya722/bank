# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from multiprocessing.connection import Client

from django.contrib import admin
from .models import (
    Account,
    Branch,
    Bank,
    ClientManager,
    Deposit,
    Transfer,
    Withdraw,
    Client
)

# Register your models here.
admin.site.register(Branch)
admin.site.register(Bank)
admin.site.register(ClientManager)
admin.site.register(Client)
admin.site.register(Account)
admin.site.register(Transfer)
admin.site.register(Withdraw)
admin.site.register(Deposit)


