# Manual de usuario — TiendaTrack

## Requisitos previos

- Python 3.10 o superior instalado
- Git instalado
- Navegador web (Chrome, Firefox, Safari)

## Instalación

1. Clonar el repositorio:

        git clone https://github.com/diegosaanchezz/proyecto-slca.git
        cd proyecto-slca

2. Crear el entorno virtual:

        python3 -m venv venv
        source venv/bin/activate

3. Instalar dependencias:

        pip install -r requirements.txt

4. Levantar el servidor:

        python3 run.py

5. Abrir en el navegador:

        http://localhost:5000

## Crear una cuenta

Al entrar por primera vez el sistema te redirige a la pantalla de login. Haz clic en "Registrate", escribe un nombre de usuario y contraseña y haz clic en "Crear cuenta". El sistema te redirige al login para que inicies sesion con tu nueva cuenta.

## Iniciar sesion

Escribe tu usuario y contraseña en la pantalla de login y haz clic en "Iniciar sesion". Si los datos son correctos entras al sistema y ves la lista de productos.

## Dashboard

El dashboard muestra un resumen del estado actual de la tienda con cuatro tarjetas: total de productos registrados, total de ventas realizadas, ingresos totales acumulados y el producto mas vendido. Tambien muestra una tabla con los productos que tienen stock igual o menor a 5 unidades para que puedas reabastecerlos a tiempo.

## Agregar un producto

1. Haz clic en "Productos" en el menu superior
2. Haz clic en el boton "Nuevo producto"
3. Llena el formulario con nombre, categoria, precio y stock inicial
4. Haz clic en "Guardar"

El producto aparece en la lista con un badge verde si tiene mas de 5 unidades en stock o rojo si tiene 5 o menos.

## Editar un producto

En la lista de productos haz clic en el icono del lapiz en la fila del producto que quieres editar, modifica los campos que necesites y haz clic en "Actualizar".

## Eliminar un producto

En la lista de productos haz clic en el icono del bote de basura en la fila del producto que quieres eliminar. El sistema te pide confirmacion antes de eliminar.

## Registrar una venta

1. Haz clic en "Ventas" en el menu superior
2. Haz clic en el boton "Nueva venta"
3. Selecciona el producto del menu desplegable — solo aparecen productos con stock disponible
4. Escribe la cantidad a vender
5. Haz clic en "Registrar venta"

El sistema descuenta automaticamente la cantidad vendida del stock del producto y registra la venta con la fecha y hora actual. Si la cantidad ingresada supera el stock disponible el sistema muestra un mensaje de error y no registra la venta.

## Ver historial de ventas

Haz clic en "Ventas" en el menu superior para ver el historial completo de ventas ordenado de la mas reciente a la mas antigua, con el producto, cantidad, total y fecha de cada venta, ademas del total acumulado de todos los ingresos.

## Cerrar sesion

Haz clic en "Cerrar sesion" en la parte superior derecha del menu para salir del sistema.
