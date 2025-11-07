# app_Webtoon/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from .models import Usuario, Webtoon  # <-- Asegúrate de importar ambos modelos

# ==========================================
# PÁGINA DE INICIO
# ==========================================
def inicio_webtoon(request):
    usuarios = Usuario.objects.all().order_by('-fecha_registro')
    webtoons = Webtoon.objects.all().order_by('-fecha_publicacion')
    return render(request, 'inicio.html', {'usuarios': usuarios, 'webtoons': webtoons})


# ==========================================
# CRUD USUARIOS (ya funcionando)
# ==========================================
def agregar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_usuario', '')
        email = request.POST.get('email', '')
        contraseña = request.POST.get('contraseña', '')
        avatar = request.POST.get('avatar', '')
        biografia = request.POST.get('biografia', '')
        tipo = request.POST.get('tipo_usuario', 'Lector')

        usuario = Usuario(
            nombre_usuario=nombre,
            email=email,
            contraseña=make_password(contraseña),
            avatar=avatar,
            biografia=biografia,
            tipo_usuario=tipo
        )
        usuario.save()
        return redirect('app_Webtoon:ver_usuario')
    return render(request, 'usuario/agregar_usuario.html')


def ver_usuario(request):
    usuarios = Usuario.objects.all().order_by('id')
    return render(request, 'usuario/ver_usuario.html', {'usuarios': usuarios})


def actualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'usuario/actualizar_usuario.html', {'usuario': usuario})


def realizar_actualizacion_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.nombre_usuario = request.POST.get('nombre_usuario', usuario.nombre_usuario)
        usuario.email = request.POST.get('email', usuario.email)
        nueva_contraseña = request.POST.get('contraseña', '')
        if nueva_contraseña:
            usuario.contraseña = make_password(nueva_contraseña)
        usuario.avatar = request.POST.get('avatar', usuario.avatar)
        usuario.biografia = request.POST.get('biografia', usuario.biografia)
        usuario.tipo_usuario = request.POST.get('tipo_usuario', usuario.tipo_usuario)
        usuario.save()
        return redirect('app_Webtoon:ver_usuario')
    return redirect('app_Webtoon:actualizar_usuario', usuario_id=usuario.id)


def borrar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('app_Webtoon:ver_usuario')
    return render(request, 'usuario/borrar_usuario.html', {'usuario': usuario})


# ==========================================
# CRUD WEBTOONS
# ==========================================

# --- AGREGAR ---
def agregar_webtoon(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '')
        descripcion = request.POST.get('descripcion', '')
        genero = request.POST.get('genero', '')
        fecha_publicacion = request.POST.get('fecha_publicacion', '')
        portada = request.POST.get('portada', '')
        estado = request.POST.get('estado', 'En curso')
        autor_id = request.POST.get('autor', None)

        autor = None
        if autor_id:
            try:
                autor = Usuario.objects.get(id=int(autor_id))
            except Usuario.DoesNotExist:
                autor = None

        webtoon = Webtoon(
            titulo=titulo,
            descripcion=descripcion,
            genero=genero,
            fecha_publicacion=fecha_publicacion or timezone.now().date(),
            portada=portada,
            estado=estado,
            autor=autor
        )
        webtoon.save()
        return redirect('app_Webtoon:ver_webtoons')

    autores = Usuario.objects.all()
    return render(request, 'webtoons/agregar_webtoon.html', {'autores': autores})


# --- VER ---
def ver_webtoons(request):
    webtoons = Webtoon.objects.all().order_by('id')
    return render(request, 'webtoons/ver_webtoons.html', {'webtoons': webtoons})


# --- ACTUALIZAR (mostrar formulario) ---
def actualizar_webtoon(request, webtoon_id):
    webtoon = get_object_or_404(Webtoon, id=webtoon_id)
    autores = Usuario.objects.all()
    return render(request, 'webtoons/actualizar_webtoon.html', {'webtoon': webtoon, 'autores': autores})


# --- REALIZAR ACTUALIZACIÓN ---
def realizar_actualizacion_webtoon(request, webtoon_id):
    webtoon = get_object_or_404(Webtoon, id=webtoon_id)
    if request.method == 'POST':
        webtoon.titulo = request.POST.get('titulo', webtoon.titulo)
        webtoon.descripcion = request.POST.get('descripcion', webtoon.descripcion)
        webtoon.genero = request.POST.get('genero', webtoon.genero)
        fecha_pub = request.POST.get('fecha_publicacion', None)
        if fecha_pub:
            webtoon.fecha_publicacion = fecha_pub
        webtoon.portada = request.POST.get('portada', webtoon.portada)
        webtoon.estado = request.POST.get('estado', webtoon.estado)

        autor_id = request.POST.get('autor', None)
        if autor_id:
            try:
                webtoon.autor = Usuario.objects.get(id=int(autor_id))
            except Usuario.DoesNotExist:
                pass

        webtoon.save()
        return redirect('app_Webtoon:ver_webtoons')
    return redirect('app_Webtoon:actualizar_webtoon', webtoon_id=webtoon.id)


# --- BORRAR ---
def borrar_webtoon(request, webtoon_id):
    webtoon = get_object_or_404(Webtoon, id=webtoon_id)
    if request.method == 'POST':
        webtoon.delete()
        return redirect('app_Webtoon:ver_webtoons')
    return render(request, 'webtoons/borrar_webtoon.html', {'webtoon': webtoon})
