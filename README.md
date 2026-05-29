# TiendaTrack

TiendaTrack es un sistema web para registrar y controlar las ventas de una tienda, hecho con Python y Flask y una base de datos SQLite porque la idea era tener algo que funcione de forma local sin depender de servicios externos y que cualquier persona pueda levantar en su maquina sin mucha complicación, de esta manera las pequeñas empresas que no disponen de mucho dinero para pagar un software puedan utilizarlo y administrar su empresa por ese medio.

## Para que sirve

Permite registrar productos con su precio y stock, hacer ventas que descuentan el inventario automaticamente, de esta manera pueden llevar un historial actualizado de su inventario y ver el historial de todas las ventas con el total acumulado, ademas de tener un sistema de autenticación para que solo usuarios registrados puedan acceder.

## Stack tecnologico

Todo el proyecto usa software de codigo abierto:

- Python 3 — PSF License
- Flask 3.1 — BSD License
- SQLAlchemy 2.0 — MIT License
- Flask-Login 0.6 — MIT License
- Bootstrap 5 — MIT License
- SQLite — Dominio publico

## Como instalar y correr el proyecto

Clona el repositorio:

    git clone https://github.com/diegosaanchezz/proyecto-slca.git
    cd proyecto-slca

Crea el entorno virtual:

    python3 -m venv venv
    source venv/bin/activate

Instala las dependencias:

    pip install -r requirements.txt

Levanta el servidor:

    python3 run.py

Abre el navegador en http://localhost:5000, crea una cuenta y ya puedes empezar a usar el sistema.

## Funcionalidades

El sistema tiene tres modulos principales que son autenticacion, gestion de productos y registro de ventas. En productos puedes agregar, editar y eliminar productos con su nombre, categoria, precio y stock. En ventas puedes registrar una venta seleccionando el producto y la cantidad, el sistema descuenta el stock automaticamente y calcula el total. Si el stock no es suficiente para la cantidad que quieres vender el sistema te avisa antes de registrar la venta de esta manera nos aseguramos de no tener numeros negativos en el inventario.

## Estructura del proyecto

    proyecto/
    ├── run.py
    ├── config.py
    ├── requirements.txt
    ├── LICENSE
    ├── CONTRIBUTING.md
    └── app/
        ├── __init__.py
        ├── models.py
        ├── routes.py
        └── templates/
            ├── base.html
            ├── auth/
            ├── productos/
            └── ventas/

## Licencia

MIT License — ver archivo LICENSE para mas detalles.
