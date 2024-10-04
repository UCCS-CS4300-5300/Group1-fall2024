from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

# Register your models here.
# For customizing the admin site
class MyAdminSite(admin.AdminSite):
    site_header = 'CookApp Administration'
    site_title = 'CookApp Admin'
    index_title = 'CookApp Admin'

admin_site = MyAdminSite(name='admin')

# register the models with the admin site
admin_site.register(User, UserAdmin)

admin_site.register(Group, GroupAdmin)
