# Como contribuir a TiendaTrack

Este proyecto esta hecho con Python y Flask y cualquier persona puede contribuir aunque hay algunas cosas que hay que tener en cuenta antes de empezar porque si no se siguen las convenciones del proyecto el codigo puede volverse dificil de leer y mantener.

## Lo que necesitas tener instalado en tu computadora

- Python 3.10 o superior
- Git

## Como configurar el proyecto en tu computadora

Primero clona el repositorio:
git clone https://github.com/diegosaanchezz/proyecto-slca.git
cd proyecto-slca

Luego crea el entorno virtual y activalo:

python3 -m venv venv
source venv/bin/activate

Instala las dependencias:

pip install -r requirements.txt

Y levanta el servidor:

python3 run.py

Abre tu navegador en http://localhost:5000 y ya deberia estar corriendo.

## Convenciones de codigo

Las variables y funciones van en camelCase en español, con nombres largos y descriptivos porque el codigo debe entenderse y estar bien estructurado, de lo contrario es dificil que el proyecto este organizado si no se siguen las convenciones.

En caso de tener una variable como "año" se debera nombrar agno, de esta manera no rompemos con el uso de palabras no permitidas por el lenguaje y tener en español las variables

## Como trabajar con Git

Cada nueva funcionalidad va en su propia rama y los commits deben tener mensajes claros que expliquen que se hizo, no solo "cambios" o "fix" sin contexto. Cuando este listo se abre un Pull Request hacia main con una descripcion de los cambios.

## Reportar errores o sugerir mejoras

Se abre un Issue en GitHub describiendo el problema o la mejora, con los pasos para reproducir el error si aplica y lo que se esperaba que pasara versus lo que paso.
