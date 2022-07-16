from django.contrib import admin
from django.urls import path

from App_Coder.views import curso, entregable, estudiante, profesor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agrega-curso/<nombre>/<camada>', curso),
    path('agrega-estudiante/<nombre>/<apellido>/<email>', estudiante),
    path('agrega-profesor/<nombre>/<apellido>/<email>/<profesion>', profesor),
    path('agrega-entregable/<nombre>/<fechaDeEntrega>/<entregado>', entregable),
]
