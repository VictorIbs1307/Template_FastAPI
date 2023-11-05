from gino.ext import starlette
from src.app.core.config import Settings 
from sqlalchemy.dialects.postgresql import UUID

DB = starlette.Gino(**Settings().gino_config())
DB.UUID = UUID
