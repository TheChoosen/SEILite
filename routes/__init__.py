"""
Package des routes pour SEILite
Contient tous les blueprints et routes de l'application
"""

from .clients_routes import clients_bp
from .documents_routes import documents_bp
from .vehicules_routes import vehicules_bp

__all__ = ['clients_bp', 'documents_bp', 'vehicules_bp']
