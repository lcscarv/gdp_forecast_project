import gcsfs
from typing import Any, List

import pandas as pd
from fastapi import APIRouter, HTTPException
from .lists import regions,regions_dict, groups,groups_dict,world_list
from .functions import preprocess_string
from .schemas.health import Health
from .schemas.group_values import UniqueGroups,CountriesPerGroup
from .schemas.predictions import PredictionResultsByCountry, PredictionResultsByGroup, PredictionResultsByRegion
from .schemas.region_values import UniqueRegions, CountriesPerRegion
from .schemas.country_values import UniqueCountries
from .schemas.top_comparison_values import TopFiveCountries,TopFivePerGroup,TopFivePerRegion
from .config import get_settings


fs = gcsfs.GCSFileSystem(
    project=get_settings().GCP_PROJECT,
    token=get_settings().GCP_SERVICE_ACCOUNT_JSON_PATH,
)

api_router = APIRouter()


@api_router.get("/health", response_model=Health, status_code=200)
def health() -> dict:
    """
    Health check endpoint.
    """

    health_data = Health(
        name=get_settings().PROJECT_NAME, api_version=get_settings().VERSION
    )

    return health_data.dict()

@api_router.get(
    "/countries_values", response_model=UniqueCountries, status_code=200
)
def countries_values() -> List:
    """
    Retrieve groups based on list.
    """
    #countries = []
    #for country in world_list:
    #    countries.append(preprocess_string(country))
        
    return {"values": world_list}

@api_router.get(
    "/groups_values", response_model=UniqueGroups, status_code=200
)
def groups_values() -> List:
    """
    Retrieve groups based on list.
    """

    return {"values": groups}


@api_router.get("/regions_values", response_model=UniqueRegions, status_code=200)
def regions_values() -> List:
    """
    Retrieve regions.
    """

    return {"values": regions}

@api_router.get(
    #"/predictions/{area}/{consumer_type}",
    "/predictions/TopFiveCountries",
    response_model=TopFiveCountries,
    status_code=200,
)
async def get_top_five() -> Any:
    """
    Get all forecasted predictions.
    """

    # Download the data from GCS.
    preds_df = pd.read_parquet(
        f"{get_settings().GCP_BUCKET}/predictions.parquet", filesystem=fs
    )
    
    countries_dict = {preprocess_string(c):c for c in world_list}
    
    preds_df = preds_df[list(countries_dict.keys())]
    
    gdp_avg_dict = {country:preds_df[country].mean() for country in preds_df.columns}
        
    gdp_avg_sorted = sorted(gdp_avg_dict.items(), key=lambda x:x[1])
        
    converted_dict = dict(gdp_avg_sorted[-5:]) 
    
    top_5 = {countries_dict.get(k, k): v for k, v in converted_dict.items()}      

    # Prepare data to be returned.
    results = {'countries_names':list(top_5.keys()),
               'avg_gdp':list(top_5.values())}
    
    return results 


@api_router.get(
    #"/predictions/{area}/{consumer_type}",
    "/predictions/{country}",
    response_model=PredictionResultsByCountry,
    status_code=200,
)
async def get_predictions(country: str) -> Any:
    """
    Get forecasted predictions based on the given group.
    """

    # Download the data from GCS.
    train_df = pd.read_parquet(f"{get_settings().GCP_BUCKET}/gdp_ts.parquet", filesystem=fs)
    preds_df = pd.read_parquet(
        f"{get_settings().GCP_BUCKET}/predictions.parquet", filesystem=fs
    )       

    # Query the data for the given area and consumer type.

    try:
        train_df = train_df[str(country)]
        preds_df = preds_df[str(country)]
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail=f"No data found for the given group: {str(country)}",
        )

    if len(train_df) == 0 or len(preds_df) == 0:
        raise HTTPException(
            status_code=404,
            detail=f"No data found for the given group: {str(country)}",
        )

    # Return only the latest week of observations.

    # Prepare data to be returned.
    year = train_df.index.to_list()
    gdp_index = train_df.to_list()

    preds_year = preds_df.index.to_list()
    preds_gdp_index = preds_df.to_list()

    results = {
        "year": year,
        "gdp_index": gdp_index,
        "preds_year": preds_year,
        "preds_gdp_index": preds_gdp_index,
    }
    return results 

@api_router.get(
    #"/predictions/{area}/{consumer_type}",
    "/predictions/group",
    response_model=PredictionResultsByGroup,
    status_code=200,
)
async def get_predictions(group: str) -> Any:
    """
    Get forecasted predictions based on the given group.
    """

    # Download the data from GCS.
    train_df = pd.read_parquet(f"{get_settings().GCP_BUCKET}/gdp_ts.parquet", filesystem=fs)
    preds_df = pd.read_parquet(
        f"{get_settings().GCP_BUCKET}/predictions.parquet", filesystem=fs
    )
    for g in groups_dict.get(group):
        for i,country in enumerate(g):
            g[i] = preprocess_string(country)
            

    # Query the data for the given area and consumer type.

    try:
        train_df = train_df[groups_dict.get(group)]
        preds_df = preds_df[groups_dict.get(group)]
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail=f"No data found for the given group: {group}",
        )

    if len(train_df) == 0 or len(preds_df) == 0:
        raise HTTPException(
            status_code=404,
            detail=f"No data found for the given group: {group}",
        )

    # Return only the latest week of observations.
    train_df = train_df.sort_index()

    # Prepare data to be returned.
    year = train_df.index.get_level_values("year").to_list()
    gdp_index = train_df["gdp_index"].to_list()

    preds_year = preds_df.index.get_level_values("year").to_list()
    preds_gdp_index = preds_df["gdp_index"].to_list()

    results = {
        "year": year,
        "gdp_index": gdp_index,
        "preds_year": preds_year,
        "preds_gdp_index": preds_gdp_index,
    }

    return results

