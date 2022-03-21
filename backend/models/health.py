from pydantic import BaseModel, Field


class HealthModel(BaseModel):
    status: str = Field(...)
    version: str = Field(...)
    db_ping: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example': {
                'status': 'OK',
                'version': '0.1.0',
                'db_ping': 'pong',
            }
        }