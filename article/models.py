from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE, verbose_name= "Yazar")
    titles = models.CharField(max_length=50,verbose_name="Başlık")
    # content = models.TextField(verbose_name="İçerik")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.titles
    