from django.contrib import admin
from .models import Transaction
# Register your models here.


#admin.site.register(Transaction)
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    
    list_display = ('reason', 'price', 'Necessary')
    list_filter = ('reason', 'price')
    search_fields = ('reason', 'price')