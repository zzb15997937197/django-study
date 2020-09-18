from django.contrib import admin

from polls.models import Student


# Register your models here.

class FlatPageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('url', 'title', 'content', 'sites')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('registration_required', 'template_name'),
        }),
    )


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday')
    search_fields = ('name',)


admin.site.register(Student, StudentAdmin)
