from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'altec.views.home', name='home'),
    # url(r'^altec/', include('altec.foo.urls')),
   	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','Principal.views.inicio'),
    url(r'^listar_cliente/','Principal.views.listar_cliente'),
    url(r'^listar_empleado/','Principal.views.listar_empleado'),
    url(r'^listar_os/','Principal.views.listar_os'),
    url(r'^busca_os/','Principal.views.busca_os'),
    url(r'^busca_cliente/','Principal.views.busca_cliente'),
    url(r'^busca_tecnico/','Principal.views.busca_tecnico'),

    url(r'^imprimir_os/','Principal.views.imprimir_os'),

    url(r'^rellena_campo/','Principal.views.rellena_campo'),
    url(r'^autobusqueda/','Principal.views.autobusqueda'),
    url(r'^autobusqueda_c/','Principal.views.autobusqueda_c'),
    url(r'^autobusqueda_e/','Principal.views.autobusqueda_e'),


    url(r'^guardar_cliente/','Principal.views.guardar_cliente'),
    url(r'^guardar_tecnico/','Principal.views.guardar_tecnico'),
    url(r'^guardar_os/','Principal.views.guardar_os'),
    url(r'^actualizar_os/','Principal.views.actualizar_os'),
    url(r'^actualizar_cliente/','Principal.views.actualizar_cliente'),
    url(r'^actualizar_tecnico/','Principal.views.actualizar_tecnico'),
    


    url(r'^autocom/','Principal.views.autocom'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^(?P<nombre>[a-z0-9A-Z_\-]*.pdf)$','Principal.views.descargarpdf'),

    #url(r'media/(?P<path>.*)','django.views.static.serve',
        #{'document_root':settings.MEDIA_ROOT}),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
