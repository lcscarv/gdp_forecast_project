from typing import List, Any

from pydantic import BaseModel
from datetime import datetime
    
class PredictionResultsByCountry(BaseModel):
    year: List[datetime]
    gdp_index: List[float]
    preds_year: List[datetime]
    preds_gdp_index: List[float]
class PredictionResultsByGroup(BaseModel):
    year: List[datetime]
    gdp_index: List[float]
    preds_year: List[datetime]
    preds_gdp_index: List[float]

class PredictionResultsByRegion(BaseModel):
    year: List[str]
    gdp_index: List[float]
    preds_year: List[str]
    preds_gdp_index: List[float]