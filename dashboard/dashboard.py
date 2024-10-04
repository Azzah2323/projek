import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("all_data.csv" ) 

# Convert 'dteday_x' to datetime for easier filtering
data['dteday_x'] = pd.to_datetime(data['dteday_x'])

# Sidebar filters
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start date", data['dteday_x'].min())
end_date = st.sidebar.date_input("End date", data['dteday_x'].max())

# Filter data based on selected date range
filtered_data = data[(data['dteday_x'] >= pd.to_datetime(start_date)) & (data['dteday_x'] <= pd.to_datetime(end_date))]

# Main dashboard
st.title("Bike Sharing")

# Line chart for weather metrics
st.subheader("Weather Metrics Over Time")
weather_metrics = st.multiselect("Select metrics to display", ['temp_x', 'atemp_x', 'hum_x', 'windspeed_x'], default=['temp_x', 'hum_x'])

st.line_chart(filtered_data.set_index('dteday_x')[weather_metrics])

# Bar chart for casual and registered riders
st.subheader("Rider Counts")
rider_type = st.radio("Select rider type", ('Casual', 'Registered'))
if rider_type == 'Casual':
    st.bar_chart(filtered_data.set_index('dteday_x')['casual_x'])
else:
    st.bar_chart(filtered_data.set_index('dteday_x')['registered_x'])

# Additional filter for season
season_filter = st.selectbox("Select Season", options=[1, 2, 3, 4], format_func=lambda x: {1: "Winter", 2: "Spring", 3: "Summer", 4: "Fall"}[x])

# Apply season filter
season_data = filtered_data[filtered_data['season_x'] == season_filter]
st.write(f"Data for season: {season_filter}")
st.line_chart(season_data.set_index('dteday_x')[['cnt_x']])

# Show total riders for the selected period
st.write(f"Total riders in the selected period: {season_data['cnt_x'].sum()}")