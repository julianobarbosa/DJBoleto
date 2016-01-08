#-*- coding: utf8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import djboleto.boleto.urls as boleto_urls
import djboleto.boleto.views as boleto_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Este include é necessário!
    url(r'^boleto/', include(boleto_urls)),

    # Estes são includes para views de teste, não devem estar numa aplicação real
    url(r'^boleto_bb/$', boleto_views.boleto_bb),
    url(r'^boleto_caixa/$', boleto_views.boleto_caixa),
    url(r'^boleto_real/$', boleto_views.boleto_real),
    url(r'^boleto_bradesco/$', boleto_views.boleto_bradesco),
]

urlpatterns += staticfiles_urlpatterns()
