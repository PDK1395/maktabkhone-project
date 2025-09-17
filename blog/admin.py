from django.contrib import admin
from blog.models import Post , Category
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ("title",'content',)
    list_display = ('title','content','author','status','counted_view','published_date','created_date','updated_date')
    list_filter = ('status','author')
    #ordering = ['-created_date'] # - poshtesh baes mishe baraks beshe 
    search_fields = ['title','content']
    summernote_fields = ('content',)

# admin.site.register(Post)
admin.site.register(Category)