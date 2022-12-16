from django.contrib import admin
from .models import Demo
# Register your models here.
@admin.register(Demo)
class DemoModel(admin.ModelAdmin):
    pass
#    list_display=['id','unm','pwd','nm']


