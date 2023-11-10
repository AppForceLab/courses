from django.contrib import admin
from . import models

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My courses"
admin.site.index_title = "Welcome to the Courses admin area"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)
# Register your models here.
