from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from .models import Ingredient, Recipe, UserPreference

# For customizing the admin site
class MyAdminSite(admin.AdminSite):
    site_header = 'CookApp Administration'
    site_title = 'CookApp Admin'
    index_title = 'CookApp Admin'

admin_site = MyAdminSite(name='admin')

# Register the models with the custom admin site
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Ingredient)
admin_site.register(Recipe)
admin_site.register(UserPreference)