# Bitácora del proyecto — TiendaTrack

## Definición del proyecto

Al principio no tenia muy claro que sistema hacer porque habia varias opciones interesantes pero al final me decidi por un sistema de ventas porque es algo que tiene logica de negocio real y me interesa mucho el tema de un sistema de registro de inventario y ventas de una empresa, ademas de que es algo que cualquier tienda pequeña podria usar en su dia a dia sin necesidad de pagar un software caro.

Decidi usar Python con Flask porque es el lenguaje con el que me siento mas comodo y Flask es suficientemente sencillo para no perder tiempo configurando cosas que no necesito, la base de datos la deje en SQLite porque para un proyecto de este tamaño no tiene sentido instalar PostgreSQL o MySQL.

## Configuración del entorno

Tuve un problema al instalar las dependencias porque Kali Linux protege su Python del sistema y no deja instalar paquetes directamente con pip, asi que decidi tomar la decision de crear un entorno virtual con python3 -m venv venv que es la forma correcta de hacerlo de todas formas porque asi las dependencias que instale quedan aisladas del sistema.

La estructura de carpetas la defini desde el principio para tener claro donde va cada cosa, esto ayuda mucho al orden y entender bien la estructura que debia llevar el proyecto, los modelos separados de las rutas y los templates en su propia carpeta organizada por modulo.

## Desarrollo de modelos y rutas

Defini los tres modelos principales: Usuario para la autenticacion, Producto para el inventario y Venta para registrar cada transaccion.

## Templates y pruebas

Agregue todos los templates HTML usando Bootstrap 5 para que la interfaz se vea profesional sin tener que escribir CSS desde cero. Probe el flujo completo: registro de usuario, inicio de sesion, agregar productos, registrar ventas y verificar que el stock se descuenta correctamente, todo funciono sin errores.

## Decisiones tecnicas

Se eligio Flask sobre Django porque para un proyecto de este tamaño Django tiene demasiada configuracion inicial y Flask permite ir mas rapido sin sacrificar funcionalidad, SQLite se eligio sobre PostgreSQL por la misma razon y porque el objetivo era que cualquier persona pueda correr el proyecto sin instalar nada extra ademas de Python.

## Problemas encontrados y como se resolvieron

El primer problema fue con pip en Kali Linux que no dejaba instalar paquetes por ser un entorno administrado externamente, se resolvio con entorno virtual. El segundo fue con los modelos de SQLAlchemy y los @property que rompian la creacion de objetos, se resolvio dejando los nombres de columna simples en los modelos.
