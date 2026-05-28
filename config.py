import os

class Config:
    SECRET_KEY = 'tiendatrack-secret-key-2024'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tiendatrack.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
