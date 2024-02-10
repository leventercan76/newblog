from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE, verbose_name= "Yazar")
    titles = models.CharField(max_length=50,verbose_name="Başlık")
    # content = models.TextField(verbose_name="İçerik")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank=True,null=True,verbose_name="Makale Fotoğrafı")
    def __str__(self):
        return self.titles
    
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name="Makale", related_name = "comments")
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateField(auto_now_add=True,verbose_name="Yorum Tarihi")
    def __str__(self):
        return self.comment_content
    class Meta: #Sıralama için meta classı gerekiyor
        ordering = ['-comment_date']