from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("start_date", "occupation")
    # minus means reverse ordering (Z -> A)
    ordering = ("-first_name", )
    readonly_fields = ("occupation", )


admin.site.register(Form, FormAdmin)
