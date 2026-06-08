# Portfolio — Dhana Corredor

Portfolio personal de **Dhana Corredor**, MarTech Developer & Frontend Engineer (Madrid).
Sitio bilingüe (ES/EN) con la web principal y dos versiones del CV (web y para imprimir/PDF).

## Stack

- **Backend:** Django 5.2 (Python)
- **Estilos:** Tailwind CSS 4 (vía `django-tailwind` + PostCSS)
- **Estáticos:** WhiteNoise (servidos por la app, con hashing y compresión)
- **i18n:** traducción ES/EN con `gettext` (catálogos compilados con `babel`)
- **Despliegue:** Vercel (TLS terminado por la plataforma)

## Estructura

```
portfolio/        # settings, urls, wsgi/asgi del proyecto
core/             # vistas y urls del sitio (index + CVs)
templates/        # base.html, index.html, cv-marketing*.html
theme/            # app de django-tailwind (CSS fuente y compilado)
  static_src/     #   código fuente Tailwind/PostCSS (package.json)
  static/css/dist/#   CSS compilado (versionado para Vercel)
static/           # favicon, CV en PDF, imagen Open Graph, JS
locale/           # traducciones es/en (.po + .mo)
```

## Rutas

| URL | Descripción |
|-----|-------------|
| `/` | Home del portfolio |
| `/cv/marketing/` | CV en versión web |
| `/cv/marketing/imprimir/` | CV optimizado para imprimir / guardar como PDF |

El prefijo de idioma se añade solo para inglés (`/en/…`); el español es el idioma por defecto sin prefijo.

## Desarrollo local

Requisitos: Python 3.12+ y Node.js (para compilar Tailwind).

```bash
# 1. Entorno e instalación
python -m venv .venv
.venv\Scripts\activate          # Windows  (source .venv/bin/activate en macOS/Linux)
pip install -r requirements.txt

# 2. Dependencias de Tailwind (primera vez)
python manage.py tailwind install

# 3. Compilar Tailwind en modo watch (terminal aparte)
python manage.py tailwind start

# 4. Levantar el servidor (DEBUG activa el auto-reload del navegador)
set DJANGO_DEBUG=true            # Windows  (export DJANGO_DEBUG=true en macOS/Linux)
python manage.py runserver
```

App disponible en http://127.0.0.1:8000/

## Build de producción de Tailwind

El CSS compilado (`theme/static/css/dist/styles.css`) **se versiona** porque el runtime de Python en Vercel no tiene Node. Tras tocar estilos o clases:

```bash
cd theme/static_src
npm run build        # genera el CSS minificado
```

## Traducciones (i18n)

Los textos van envueltos en `{% translate %}` / `{% blocktranslate %}` (plantillas) y `_()` (Python).

```bash
# Extraer/actualizar cadenas
python manage.py makemessages -l es -l en

# Compilar a .mo
python manage.py compilemessages
```

> Si no tienes `gettext` (`msgfmt`) instalado, los `.mo` pueden recompilarse con `babel`
> (incluido en `requirements.txt`) leyendo cada `.po` y escribiendo su `.mo`.

## Tests

```bash
python manage.py test
```

Cubren las tres rutas públicas, el cambio de idioma ES/EN y varias guardas de
regresión de contenido (enlace de reserva válido, imagen Open Graph absoluta,
nivel de inglés sin sobredeclarar).

## Variables de entorno

| Variable | Por defecto | Uso |
|----------|-------------|-----|
| `DJANGO_SECRET_KEY` | clave de desarrollo | **obligatoria en producción** |
| `DJANGO_DEBUG` | `False` | `true` para desarrollo |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1,.vercel.app` | hosts permitidos (separados por comas) |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | `https://*.vercel.app` | orígenes CSRF de confianza |
| `NPM_BIN_PATH` | ruta a `npm.cmd` (Windows) | usado por `django-tailwind` |

## Despliegue

Configurado para **Vercel**. Antes de desplegar, asegúrate de:

1. Tener el CSS de Tailwind compilado y versionado.
2. Definir `DJANGO_SECRET_KEY` (y revisar `DJANGO_ALLOWED_HOSTS`) en el panel de Vercel.
3. Ejecutar `python manage.py collectstatic` si tu pipeline de build lo requiere.
