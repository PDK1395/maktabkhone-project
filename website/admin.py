from django.contrib import admin
from website.models import Contact , NewsLetter

@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message','created_date')
    search_fields = ('name',)
    list_filter = ('email',)
    
@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)
    list_filter = ('email',)