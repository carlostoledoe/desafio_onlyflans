from django.contrib import admin
from web.models import Flan

# Register your models here.
class FlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(Flan, FlanAdmin)