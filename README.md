TaskRunner API

API REST para la gestión de tareas académicas desarrollada con Django y Django REST Framework.

Este proyecto funciona como backend base para registrar, consultar, actualizar y eliminar tareas escolares mediante endpoints REST. Está pensado como una práctica académica enfocada en comprender la estructura de una API, la separación de responsabilidades y la correcta documentación técnica del proceso.

Objetivo del proyecto

El objetivo de este proyecto es aplicar conceptos fundamentales de desarrollo backend, específicamente:

Configuración correcta de rutas (endpoints).

Separación básica entre rutas y lógica de negocio.

Implementación de controladores simples.

Documentación clara y replicable del proceso técnico.

El proyecto está diseñado para ejecutarse localmente y servir como base para futuras ampliaciones.

Descripción general

TaskRunner API centraliza la lógica relacionada con la gestión de tareas académicas.
En esta primera versión, el sistema permite realizar operaciones CRUD sobre tareas utilizando una API REST que responde en formato JSON.

No se incluye autenticación ni lógica avanzada, ya que el enfoque está en la estructura y claridad del backend.

Alcance técnico (MVP)
Recurso principal

Tasks (tareas)

Operaciones REST implementadas

GET /api/tasks/
Lista todas las tareas registradas.

POST /api/tasks/
Crea una nueva tarea.

GET /api/tasks/{id}/
Obtiene el detalle de una tarea específica.

PUT /api/tasks/{id}/
Actualiza una tarea existente.

DELETE /api/tasks/{id}/
Elimina una tarea.

Este conjunto de endpoints cumple con el uso correcto de métodos HTTP, convenciones REST y respuestas en formato JSON.

Reglas de negocio iniciales

Toda tarea debe tener un título.

La descripción es opcional.

Las tareas pueden crearse, editarse y eliminarse desde la API.

Cada tarea tiene un identificador único.

Las respuestas de la API son en formato JSON.

Se utiliza SQLite como base de datos local para desarrollo.

Configuración de rutas y controladores
Estructura del proyecto
TaskRunner-API/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── taskrunner/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
└── README.md

Responsabilidad de cada parte

taskrunner/urls.py
Archivo principal de rutas del proyecto. Aquí se registran las rutas generales y se conecta la app tasks.

tasks/urls.py
Define las rutas específicas del recurso tareas (/api/tasks/).

tasks/views.py
Contiene los controladores que manejan la lógica de cada endpoint.

Esta separación permite que las rutas solo se encarguen de direccionar las peticiones, mientras que la lógica de negocio se mantiene en los controladores.

Paso a paso técnico

Se creó el proyecto Django con django-admin startproject.

Se creó la aplicación tasks para manejar el recurso principal.

Se definió el modelo Task en models.py.

Se creó un serializer para convertir los datos a JSON.

Se implementaron los controladores en views.py.

Se configuraron las rutas del recurso en tasks/urls.py.

Las rutas de la app se registraron en taskrunner/urls.py.

Este flujo permite mantener el proyecto organizado y fácil de escalar.

Endpoints implementados
Crear tarea

POST /api/tasks/

Request:

{
  "title": "Entregar actividad de backend",
  "description": "API con Django REST Framework"
}


Response (201):

{
  "id": 1,
  "title": "Entregar actividad de backend",
  "description": "API con Django REST Framework"
}

Listar tareas

GET /api/tasks/

Response (200):

[
  {
    "id": 1,
    "title": "Entregar actividad de backend",
    "description": "API con Django REST Framework"
  }
]

Obtener una tarea

GET /api/tasks/{id}/

Actualizar una tarea

PUT /api/tasks/{id}/

Eliminar una tarea

DELETE /api/tasks/{id}/

Cómo probar la API
Levantar el servidor

Crear entorno virtual:

Windows:

python -m venv venv
venv\Scripts\activate


Linux / macOS:

python3 -m venv venv
source venv/bin/activate


Instalar dependencias:

pip install -r requirements.txt


Ejecutar migraciones:

python manage.py migrate


Iniciar servidor:

python manage.py runserver


Servidor local:

http://127.0.0.1:8000/


Los endpoints pueden probarse desde el navegador, Postman o usando curl.

Tecnologías utilizadas

Python

Django

Django REST Framework

SQLite

Git y GitHub

Visual Studio Code

Autor

Mario Quiñones Castro
Estudiante universitario de Software

Notas finales

Este proyecto sirve como base para seguir ampliando funcionalidades, tales como:

Autenticación de usuarios

Asignación de tareas por usuario

Manejo de estados y prioridades

Integración con un frontend web o móvil

El enfoque principal del proyecto es reforzar el aprendizaje del desarrollo backend utilizando Django REST Framework
