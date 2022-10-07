from typing import Optional

from pydantic.config import Extra
from pydantic.fields import Field
from pydantic.main import BaseModel

from modules.person_roles.constants import PersonRoles


class SearchByParams(BaseModel):
    class Config:
        extra = Extra.allow

    person_role: PersonRoles = Field(description='Роль сотрудника')
    limit: int | None = Field(ge=0)
    offset: int | None = Field(ge=0)


class SearchByParamsOut(BaseModel):
    items: list[dict]
    params: SearchByParams
