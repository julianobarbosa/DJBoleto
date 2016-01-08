from django.conf.urls import url, include
from django.contrib import admin
from djboleto.boleto.views import imagem_barras

urlpatterns = [
    url(r'imagem_barras/$', imagem_barras, name='imagem_barras')
]
