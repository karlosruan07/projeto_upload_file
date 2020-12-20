
from django.shortcuts import render
from django.http import HttpResponse
from urllib import request #tem que importar para usar nos parâmetros
from .models import UploadFiles, Article # NÃO esquecer de importar as classe lá do modelo;


def teste(request):
    """
    docstring
    """
    return render(request, 'uploads/teste.html')

def uploads(request):
    arquivos = UploadFiles.objects.all()
    return render(request, 'uploads/uploads.html', {'arquivos':arquivos})

def year_archive(request):
    #return HttpResponse("<h1> Teste </h1>")
    arquivos = Article.objects.all()
    #context = {'year':year, 'article_list':a_list}
    return render(request, 'uploads/year_archive.html', {'arquivos':arquivos})
     
    
    
    