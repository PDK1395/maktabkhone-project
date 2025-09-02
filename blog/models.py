from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    author = models.ForeignKey(User,on_delete= models.SET_NULL , null=True) # inja age beja ( set_null ) mizashtim ( CASCADE ) kole post haye oon fard ham pak mikard vaghty oon fard acc ro delete mikard 
    image = models.ImageField(upload_to='blog/' , default= 'blog/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category) # inja null ya default nazashtim chon django mige midonam mitone null ham bashe pas dast nemizanim
    # tags
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True) # 
    

# in modele neveshtan to sql hast bara gereftan tamam dade haye mojod    
# SELECT * FROM Post
# SELECT * FROM Post WHERE status = 1

    class Meta:
        ordering = ['-created_date']
#        verbose_name = 'پست'
#        verbose_name_plural = 'پست ها'
        
    def __str__(self):
        return " {} - {} ".format(self.title , self.id)
    
