from django.contrib import admin

# Register your models here.
from .models import Box, Dvd, Type_of

# class BoxInLine(admin.StackedInline):
#     model = Dvd
#
#
# class DvdAdmin(admin.ModelAdmin):
#     inlines = [BoxInLine,]


admin.site.register(Dvd)
admin.site.register(Box)
admin.site.register(Type_of)
