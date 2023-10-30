from typing import Any, List

from pydantic import BaseModel


class UniqueCountries(BaseModel):
    values: List[str]