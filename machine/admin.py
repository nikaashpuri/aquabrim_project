from django.contrib import admin
from machine.models import Transmitter, Controller, Command
# Register your models here.

class TransmitterAdmin(admin.ModelAdmin):
    list_display = ['device_id']


class CommandAdmin(admin.ModelAdmin):
    list_display = ['name', 'electronic_format']

admin.site.register(Transmitter, TransmitterAdmin)
admin.site.register(Command, CommandAdmin)
admin.site.register(Controller, TransmitterAdmin)
