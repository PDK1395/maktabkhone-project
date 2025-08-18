from django.db import models

class Post(models.Model):
    #author
    #image
    title = models.CharField(max_length=255)
    content = models.TextField()
    # category 
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