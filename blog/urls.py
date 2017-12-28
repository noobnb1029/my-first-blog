from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list), #si esta vacia, se asigna el view de la lista de posts a la pagina de inicio
]
