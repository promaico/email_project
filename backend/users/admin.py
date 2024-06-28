from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, EmailAccount
from .forms import CustomUserChangeForm, CustomUserCreationForm, EmailAccountCreationForm

class EmailAccountAdminInline(admin.TabularInline):
    model = EmailAccount
    

class EmailAccountAdmin(admin.ModelAdmin):
    model = EmailAccount
    add_form = EmailAccountCreationForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    inlines = (EmailAccountAdminInline, )
    
admin.site.register(EmailAccount)
