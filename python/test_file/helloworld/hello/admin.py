from django.contrib import admin
from hello.models import Kid

class KidAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex')
    ordering = ('id', )
    search_fields = ('name', 'sex')

# Register your models here.
admin.site.register(Kid, KidAdmin)

