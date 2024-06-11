from pydantic import BaseModel

from src.core.pydantic.mixins import SolidMixin


class TaskRequest(SolidMixin, BaseModel):
    url: str


class TaskResponse(SolidMixin, BaseModel):
    id: str
    status: str
