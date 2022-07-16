from django.contrib import admin
from django.urls import path, include 

from App_Coder.views import curso, entregable, estudiante, profesor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app-coder/', include('App_Coder.urls')),
]
