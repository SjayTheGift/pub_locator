from django.contrib import admin

from .models import PubInfo


class PubInfoAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'street_name',
                    'city',
                    'suburb',
                    'postal_code',
                    'contact_number',
                    'open_time',
                    'closing_time'
                    )
    list_filter = ("name",)
    search_fields = ['name', 'city', 'suburb', 'open_time']


admin.site.register(PubInfo, PubInfoAdmin)
