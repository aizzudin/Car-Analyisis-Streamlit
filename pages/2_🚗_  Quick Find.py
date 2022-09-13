import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Welcome import df

st.set_page_config(page_title="Quick Find", page_icon="🚗")


st.sidebar.header("Find Your Car")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)


input_Brand = st.multiselect(
     'Select Brands You Prefer:',
     np.append(['All'], df['Brand'].unique()))

if 'All' in input_Brand:
    input_Brand = df['Brand'].unique()



input_fuelType = st.radio(
     "Select Fuel Type:",
     ('Petrol', 'Diesel', 'All'))

if input_fuelType == 'All':
    input_fuelType = ['Petrol', 'Diesel']


cc_limiter = st.slider("Engine CC:", value=[0,7000], step=500)













st.write(df.query(f"`Brand` in @input_Brand and `Fuel Type` == @input_fuelType and `Engine Displacement (cc)` >= @cc_limiter[0] and `Engine Displacement (cc)` <= @cc_limiter[1]").style.set_precision(2))