# Register your models here.

from django.contrib import admin
from .models import Chat , Thread , Forum


#register the models to the admin

admin.site.register(Chat)
admin.site.register(Thread)
admin.site.register(Forum)
