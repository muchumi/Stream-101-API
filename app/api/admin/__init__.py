from flask import Blueprint

"""
    Admin Blueprint
"""

blueprint = Blueprint(
    'admin_blueprint',
    __name__,
    url_prefix = '/admin'
)


from app.api.admin.views import admin