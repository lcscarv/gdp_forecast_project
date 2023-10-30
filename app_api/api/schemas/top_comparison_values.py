from typing import List, Any

from pydantic import BaseModel
from datetime import datetime

class TopFiveCountries(BaseModel):
    
    countries_names: List[str]
    avg_gdp: List[float]
    
class TopFivePerRegion(BaseModel):

    countries_names: List[str]
    avg_gdp: List[float]
    
class TopFivePerGroup(BaseModel):
    
    countries_names: List[str]
    avg_gdp: List[float]
