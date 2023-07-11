from django.contrib import admin
from .models import *

class UserWithRoleAdmin(admin.ModelAdmin):
    list_filter=("role","gender")
    
# Register your models here.
admin.site.register(Company)
admin.site.register(Candidates)
admin.site.register(UserWithRole,UserWithRoleAdmin)
admin.site.enable_nav_sidebar =False