@api_router.get(
    #"/predictions/{area}/{consumer_type}",
    "/predictions/groups/{group}/countries",
    response_model=CountriesPerGroup,
    status_code=200,
)
async def get_countries_in_group(group: str) -> Any:
    """
    Get countries based on the given group.
    """
    try:
        countries_in_group = groups_dict.get(group)
        result = list(countries_in_group)
    except:
        print("No countries found for specified group")
        result = []

    results = {
        "country_list": result
    }
    return results 

@api_router.get(
    #"/predictions/{area}/{consumer_type}",
    "/predictions/groups/{group}/TopFivePerGroup",
    response_model=TopFivePerGroup,
    status_code=200,
)
async def get_top_five_per_group(group) -> Any:
    """
    Get all forecasted predictions.
    """

    # Download the data from GCS.
    preds_df = pd.read_parquet(
        f"{get_settings().GCP_BUCKET}/predictions.parquet", filesystem=fs
    )
    
    countries_groups_dict = {preprocess_string(c):c for c in groups_dict[group]}
         
    preds_df = preds_df[countries_groups_dict.keys()]
    
    gdp_avg_dict = {country:preds_df[country].mean() for country in preds_df.columns}
        
    gdp_avg_sorted = sorted(gdp_avg_dict.items(), key=lambda x:x[1])
        
    converted_dict = dict(gdp_avg_sorted[-5:]) 
    
    top_5 = {countries_groups_dict.get(k, k): v for k, v in converted_dict.items()}     

    # Prepare data to be returned.
    results = {'countries_names':list(top_5.keys()),
               'avg_gdp':list(top_5.values())}
    
    return results 

@api_router.get(
    #"/predictions/{area}/{consumer_type}",
    "/predictions/region",
    response_model=PredictionResultsByRegion,
    status_code=200,
)
async def get_predictions(region: str) -> Any:
    """
    Get forecasted predictions based on the given Region.
    """

    # Download the data from GCS.
    train_df = pd.read_parquet(f"{get_settings().GCP_BUCKET}/gdp_ts.parquet", filesystem=fs)
    preds_df = pd.read_parquet(
        f"{get_settings().GCP_BUCKET}/predictions.parquet", filesystem=fs
    )
    for r in regions_dict.get(region):
        for i,country in enumerate(r):
            r[i] = preprocess_string(country)

    # Query the data for the given area and consumer type.

    try:
        train_df = train_df[regions_dict.get(region)]
        preds_df = preds_df[regions_dict.get(region)]
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail=f"No data found for the given region : {region}",
        )

    if len(train_df) == 0 or len(preds_df) == 0:
        raise HTTPException(
            status_code=404,
            detail=f"No data found for the given region : {region}",
        )

    # Return only the latest week of observations.
    train_df = train_df.sort_index()

    # Prepare data to be returned.
    year = train_df.index.get_level_values("year").to_list()
    gdp_index = train_df["gdp_index"].to_list()

    preds_year = preds_df.index.get_level_values("year").to_list()
    preds_gdp_index = preds_df["gdp_index"].to_list()

    results = {
        "year": year,
        "gdp_index": gdp_index,
        "preds_year": preds_year,
        "preds_gdp_index": preds_gdp_index,
    }

    return results

@api_router.get(
    #"/predictions/{area}/{consumer_type}",
    "/predictions/regions/{region}/TopFivePerRegion",
    response_model=TopFivePerRegion,
    status_code=200,
)
async def get_top_five_per_region(region) -> Any:
    """
    Get all forecasted predictions.
    """

    # Download the data from GCS.
    preds_df = pd.read_parquet(
        f"{get_settings().GCP_BUCKET}/predictions.parquet", filesystem=fs
    )
    
    if region in regions_dict:
        countries_regions_dict = {preprocess_string(c):c for c in regions_dict.get(region)}
         
    preds_df = preds_df[countries_regions_dict.keys()]
    
    gdp_avg_dict = {country:preds_df[country].mean() for country in preds_df.columns}
        
    gdp_avg_sorted = sorted(gdp_avg_dict.items(), key=lambda x:x[1])
        
    converted_dict = dict(gdp_avg_sorted[-5:])
    
    top_5 = {countries_regions_dict.get(k, k): v for k, v in converted_dict.items()}     

    # Prepare data to be returned.
    results = {'countries_names':list(top_5.keys()),
               'avg_gdp':list(top_5.values())}
    
    return results 

@api_router.get(
    #"/predictions/{area}/{consumer_type}",
    "/predictions/regions/{region}/countries",
    response_model=CountriesPerRegion,
    status_code=200,
)
async def get_countries_in_region(region: str) -> Any:
    """
    Get forecasted predictions based on the given group.
    """
    try:
        countries_in_region = regions_dict.get(region)
    except:
        print("No countries found for specified region")
    results = {
        "region_country_list": list(countries_in_region),
    }
    
    return results 