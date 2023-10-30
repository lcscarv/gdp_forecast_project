from typing import Any, List

from pydantic import BaseModel


class UniqueGroups(BaseModel):
    values: List[str]

class CountriesPerGroup(BaseModel):
    country_list: List[str]