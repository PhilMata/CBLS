from django.contrib import admin
from .models import User, Agent, Lead
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [ 'username', 'email']

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = [ 'user']

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = [ 'first_name', 'last_name']