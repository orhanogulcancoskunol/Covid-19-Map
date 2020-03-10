#import streamlit as st
import pandas as pd
import folium
from folium.plugins import FastMarkerCluster

deathlocs = pd.read_csv("datas.csv")

folium_map = folium.Map(tiles='CartoDB dark_matter')


FastMarkerCluster(data=list(zip(deathlocs['lat'].values, deathlocs['lon'].values))).add_to(folium_map)
folium.LayerControl().add_to(folium_map)
folium_map.save('index.html')

#st.map(deathlocs)
