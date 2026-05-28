from app import crearAplicacion

aplicacion = crearAplicacion()

if __name__ == '__main__':
    aplicacion.run(debug=True, host='0.0.0.0', port=5000)
