import pandas as pd
import streamlit as st
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

df = pd.read_csv("covid_19_data.csv")

geolocator = Nominatim(user_agent="Corona Check", timeout=None)
#geocode= RateLimiter(geolocator.geocode, min_delay_seconds=1)

#df['location'] = df['Province/State'].apply(geocode)

#df['point'] = df['location'].sample(n=10, random_state=1).apply(lambda loc: tuple(loc.point) if loc else None)

#df['point'].to_csv(r'datas.csv')

#st.map(df['point'])

lats = []
longs = []
countries = []
i=0

for item in df['Country/Region'].values:
    if item not in countries:
        finali = geolocator.geocode(item)
        if finali is not None:
            lats.append(finali.latitude)
            longs.append(finali.longitude)
            i = i + 1
        print(i)
        countries.append(item)


deathlocs = pd.DataFrame()

deathlocs['lat'] = lats
deathlocs['lon'] = longs

deathlocs.to_csv(r'datas.csv')
