# RRHH Flask API

Backend REST para la gestión de empleados, desarrollado con **Flask**, **SQLAlchemy** y **MySQL**. Expone un CRUD completo (listar, crear, editar y eliminar empleados) consumido por un frontend en [Angular](https://github.com/brianmatiasllampa/rrhh-angular).

## Tecnologías

- Python 3
- Flask
- Flask-SQLAlchemy / Flask-Migrate (Alembic)
- Flask-CORS
- MySQL (PyMySQL)
- python-dotenv

## Requisitos previos

- Python 3.10+
- MySQL corriendo localmente (o accesible por red)
- Una base de datos creada para el proyecto

## Instalación

1. Cloná el repositorio:
   ```bash
   git clone https://github.com/brianmatiasllampa/rrhh-flask-api.git
   cd rrhh-flask-api
   ```

2. Creá y activá un entorno virtual:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\Activate.ps1
   # Mac/Linux
   source .venv/bin/activate
   ```

3. Instalá las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Copiá el archivo de variables de entorno de ejemplo y completá tus datos:
   ```bash
   cp .env.example .env
   ```
   Editá `.env` con la conexión a tu base de datos:
   ```
   DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost/nombre_de_tu_base?charset=utf8mb4
   ```

5. Aplicá las migraciones:
   ```bash
   flask db upgrade
   ```

## Uso

```bash
python app.py
```

El servidor levanta por defecto en `http://127.0.0.1:8080`.

## Endpoints principales

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/api/empleados` | Lista todos los empleados |
| POST | `/api/empleados` | Crea un nuevo empleado |
| PUT | `/api/empleados/<id>` | Edita un empleado existente |
| DELETE | `/api/empleados/<id>` | Elimina un empleado |

## Proyecto relacionado

- Frontend: [rrhh-angular](https://github.com/brianmatiasllampa/rrhh-angular)
