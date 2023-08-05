from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
  list_display = ("name", "surname", "ticket_number")
  
admin.site.register(Ticket, TicketAdmin)