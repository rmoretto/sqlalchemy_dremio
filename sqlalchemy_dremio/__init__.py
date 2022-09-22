__version__ = '2.0.0'

from .db import Connection, connect
from sqlalchemy.dialects import registry

# Register the Flight end point
registry.register("dremio+flight", "sqlalchemy_dremio.flight", "DremioDialect_flight")
# HACK: Register the flight endpoint as dremio, so superset can see and use the plugin
registry.register("dremio", "sqlalchemy_dremio.flight", "DremioDialect_flight")
