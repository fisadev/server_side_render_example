from django.contrib import admin


from website.models import Visit


class VisitAdmin(admin.ModelAdmin):
    list_display = 'id', 'timestamp'


admin.site.register(Visit, VisitAdmin)
