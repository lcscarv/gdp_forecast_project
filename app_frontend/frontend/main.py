import requests

import streamlit as st

from settings import API_URL, TITLE
from components import build_data_plot,build_comparison_plot_general, build_comparison_plot_groups, build_comparison_plot_regions
from functions import preprocess_string

st.set_page_config(page_title=TITLE,layout="wide")
st.title(TITLE)

tabs = st.tabs(['Countries','Economic Groups','Regions'])

Countries = tabs[0]
Economic_groups = tabs[1]
Regions = tabs[2]

with Countries:
    

    # Create dropdown for country selection.
    country_response = requests.get(API_URL / "countries_values")

    country = preprocess_string(st.selectbox(
        label="Gross domestic product (GDP) is the standard measure of the value added created \
            through the production of goods and services in a country during a certain period. \
             Annual percent change in real GDP shows how much higher or lower it is relative to the previous year. \
                 Select a country to check its predicted GDP annual percent change for 2024 to 2028.",
                
        options=country_response.json().get("values", []),
    ))
    
    # Check if country have values listed, then create plot for data.
    if country:
        st.plotly_chart(build_data_plot(country))
    
    c1, c2 = st.columns(2,gap="medium")
    c1.plotly_chart(build_data_plot('world',width=430,title = "World GDP Annual Percent Change",legend=False))
    c2.plotly_chart(build_comparison_plot_general())
	 
    

with Economic_groups:
    group_response = requests.get(API_URL / "groups_values")
    
    
    group = preprocess_string(st.selectbox(
        label="Gross domestic product (GDP) is the standard measure of the value added created \
            through the production of goods and services in a country during a certain period. \
             Annual percent change in real GDP shows how much higher or lower it is relative to the previous year. \
                 Select a Economic Group to check its predicted GDP annual percent change for 2024 to 2028, \
                     and a country for the specified group below.",
                
        options=group_response.json().get("values", []),
    ))
    country_response = requests.get(API_URL / "predictions" /"groups"/group /"countries")
    
    if group:
        st.plotly_chart(build_data_plot(group))
    c1, c2 = st.columns(2,gap="medium")
    
    with c1:
        country = preprocess_string(st.selectbox(
        label = 'Selection for country in specified group',
        options=country_response.json().get("country_list", []),))
        
        st.plotly_chart(build_data_plot(country,width=430,title = "Country GDP Annual Percent Change",legend=False))
    
    c2.plotly_chart(build_comparison_plot_groups(group))

with Regions:
    region_response = requests.get(API_URL / "regions_values")
    
    
    region = preprocess_string(st.selectbox(
        label="Gross domestic product (GDP) is the standard measure of the value added created \
            through the production of goods and services in a country during a certain period. \
             Annual percent change in real GDP shows how much higher or lower it is relative to the previous year. \
                 Select a Region to check its predicted GDP annual percent change for 2024 to 2028.",
                
        options=region_response.json().get("values", []),
    ))
    country_response = requests.get(API_URL / "predictions" /"regions"/region /"countries")
    
    if region:
        st.plotly_chart(build_data_plot(region))
    c1, c2 = st.columns(2,gap="medium")
    
    with c1:
        country = preprocess_string(st.selectbox(
        label = 'Selection for country in specified region',
        options=country_response.json().get("region_country_list", []),))
        
        st.plotly_chart(build_data_plot(country,width=430,title = "Country GDP Annual Percent Change",legend=False))
    
    c2.plotly_chart(build_comparison_plot_regions(region))
    
    
    
    
#    # Create dropdown for consumer type selection.
#    consumer_type_response = requests.get(API_URL / "consumer_type_values")
#
#    consumer_type = st.selectbox(
#        label="The consumer type is the Industry Code DE35 which is owned \
#            and maintained by Danish Energy, a non-commercial lobby \
#                organization for Danish energy companies. \
#                    The code is used by Danish energy companies.",
#        options=consumer_type_response.json().get("values", []),
#    )
