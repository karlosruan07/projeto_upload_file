from django.contrib import admin
from .models import UploadFiles, Reporter, Article #Não esquecer de importar os modelos aqui
# Register your models here.
admin.site.register(UploadFiles)
admin.site.register(Reporter)
admin.site.register(Article)

