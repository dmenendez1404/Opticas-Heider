"""optica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from articulo.views import Logout
from django.contrib.staticfiles.urls import static
from rest_framework.authtoken.views import ObtainAuthToken

from articulo import views as articulo_views
from articulo.apiRouters import router
from articulo.views import LoginView
from optica import settings
from proveedor import views as proveedor_views
from receta import views as receta_views
from venta import views as ventas_views
from compra import views as compras_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/login/', LoginView.as_view()),
    url(r'^api/logout/', Logout.as_view()),
    url(r'^$', articulo_views.index, name='index'),
    url(r'^almacen/$', articulo_views.articulos, name='almacen'),
    url(r'^lentes/$', articulo_views.lentes, name='lentes'),
    url(r'^addArticulo/$', articulo_views.addArticulo, name='addArticulo'),
    url(r'^accesorios/$', articulo_views.accesorios, name='accesorios'),
    url(r'^lentesContacto/$', articulo_views.lentesContacto, name='lentes_contacto'),
    url(r'^cristalesGraduados/$', articulo_views.cristalesGraduados, name='cristales_graduados'),
    url(r'^gafaSol/$', articulo_views.gafaSol, name='gafas_sol'),
    url(r'^recetas/$', receta_views.recetas, name='recetas'),
    url(r'^recetas/pdf/$', receta_views.pdf_receta, name='pdf_recetas'),
    url(r'^proveedores/$', proveedor_views.proveedores, name='proveedores'),
    url(r'^addVenta/$', ventas_views.addVentas, name='addVentas'),
    url(r'^ventas/$', ventas_views.ventas, name='ventas'),
    url(r'^addCompra/$', compras_views.addCompra, name='addCompra'),
    url(r'^compras/$', compras_views.compras, name='compras'),
    url(r'^addLente/$', compras_views.addLente, name='addLente'),
    url(r'^graficos/$', articulo_views.graficos, name='graficos')

    #url(r'^images/$', proveedor_views.ImageView.as_view(), name='file-upload')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
