from typing import List
import requests
from datetime import datetime

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from functions import endpoint_decorator

from settings import API_URL


def build_data_plot(country: str, width = None, title = None, legend = None):
    """
    Build plotly graph for data.
    """

    # Get predictions from API.
    response = requests.get(
        API_URL / "predictions" / f"{country}" , verify=False
    )
    if response.status_code != 200:
        # If the response is invalid, build empty dataframes in the proper format.
        train_df = build_dataframe([], [])
        preds_df = build_dataframe([], [])

        title = "NO DATA AVAILABLE FOR THE GIVEN COUNTRY"
    else:
        json_response = response.json()

        # Build DataFrames for plotting.
        year = json_response.get("year")
        gdp_index = json_response.get("gdp_index")
        pred_year = json_response.get("preds_year")
        pred_gdp_index = json_response.get("preds_gdp_index")

        train_df = build_dataframe(year, gdp_index)
        preds_df = build_dataframe(pred_year, pred_gdp_index)

    if width == None:
        width = 1000
    if title == None:
        title = "GDP Annual Percent Change"
    if legend == None:
        legend = True
    # Create plot.
    fig = go.Figure()
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(family="Arial", size=16),
        ),
        showlegend=legend,
        width = width,
    )
    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="GDP Index")
    fig.add_scatter(
        x=train_df["year"],
        y=train_df["gdp_index"],
        name="Observations",
        line=dict(color="#C4B6B6"),
        hovertemplate="<br>".join(["Year: %{x}", "GDP Change: %{y} %"]),
    )
    fig.add_scatter(
        x=preds_df["year"],
        y=preds_df["gdp_index"],
        name="Predictions",
        line=dict(color="#FFC703"),
        hovertemplate="<br>".join(["Year: %{x}", "GDP Change: %{y} %"]),
    )

    return fig

def build_comparison_plot(endpoint):
    """
    Build plotly horizontal graph for top 5 comparison.
    """

    # Get predictions from API.
    response = requests.get(
        endpoint,verify=False
    )
    if response.status_code != 200:
        # If the response is invalid, build empty dataframes in the proper format.
        top_5_dict = {}

        title = "NO DATA AVAILABLE"
    else:
        json_response = response.json()
        
        top_5_dict = {k:v for (k,v) in zip(json_response.get('countries_names'),json_response.get('avg_gdp'))}

    # Create plot.
    percentage_text = [f'{p:.2f}%' for p in top_5_dict.values()]
    fig = go.Figure(
            go.Bar(
                x=[30]*5,
                y=list(top_5_dict.keys()),
                text=percentage_text,
                textposition="inside",
                textfont=dict(color="white"),
                orientation="h",
                marker_color="black",
                opacity = 0.5
            )
    )

    fig.add_trace(
        go.Bar(
            x=percentage_text,
            y=list(top_5_dict.keys()),
            orientation="h",
            marker_color = "#FFC703"
        )
    )
    fig.update_layout(title=dict(
                text='Top 5 Average GDP Growth in Next 4 Years',
                font=dict(family="Arial",color = "white"),
            ), 
                    barmode="overlay", showlegend=False, template="presentation",paper_bgcolor = 'rgba(0, 0, 0, 0)', 
                    plot_bgcolor = 'rgba(0, 0, 0, 0)',font=dict(family="Arial", size=17),width=400)
    fig.update_yaxes(
        tickmode="array",
        categoryorder="total ascending",
        tickvals=list(top_5_dict.keys()),
        ticktext=list(top_5_dict.keys()),
        ticklabelposition="inside",
        tickfont=dict(color="white"),
    )
    fig.update_xaxes(range=[0, 30], visible=False)

    return fig

def build_comparison_plot_general():
    endpoint = f"{API_URL}{'/predictions/TopFiveCountries'}"
    
    return build_comparison_plot(endpoint)

def build_comparison_plot_groups(group):
    
    endpoint = f"{API_URL}{f'/predictions/groups/{group}/TopFivePerGroup'}"
    
    return build_comparison_plot(endpoint)

def build_comparison_plot_regions(region):
    
    endpoint = f"{API_URL}{f'/predictions/regions/{region}/TopFivePerRegion'}"
    
    return build_comparison_plot(endpoint)

def build_dataframe(year: List[datetime], gdp_index_values: List[float]):
    """
    Build DataFrame for plotting from timestamps and energy consumption values.

    Args:
        datetime_utc (List[int]): list of timestamp values in UTC
        values (List[float]): list of energy consumption values
    """

    df = pd.DataFrame(
        list(zip(year, gdp_index_values)),
        columns=["year", "gdp_index"],
    )
    df["year"] = pd.to_datetime(df["year"])

    # Resample to yearly frequency to make the data continuous.
    df = df.set_index("year")
    df = df.resample("Y").asfreq()
    df = df.reset_index()

    return df