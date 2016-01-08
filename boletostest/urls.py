#-*- coding: utf8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import djboleto.boleto.urls
import djboleto.boleto.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Este include é necessário!
    url(r'^boleto/', include(djboleto.boleto.urls)),

    # Estes são includes para views de teste, não devem estar numa aplicação real
    url(r'^boleto_bb/$', djboleto.boleto.views.boleto_bb),
    url(r'^boleto_itau/$', djboleto.boleto.views.boleto_itau),
    url(r'^boleto_caixa/$', djboleto.boleto.views.boleto_caixa),
    url(r'^boleto_real/$', djboleto.boleto.views.boleto_real),
    url(r'^boleto_bradesco/$', djboleto.boleto.views.boleto_bradesco),
]

urlpatterns += staticfiles_urlpatterns()
