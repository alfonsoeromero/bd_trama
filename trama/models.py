from django.db import models


class Estilo(models.Model):
    nombre_estilo = models.CharField(
        max_length=256,
        help_text="Nombre del estilo artítico (Renacimiento, barroco, etc.)")


class TipoDeObra(models.Model):
    nombre_tipo = models.CharField(
        max_length=256,
        help_text="Tipo de obra: Pintura, Escultura,...")


class TrabajoRepresentado(models.Model):
    nombre_trabajo = models.CharField(
        max_length=256,
        help_text="Nombre de la profesión representada (hilandera, curandera,...)")


class Obra(models.Model):
    nombre_obra = models.CharField(
        max_length=256,
        help_text="Nombre completo de la obra")
    autor = models.CharField(max_length=256,
        help_text="Autor de la obra")
    anno = models.CharField(max_length=64,
        help_text="Año (exacto o aproximado) de creación de la obra")
    ubicacion = models.CharField(max_length=128,
        help_text="Ubicación de la obra (museo, colección particular...)")
    iconografia = models.CharField(max_length=128,
        help_text="Breve descripción de la iconografía representada")
    descripcion = models.TextField(
        help_text="Descripción de la obra en texto libre")
    estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE)
    tipo_de_obra = models.ForeignKey(TipoDeObra, on_delete=models.CASCADE)
    trabajo_representado = models.ManyToManyField(TrabajoRepresentado)
