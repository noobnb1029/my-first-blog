from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list), #si esta vacia, se asigna el view de la lista de posts a la pagina de inicio
	url (r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name ='post_detail'), #<pk> significa que se tomara el numero  de post y se pasara como parametro a la view de post_detail (la variable se llamara pk)
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

]