from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('^$', views.index, name='index'),

    # 1.- vista detalle de una obra
    re_path(r'^obra/(?P<obra_id>\d+)/$',
            views.obra, name='detalle_obra'),

    # 2.- buscador
    re_path(r'^search/$', views.search, name='search'),

    # 3.- resultados de la búsqueda
    re_path(r'^search_result/$', views.search_result, name="search_result"),

    # 4.- listado de toda la BD (sin parámetros de búsqueda)
    re_path(r'^listado/$', views.listado, name="listado"),

    # 5.- "acerca de", página estática
    re_path(r'^acerca/$', views.acerca, name='acerca'),

]
