from django.contrib import admin

from .models import Main, Jobs, Languages


class MainAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'full_name'
    )
    ordering = ('-order',)


class JobsAdmin(admin.ModelAdmin):
    list_display = ('company', 'start', 'end', 'title')
    ordering = ('-order',)


class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    ordering = ('-order',)


admin.site.register(Main, MainAdmin)
admin.site.register(Jobs, JobsAdmin)
admin.site.register(Languages, LanguagesAdmin)
