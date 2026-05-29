from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import Usuario, Producto, Venta

autenticacion = Blueprint('auth', __name__)
gestionProductos = Blueprint('productos', __name__, url_prefix='/productos')
gestionVentas = Blueprint('ventas', __name__, url_prefix='/ventas')

@autenticacion.route('/')
def paginaInicio():
    if current_user.is_authenticated:
        return redirect(url_for('productos.listaProductos'))
    return redirect(url_for('auth.paginaLogin'))

@autenticacion.route('/login', methods=['GET', 'POST'])
def paginaLogin():
    if request.method == 'POST':
        nombreUsuario = request.form.get('username')
        contrasenaIngresada = request.form.get('password')
        usuarioEncontrado = Usuario.query.filter_by(username=nombreUsuario).first()
        contrasenaCorrecta = usuarioEncontrado and check_password_hash(usuarioEncontrado.password, contrasenaIngresada)
        if contrasenaCorrecta:
            login_user(usuarioEncontrado)
            return redirect(url_for('productos.listaProductos'))
        flash('Usuario o contrasena incorrectos.', 'danger')
    return render_template('auth/login.html')

@autenticacion.route('/register', methods=['GET', 'POST'])
def paginaRegistro():
    if request.method == 'POST':
        nombreUsuario = request.form.get('username')
        contrasenaIngresada = request.form.get('password')
        usuarioExistente = Usuario.query.filter_by(username=nombreUsuario).first()
        if usuarioExistente:
            flash('El usuario ya existe.', 'danger')
        else:
            contrasenhaEncriptada = generate_password_hash(contrasenaIngresada)
            nuevoUsuario = Usuario(username=nombreUsuario, password=contrasenhaEncriptada)
            db.session.add(nuevoUsuario)
            db.session.commit()
            flash('Cuenta creada. Inicia sesion.', 'success')
            return redirect(url_for('auth.paginaLogin'))
    return render_template('auth/register.html')

@autenticacion.route('/logout')
@login_required
def cerrarSesion():
    logout_user()
    return redirect(url_for('auth.paginaLogin'))

@autenticacion.route('/dashboard')
@login_required
def dashboard():
    totalProductos = Producto.query.count()
    totalVentas = Venta.query.count()
    todasLasVentas = Venta.query.all()
    totalIngresos = sum(v.total for v in todasLasVentas)
    productosStockBajo = Producto.query.filter(Producto.stock <= 5).all()
    productoMasVendido = None
    cantidadMaxima = 0
    todosLosProductos = Producto.query.all()
    for producto in todosLosProductos:
        cantidadVendidaTotal = sum(v.cantidad for v in producto.ventas)
        if cantidadVendidaTotal > cantidadMaxima:
            cantidadMaxima = cantidadVendidaTotal
            productoMasVendido = producto
    return render_template('dashboard.html',
        totalProductos=totalProductos,
        totalVentas=totalVentas,
        totalIngresos=totalIngresos,
        productosStockBajo=productosStockBajo,
        productoMasVendido=productoMasVendido
    )

@gestionProductos.route('/')
@login_required
def listaProductos():
    todosLosProductos = Producto.query.all()
    return render_template('productos/index.html', productos=todosLosProductos)

@gestionProductos.route('/nuevo', methods=['GET', 'POST'])
@login_required
def nuevoProducto():
    if request.method == 'POST':
        nombreProducto = request.form.get('nombre')
        precioProducto = float(request.form.get('precio'))
        stockProducto = int(request.form.get('stock'))
        categoriaProducto = request.form.get('categoria')
        precioNegativo = precioProducto < 0
        stockNegativo = stockProducto < 0
        if precioNegativo:
            flash('El precio no puede ser negativo.', 'danger')
            return render_template('productos/nuevo.html')
        if stockNegativo:
            flash('El stock no puede ser negativo.', 'danger')
            return render_template('productos/nuevo.html')
        productoNuevo = Producto(
            nombre=nombreProducto,
            precio=precioProducto,
            stock=stockProducto,
            categoria=categoriaProducto
        )
        db.session.add(productoNuevo)
        db.session.commit()
        flash('Producto agregado.', 'success')
        return redirect(url_for('productos.listaProductos'))
    return render_template('productos/nuevo.html')

@gestionProductos.route('/editar/<int:idProducto>', methods=['GET', 'POST'])
@login_required
def editarProducto(idProducto):
    productoSeleccionado = Producto.query.get_or_404(idProducto)
    if request.method == 'POST':
        precioProducto = float(request.form.get('precio'))
        stockProducto = int(request.form.get('stock'))
        precioNegativo = precioProducto < 0
        stockNegativo = stockProducto < 0
        if precioNegativo:
            flash('El precio no puede ser negativo.', 'danger')
            return render_template('productos/editar.html', producto=productoSeleccionado)
        if stockNegativo:
            flash('El stock no puede ser negativo.', 'danger')
            return render_template('productos/editar.html', producto=productoSeleccionado)
        productoSeleccionado.nombre = request.form.get('nombre')
        productoSeleccionado.precio = precioProducto
        productoSeleccionado.stock = stockProducto
        productoSeleccionado.categoria = request.form.get('categoria')
        db.session.commit()
        flash('Producto actualizado.', 'success')
        return redirect(url_for('productos.listaProductos'))
    return render_template('productos/editar.html', producto=productoSeleccionado)

@gestionProductos.route('/eliminar/<int:idProducto>')
@login_required
def eliminarProducto(idProducto):
    productoSeleccionado = Producto.query.get_or_404(idProducto)
    db.session.delete(productoSeleccionado)
    db.session.commit()
    flash('Producto eliminado.', 'warning')
    return redirect(url_for('productos.listaProductos'))

@gestionVentas.route('/')
@login_required
def listaVentas():
    todasLasVentas = Venta.query.order_by(Venta.fecha.desc()).all()
    totalAcumulado = sum(v.total for v in todasLasVentas)
    return render_template('ventas/index.html', ventas=todasLasVentas, totalAcumulado=totalAcumulado)

@gestionVentas.route('/nueva', methods=['GET', 'POST'])
@login_required
def nuevaVenta():
    productosDisponibles = Producto.query.filter(Producto.stock > 0).all()
    if request.method == 'POST':
        idProductoSeleccionado = int(request.form.get('producto_id'))
        cantidadVendida = int(request.form.get('cantidad'))
        productoSeleccionado = Producto.query.get_or_404(idProductoSeleccionado)
        cantidadNegativa = cantidadVendida <= 0
        stockInsuficiente = cantidadVendida > productoSeleccionado.stock
        if cantidadNegativa:
            flash('La cantidad debe ser mayor a cero.', 'danger')
        elif stockInsuficiente:
            flash('Stock insuficiente. Solo hay ' + str(productoSeleccionado.stock) + ' unidades.', 'danger')
        else:
            totalVenta = productoSeleccionado.precio * cantidadVendida
            ventaNueva = Venta(producto_id=idProductoSeleccionado, cantidad=cantidadVendida, total=totalVenta)
            productoSeleccionado.stock -= cantidadVendida
            db.session.add(ventaNueva)
            db.session.commit()
            flash('Venta registrada por $' + str(round(totalVenta, 2)), 'success')
            return redirect(url_for('ventas.listaVentas'))
    return render_template('ventas/nueva.html', productos=productosDisponibles)
