from django.db import models


class Estilo(models.Model):
    nombre_estilo = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        help_text="Nombre del estilo artítico (Renacimiento, barroco, etc.)")

    def __str__(self):
        return self.nombre_estilo


class TipoDeObra(models.Model):
    nombre_tipo = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        help_text="Tipo de obra: Pintura, Escultura,...")

    def __str__(self):
        return self.nombre_tipo


class TrabajoRepresentado(models.Model):
    nombre_trabajo = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        help_text="Nombre de la profesión representada (hilandera, curandera,...)")

    def __str__(self):
        return self.nombre_trabajo


class Autor(models.Model):
    nombre = models.CharField(max_length=256,
                              blank=False,
                              null=False,
                              help_text="Autor de la obra")
    alias = models.CharField(max_length=256,
                             blank=True,
                             null=True,
                             help_text="Alias u otros nombres por los que el artista es conocido"
                             )

    def __str__(self):
        return self.nombre


class Obra(models.Model):
    nombre_obra = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        help_text="Nombre completo de la obra")
    autor = models.ForeignKey(
        Autor,
        blank=False,
        null=False,
        on_delete=models.CASCADE)
    anno = models.CharField("Año o época aproximada de la obra",
                            max_length=64,
                            blank=False,
                            null=False,
                            help_text="Año (exacto o aproximado) de creación de la obra")
    ubicacion = models.CharField("Ubicación",
                                 max_length=128,
                                 blank=False,
                                 null=False,
                                 help_text="Ubicación de la obra (museo, colección particular...)")
    iconografia = models.CharField("Iconografía",
                                   max_length=128,
                                   blank=False,
                                   null=False,
                                   help_text="Breve descripción de la iconografía representada")
    descripcion = models.TextField("Descripción",
                                   blank=False,
                                   null=False,
                                   help_text="Descripción de la obra en texto libre")
    url_externa = models.CharField(max_length=512,
                                   blank=True,
                                   null=True,
                                   help_text="URL con contexto")
    url_imagen = models.CharField(max_length=512,
                                  blank=True,
                                  null=True,
                                  help_text="URL externa del archivo de imagen (si la hay)")
    estilo = models.ForeignKey(
        Estilo,
        blank=False,
        null=False,
        on_delete=models.CASCADE)
    tipo_de_obra = models.ForeignKey(
        TipoDeObra,
        blank=False,
        null=False,
        on_delete=models.CASCADE)
    trabajo_representado = models.ManyToManyField(
        TrabajoRepresentado,
        blank=False)

    def __str__(self):
        return f"{self.nombre_obra} ({self.autor})"
