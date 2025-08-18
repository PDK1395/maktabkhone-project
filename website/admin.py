from django.contrib import admin
from website.models import Contact

@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','massage','created_date')
    search_fields = ('name',)
    list_filter = ('email',)