from django.conf.urls import patterns, url

from oob import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),

    url(r'^demande/$', views.demande, name='demande'),

    url(r'^resultat/(?P<ticket_id>\d+)$', views.resultat, name='resultat'),

    url(r'^traitement_de_demande/$', views.traitement_de_demande, name='traitement_de_demande'))





    #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),

    #url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),

    #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
