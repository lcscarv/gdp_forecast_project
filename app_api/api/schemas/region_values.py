from typing import Any, List

from pydantic import BaseModel


class UniqueRegions(BaseModel):
    values: List[str]

class CountriesPerRegion(BaseModel):
    region_country_list: List[str]