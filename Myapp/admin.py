from django.contrib import admin

# Register your models here.
from Myapp.models import USERPASS,Signup,Resturant

admin.site.register(USERPASS)
admin.site.register(Signup)
admin.site.register(Resturant)