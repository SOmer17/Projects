from django.contrib import admin
from .models import Students,Contact_Info,Address

admin.site.register(Students)
# admin.site.register(Names)
admin.site.register(Contact_Info)
admin.site.register(Address)

# Register your models here.
