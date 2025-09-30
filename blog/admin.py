from django.contrib import admin
from blog.models import Post , Category , Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ("title",'content',)
    list_display = ('title','content','author','status','login_required','counted_view','published_date','created_date','updated_date')
    list_filter = ('status','author')
    #ordering = ['-created_date'] # - poshtesh baes mishe baraks beshe 
    search_fields = ['title','content']
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('post','name','email','subject','message','approved','created_date','updated_date')
    list_filter = ('approved','created_date')
    search_fields = ['title','content']


# admin.site.register(Post)
admin.site.register(Category)

