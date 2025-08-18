from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ("title",'content',)
    list_display = ('title','content','status','counted_view','published_date','created_date','updated_date')
    list_filter = ('status',)
    #ordering = ['-created_date'] # - poshtesh baes mishe baraks beshe 
    search_fields = ['title','content']

# admin.site.register(Post)
