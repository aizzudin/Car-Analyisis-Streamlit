import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Welcome import df

st.set_page_config(page_title="Explore", page_icon="📊")
st.markdown("# Explore Dataset")


#GROUPING BY BRANDS AND MEAN
df_mean = df.groupby(['Brand']).mean()

#METRICS
col1, col2, col3 = st.columns(3)
col1.metric("Brand Listed", len(df_mean.index))
col2.metric("Cars Listed", len(df))
col3.metric("Average Rating", float("{:.2f}".format(df['Rating'].mean())))



#Graph 1 with price limiter
index = df_mean.index
start_p = df_mean['Starting Price']
end_p = df_mean['Ending Price']
st.subheader('Explore Cars Within Your Budgets')
price_limiter = st.slider("Price Range", value=[0,700000], step=50000)

fig, ax = plt.subplots(figsize=[10,10])
ax.barh(range(len(index)), width=[h-b for h, b in zip(start_p, end_p)], left=start_p, align='center', color='#ef476f', zorder=3)
plt.yticks(range(len(index)), index)
plt.grid(zorder=0, color="#e5e5e5")
plt.title("Average Price Range of Car Brands ($)")
plt.xlim(price_limiter[0],price_limiter[1])

plt.tight_layout()
st.pyplot(fig)

#SELECT CAR WITHIN BRANDS
#Create brand list
brand_cars = df['Brand'].unique()

#Create df for car brands and car name
brand_and_carname = pd.DataFrame([list(x) for x in df.groupby(['Brand', 'Car Name']).count().index])
brand_and_carname.rename({0:'Brand', 1:'Name'}, axis=1, inplace=True)

#User brand input
st.subheader('Look at cars from your favourite brands')
pick = st.selectbox('Select a car manufacturer:', brand_cars)

cars_result = df[df['Brand'] == pick].reset_index()[['Car Name', 'Starting Price', 'Ending Price']]

st.write(f'Listed cars from {pick} brand are:')
st.table(cars_result.style.set_precision(2))



#VIEW CAR SPECIFICATIONS
#Create car name list
name_cars = df['Car Name'].unique()

#User car name input
selected_car = st.selectbox('Select a car: ', name_cars)
car_name_result = df[df['Car Name'] == selected_car][['Car Name','Brand','Engine Displacement (cc)', 'Fuel Type', 'TransmissionType', 'Seating Capacity', 'Body Type']]

st.write(f'Specification of {selected_car} as below:')
st.table(car_name_result)
