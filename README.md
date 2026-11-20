# Portafolio personal – Cefora Rebeca

Proyecto académico Django + JavaScript. Incluye seis rutas, vistas, plantillas, archivos estáticos y menú móvil, validación de formulario y filtros de proyectos.

## Ejecutar en Windows (PowerShell)

1. Abre esta carpeta en Visual Studio Code.
2. En la terminal ejecuta:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

3. Abre http://127.0.0.1:8000/

Para detener el servidor presiona Ctrl+C. No hace falta activar el entorno virtual porque usamos directamente su ejecutable.

## Rutas

- `/` Inicio
- `/sobre-mi/` Sobre mí
- `/habilidades/` Habilidades
- `/proyectos/` Proyectos
- `/contacto/` Contacto
- `/404/` Ejemplo de página 404; otras rutas inexistentes devuelven error 404.

## Notas

El formulario es una demostración, no envía datos a un servidor. No hay modelos de datos ni autenticación de usuarios.

El diseño proviene del prototipo HTML de la estudiante. Para entregar, comparar con los mockups de Figma, realizar commits en GitHub y preparar la demostración.

`DEBUG=True` y la clave local solo son adecuados para desarrollo; antes de publicar configura variables de entorno, `DEBUG=False` y `ALLOWED_HOSTS`.
