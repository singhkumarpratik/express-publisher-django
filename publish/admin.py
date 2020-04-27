from django.contrib import admin
from .models import *
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','body','time')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(express_publish, PostAdmin)