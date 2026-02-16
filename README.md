# TaskRunner API

Backend REST construido con Django y Django REST Framework para gestionar tareas.

## Estado actual

- Proyecto Django activo en `backend/`
- Recurso expuesto: `Task` (CRUD completo via `ModelViewSet`)
- Autenticacion JWT habilitada (`SimpleJWT`)
- Documentacion OpenAPI disponible con `drf-spectacular`
- Base de datos local: SQLite

## Estructura del proyecto

```text
TaskRunner_API/
|-- backend/
|   |-- manage.py
|   |-- db.sqlite3
|   |-- config/
|   |   |-- settings.py
|   |   `-- urls.py
|   |-- runner/
|   |   |-- models.py
|   |   |-- serializers.py
|   |   |-- views.py
|   |   `-- urls.py
|   `-- users/
`-- requirements.txt
```

Nota: en la raiz existe otro `manage.py`, pero el backend funcional que usa `runner` y `users` es `backend/manage.py`.

## Requisitos

- Python 3.12+ (recomendado)
- Entorno virtual

## Instalacion y ejecucion

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
.\.venv\Scripts\python.exe backend\manage.py migrate
.\.venv\Scripts\python.exe backend\manage.py runserver
```

Servidor local: `http://127.0.0.1:8000/`

## Endpoints principales

### CRUD de tareas

- `GET /api/tasks/`
- `POST /api/tasks/`
- `GET /api/tasks/{id}/`
- `PUT /api/tasks/{id}/`
- `PATCH /api/tasks/{id}/`
- `DELETE /api/tasks/{id}/`

### Autenticacion JWT

- `POST /api/token/` (obtener access y refresh)
- `POST /api/token/refresh/` (renovar access)

### Documentacion

- `GET /api/schema/` (OpenAPI schema)
- `GET /api/docs/` (Swagger UI)
- `GET /api/redoc/` (ReDoc)

## Modelo Task (actual)

Campos expuestos por la API:

- `id`
- `task_master_id` (unico)
- `title`
- `description` (opcional)
- `status` (default: `pending`)
- `assigned_at` (auto)
- `completed_at` (opcional)

## Ejemplo de creacion de tarea

```json
{
  "task_master_id": "TM-001",
  "title": "Preparar entrega final",
  "description": "Actualizar README y validar endpoints",
  "status": "pending"
}
```

## CORS (desarrollo)

Origenes permitidos actualmente:

- `http://127.0.0.1:5500`
- `http://localhost:5500`
- `http://127.0.0.1:5501`
- `http://localhost:5501`

## Dependencias principales

- Django 6.0.1
- djangorestframework 3.16.1
- djangorestframework_simplejwt 5.5.1
- drf-spectacular 0.29.0
- django-cors-headers 4.9.0
