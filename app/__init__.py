from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
loginManager = LoginManager()

def crearAplicacion():
    aplicacion = Flask(__name__)
    aplicacion.config.from_object('config.Config')

    db.init_app(aplicacion)
    loginManager.init_app(aplicacion)
    loginManager.login_view = 'auth.paginaLogin'
    loginManager.login_message = 'Inicia sesion para continuar.'

    from .routes import autenticacion, gestionProductos, gestionVentas
    aplicacion.register_blueprint(autenticacion)
    aplicacion.register_blueprint(gestionProductos)
    aplicacion.register_blueprint(gestionVentas)

    with aplicacion.app_context():
        db.create_all()

    return aplicacion

from app.models import Usuario

@loginManager.user_loader
def cargarUsuario(idUsuario):
    return Usuario.query.get(int(idUsuario))
