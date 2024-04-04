from django.contrib import admin
from .models import Registar1, User, Report_1
# Register your models here.




class CallAllModelsAdmin(admin.ModelAdmin):
    list_display = ("id_number", "last_name", "b_year", "create_date")

class CallUserModelsAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "password")

class CallRiport1ModelsAdmin(admin.ModelAdmin):
    list_display = ("teacher", "student_name", "year_of_report")

#class call_all_models(admin.ModelAdmin):
#    list_display = ("id_number","last_name","b_year","create_date",)


#class call_user_models(admin.ModelAdmin):
#    list_display = ("username","email", "password")

admin.site.register(Report_1, CallRiport1ModelsAdmin)
admin.site.register(Registar1, CallAllModelsAdmin)
admin.site.register(User, CallUserModelsAdmin)


