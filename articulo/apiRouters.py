from articulo import views as articulo_views
from receta import views as receta_views
from proveedor import views as proveedor_views
from venta import views as venta_views
from compra import views as compra_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articulo', articulo_views.ArticulosViewSet)
router.register(r'accesorios', articulo_views.AccesoriosViewSet)
router.register(r'sucursales', articulo_views.SucursalViewSet)
router.register(r'lentes', articulo_views.EspejueloViewSet)
router.register(r'lentescontacto', articulo_views.LentesContactoViewSet)
router.register(r'gafasol', articulo_views.GafaSolViewSet)
router.register(r'cristalesgraduados', articulo_views.CristalesGraduadosViewSet)
router.register(r'colores', articulo_views.ColorViewSet)
router.register(r'tipoarmadura',articulo_views.TipoArmazonViewSet)
router.register(r'tipomontura', articulo_views.TipoMonturaViewSet)
router.register(r'marca', articulo_views.MarcaViewSet)
router.register(r'modelo', articulo_views.ModeloViewSet)
router.register(r'materialarmadura', articulo_views.MaterialArmaduraViewSet)
router.register(r'medicion', articulo_views.MedicionViewSet)
router.register(r'materialcristal', articulo_views.MaterialCristalViewSet)
router.register(r'tratamientocristal',articulo_views.TratamientoCristalViewSet)
router.register(r'materialsol', articulo_views.MaterialSolViewSet)
router.register(r'user', receta_views.UserViewSet)
router.register(r'cliente', receta_views.ClienteViewSet)
router.register(r'doctor', receta_views.DoctorViewSet)
router.register(r'receta', receta_views.RecetaViewSet)
router.register(r'proveedor', proveedor_views.ProveedorViewSet)
router.register(r'venta', venta_views.VentaViewSet)
router.register(r'compra', compra_views.CompraViewSet)