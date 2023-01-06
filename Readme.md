Base de datos del Proyecto TRAMA
=================================

# Descripción:

Base de datos con autores / obras / trabajos representados de las mujeres en Andalucía, en la Edad Moderna.


# Instalación / uso

## Pre-instalación

- Hacer checkout del repositorio, `https://github.com/alfonsoeromero/bd_trama`
- Crear entorno virtual e instalar dependencias de `requirements.txt`

## Creación y carga de la base de datos

a. Borrado de las tablas de la antigua bd:
`python manage.py flush`

b. Creación de la bd:
`python manage.py migrate`

c. Carga de los datos mediante las fixturas existentes:
`python manage.py loaddata trama/fixtures/data.json`


## Backup como fixtura de la base de datos existente
`python manage.py dumpdata --indent=4 --exclude=auth --exclude=contenttypes > trama/fixtures/data.json`


## Ejecución del servidor de desarrollo

Existen dos scripts para la ejecución del servidor de desarrollo, en el directorio `scripts`, uno para sistemas GNU/Linux (`trama.sh`) y otro para MacOS (`trama.command`). Ejecutando el script conveniente se lanzará en segundo plano el servidor de desarrollo en el puerto 8000.
