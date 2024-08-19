from django.contrib import admin

from .models import Bb, Rubric


# Register your models here.
class BbAdmin(admin.ModelAdmin):
    list_display = ( 'rubric', 'title', 'content', 'price', 'published')
    list_display_links = ('title', 'rubric', 'content')
    search_fields = ('title', 'content')



admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
