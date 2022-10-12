# Generated by Django 4.1.1 on 2022-10-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trama', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obra',
            name='nombre_archivo',
        ),
        migrations.AlterField(
            model_name='estilo',
            name='nombre_estilo',
            field=models.CharField(help_text='Nombre del estilo artítico (Renacimiento, barroco, etc.)', max_length=256),
        ),
        migrations.AlterField(
            model_name='obra',
            name='anno',
            field=models.CharField(help_text='Año (exacto o aproximado) de creación de la obra', max_length=64),
        ),
        migrations.AlterField(
            model_name='obra',
            name='autor',
            field=models.CharField(help_text='Autor de la obra', max_length=256),
        ),
        migrations.AlterField(
            model_name='obra',
            name='descripcion',
            field=models.TextField(help_text='Descripción de la obra en texto libre'),
        ),
        migrations.AlterField(
            model_name='obra',
            name='iconografia',
            field=models.CharField(help_text='Breve descripción de la iconografía representada', max_length=128),
        ),
        migrations.AlterField(
            model_name='obra',
            name='nombre_obra',
            field=models.CharField(help_text='Nombre completo de la obra', max_length=256),
        ),
        migrations.AlterField(
            model_name='obra',
            name='ubicacion',
            field=models.CharField(help_text='Ubicación de la obra (museo, colección particular...)', max_length=128),
        ),
        migrations.AlterField(
            model_name='tipodeobra',
            name='nombre_tipo',
            field=models.CharField(help_text='Tipo de obra: Pintura, Escultura,...', max_length=256),
        ),
        migrations.AlterField(
            model_name='trabajorepresentado',
            name='nombre_trabajo',
            field=models.CharField(help_text='Nombre de la profesión representada (hilandera, curandera,...)', max_length=256),
        ),
    ]
