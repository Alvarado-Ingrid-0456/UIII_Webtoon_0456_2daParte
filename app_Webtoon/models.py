from django.db import models

# ==========================================
# MODELO: USUARIO (ya existente)
# ==========================================
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    avatar = models.URLField(max_length=255, null=True, blank=True)
    biografia = models.TextField(blank=True, null=True)
    tipo_usuario = models.CharField(
        max_length=20,
        choices=[
            ('Lector', 'Lector'),
            ('Autor', 'Autor'),
            ('Admin', 'Admin')
        ],
        default='Lector'
    )

    def __str__(self):
        return self.nombre_usuario

# ==========================================
# MODELO: WEBTOON
# ==========================================
class Webtoon(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    genero = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    portada = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[
        ('En curso', 'En curso'),
        ('Finalizado', 'Finalizado'),
        ('Hiato', 'Hiato')
    ], default='En curso')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='webtoons')

    def __str__(self):
        return self.titulo

# ==========================================
# MODELO: MEMBRESIA (pendiente)
# ==========================================
