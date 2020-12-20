
from django.urls import path
from . import views
from app_upload_file.views import uploads #aqui temos que importar as funções funçoes das views



urlpatterns = [
    #path('', views.post_list, name='post_list')
    path('uploads/', uploads)
]
