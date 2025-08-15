from sys import path_hooks
from django.contrib import admin
from django.urls import path
from front import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('resultados-da-busca', views.search_results, name='search_results'),
    path('detalhes-do-imovel', views.property_details, name='property_details'),
    path('anunciar-imovel', views.ad_register, name='ad_register'),
    path('login', views.login, name='login'),
    path('esqueci-minha-senha', views.forgot_password, name='forgot_password'),
    path('redefinir-senha', views.reset_password, name='reset_password'),
    # Backoffice
    path('backoffice', views.backoffice_main, name='backoffice_main'),
    path('backoffice/editar', views.backoffice_edit, name='backoffice_edit'),
    path('backoffice/adicionar', views.backoffice_add, name='backoffice_add'),
]
