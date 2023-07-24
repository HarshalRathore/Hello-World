from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from binary_plan import models

admin.site.register(models.BinaryUserInstence, MPTTModelAdmin)

class BinaryTreeQueueAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'item',
    ]
    
admin.site.register(models.BinaryTreeQueue, BinaryTreeQueueAdmin)
admin.site.register(models.BinaryWallet)
admin.site.register(models.TransactionLog)