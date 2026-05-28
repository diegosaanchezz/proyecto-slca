from . import db
from flask_login import UserMixin
from datetime import datetime

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreUsuario = db.Column('username', db.String(80), unique=True, nullable=False)
    contrasenhaEncriptada = db.Column('password', db.String(200), nullable=False)

    @property
    def username(self):
        return self.nombreUsuario

    @property
    def password(self):
        return self.contrasenhaEncriptada

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreProducto = db.Column('nombre', db.String(100), nullable=False)
    precioProducto = db.Column('precio', db.Float, nullable=False)
    stockDisponible = db.Column('stock', db.Integer, nullable=False, default=0)
    categoriaProducto = db.Column('categoria', db.String(50))

    @property
    def nombre(self):
        return self.nombreProducto

    @property
    def precio(self):
        return self.precioProducto

    @property
    def stock(self):
        return self.stockDisponible

    @property
    def categoria(self):
        return self.categoriaProducto

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idProductoVendido = db.Column('producto_id', db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidadVendida = db.Column('cantidad', db.Integer, nullable=False)
    totalVenta = db.Column('total', db.Float, nullable=False)
    fechaVenta = db.Column('fecha', db.DateTime, default=datetime.utcnow)
    productoRelacionado = db.relationship('Producto', backref='ventas')

    @property
    def producto_id(self):
        return self.idProductoVendido

    @property
    def cantidad(self):
        return self.cantidadVendida

    @property
    def total(self):
        return self.totalVenta

    @property
    def fecha(self):
        return self.fechaVenta

    @property
    def producto(self):
        return self.productoRelacionado
