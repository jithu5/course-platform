from django.contrib import admin

# Register your models here.
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ['title','description','image','access','status','display_image'],
    list_display = ['title','description','image','access','status']
    list_filter = ['access','status']
    readonly_fields=['display_image']


    def display_image(self,obj,*args,**kwargs):
        print(obj)

admin.site.register(Course)