from django.db import models
from django.utils import timezone

# Create your models here.
class UploadFiles(models.Model):
    data_criacao = models.DateTimeField(default=timezone.now)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    
    
class Reporter(models.Model):
    full_name = models.CharField(max_length=70) #nome completo do autor
    
    def __str__(self):
        return self.full_name #retorna o nome dos autores em uma string
    

class Article(models.Model):
    pub_date = models.DateField() #Pega a data da publicação
    headline = models.CharField(max_length= 200) #Pega o titulo da postagem
    content = models.TextField() #Pega o conteudo da postagem
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE) #Trata da chave estrageira

    def __str__(self):
        return self.headline
    
    