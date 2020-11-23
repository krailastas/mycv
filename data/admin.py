from django.contrib import admin

from .models import Main, Jobs


class MainAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'full_name'
    )
    ordering = ('id',)


class JobsAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'start', 'end', 'title')
    ordering = ('id',)


admin.site.register(Main, MainAdmin)
admin.site.register(Jobs, JobsAdmin)
