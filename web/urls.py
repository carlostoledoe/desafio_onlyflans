from django.urls import path
from web.views import index, about, contact, success, welcome

urlpatterns = [
    path('', index, name='index'),
    path('acerca/', about, name='about'),
    path('bienvenido/', welcome, name='welcome'),
    path('contacto/', contact, name='contact'),
    path('exito/', success, name='success'),
]