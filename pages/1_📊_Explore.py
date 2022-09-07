import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(page_title="Explore", page_icon="📊")
st.markdown("# Explore Dataset")

# Retrieving data
url = 'https://drive.google.com/file/d/15EX86AjdObYhay_I9NQf1_M4f_Tfdq2C/view?usp=sharing'
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)

#formatting
# df['Fuel Tank Capacity'] = df['Fuel Tank Capacity'].astype(int)
# df['Starting Price'] = df['Starting Price'].astype('int32')
# df['Ending Price'] = df['Ending Price'].astype(int)
# df['Max Torque (Nm)'] = df['Max Torque (Nm)'].astype(int)
# df['Max Power (BHP)'] = df['Max Power (BHP)'].astype(int)

#CLEANING DATA
#Create Brand column
df['Car Name'] = df['Car Name'].str.replace('Land Rover', 'Land-Rover')
df['Car Name'] = df['Car Name'].str.replace('Aston Martin', 'Aston-Martin')
df['Car Name'] = df['Car Name'].str.replace('Rolls Royce', 'Rolls-Royce')
df['Car Name'] = df['Car Name'].str.replace('Strom Motors', 'Strom-Motors')
df['Brand'] = df['Car Name'].str.split(' ').str[0]

#Clean Car Name column
df['Car Name'] = [" ".join(x) for x in df['Car Name'].str.split(' ').str[1:]]

#Clean Reviews Count column
reviews = df['Reviews Count'].str.replace(' reviews', '')
reviews = reviews.str.replace(' review', '')
df['Reviews Count'] = reviews

#Replace NaN with 2 and change from float to int in Seating Capacity column
df['Seating Capacity'].fillna(2, inplace=True)
df['Seating Capacity'] = df['Seating Capacity'].apply(lambda x: int(x))

#Convert Starting and Ending Prie to USD
df['Starting Price'] = df['Starting Price'].map(lambda x: x/80)
df['Ending Price'] = df['Ending Price'].map(lambda x: x/80)


#GROUPING BY BRANDS AND MEAN
df_mean = df.groupby(['Brand']).mean()


#METRICS
col1, col2, col3 = st.columns(3)
col1.metric("Brand Listed", len(df_mean.index))
col2.metric("Cars Listed", len(df))
col3.metric("Average Rating", float("{:.2f}".format(df['Rating'].mean())))

#RAW DATA
st.subheader('Raw Data')
st.dataframe(df.style.set_precision(2))

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