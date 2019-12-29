from django.contrib import admin

# Register your models here.
from .models import cateType,UserInfo


class AreaAdmin(admin.ModelAdmin):
    list_display = ['id','name',"phone","is_default","type"]
    list_filter = ["is_default","type"]
    search_fields = ('name', 'phone')

class AreaCate(admin.ModelAdmin):
    list_display = ['id', 'cate', "desc", "count","index"]

admin.site.register(cateType,AreaCate)
admin.site.register(UserInfo,AreaAdmin)