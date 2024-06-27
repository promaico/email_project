from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, EmailAccount

class EmailAccountAdminInline(admin.TabularInline):
    model = EmailAccount
    

class EmailAccountAdmin(admin.ModelAdmin):
    model = EmailAccount
    

class UserAdmin(BaseUserAdmin):
    inlines = (EmailAccountAdminInline, )
    
admin.site.register(EmailAccount)
admin.site.register(User, UserAdmin)