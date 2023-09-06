from django.contrib import admin
from tabledata.models import tabledata
from tabledata.models import passouts
from tabledata.models import fee
from tabledata.models import feetable
# Register your models here.
class tabledataAdmin(admin.ModelAdmin):
    list_display=('regno','name','fname','mname','phone_no','address','city','gender','course','btime','photo','fee','remfee')

admin.site.register(tabledata,tabledataAdmin)

class passoutsAdmin(admin.ModelAdmin):
    list_display=('regno','name','fname','mname','phone_no','address','city','gender','course','btime','photo','fee','remfee')

admin.site.register(passouts,passoutsAdmin)

class feeAdmin(admin.ModelAdmin):
    list_display=('regno','fee','date')

admin.site.register(fee,feeAdmin)

class feetableAdmin(admin.ModelAdmin):
    list_display=('regno','rem','totalfee','fee','date')

admin.site.register(feetable,feetableAdmin)