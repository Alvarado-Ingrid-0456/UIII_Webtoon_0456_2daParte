# app_Webtoon/urls.py
from django.urls import path
from . import views

app_name = 'app_Webtoon'

urlpatterns = [
    path('', views.inicio_webtoon, name='inicio'),
    path('usuario/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuario/ver/', views.ver_usuario, name='ver_usuario'),
    path('usuario/actualizar/<int:usuario_id>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuario/realizar_actualizacion/<int:usuario_id>/', views.realizar_actualizacion_usuario, name='realizar_actualizacion_usuario'),
    path('usuario/borrar/<int:usuario_id>/', views.borrar_usuario, name='borrar_usuario'),
    path('webtoons/agregar/', views.agregar_webtoon, name='agregar_webtoon'),
    path('webtoons/ver/', views.ver_webtoons, name='ver_webtoons'),
    path('webtoons/actualizar/<int:webtoon_id>/', views.actualizar_webtoon, name='actualizar_webtoon'),
    path('webtoons/realizar_actualizacion/<int:webtoon_id>/', views.realizar_actualizacion_webtoon, name='realizar_actualizacion_webtoon'),
    path('webtoons/borrar/<int:webtoon_id>/', views.borrar_webtoon, name='borrar_webtoon'),
]
