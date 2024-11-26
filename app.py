import streamlit as st
import pandas as pd
import plotly.express as px
from plotly import graph_objects as go

# Load the dataset
vehicles_us = pd.read_csv(r'C:\Users\sicol\whipdata\whipdata_r\vehicles_us.csv')

# Display a sample of the dataset
st.header("Sample of Vehicle Dataset")
st.write(vehicles_us.sample(10))

# Distribution of Odometer Readings Chart with Checkbox
st.header("Distribution of Odometer Readings (Below 500K Miles)")

# Initial filtering for odometer readings less than 400,000 miles
filtered_data = vehicles_us[vehicles_us['odometer'] < 400000]

# Checkbox for excluding "new" condition vehicles
exclude_new = st.checkbox("Exclude vehicles with 'new' condition")

if exclude_new:
    filtered_data = filtered_data[filtered_data['condition'] != 'new']

# Checkbox for excluding "like new" condition vehicles
exclude_likenew = st.checkbox("Exclude vehicles with 'like new' condition")

if exclude_likenew:
    filtered_data = filtered_data[filtered_data['condition'] != 'like new']

# Checkbox for excluding "good" condition vehicles
exclude_good = st.checkbox("Exclude vehicles with 'good' condition")

# Checkbox for excluding "excellent" condition vehicles
exclude_excellent = st.checkbox("Exclude vehicles with 'excellent' condition")

if exclude_excellent:
    filtered_data = filtered_data[filtered_data['condition'] != 'excellent']

if exclude_good:
    filtered_data = filtered_data[filtered_data['condition'] != 'good']

# Checkbox for excluding "fair" condition vehicles
exclude_fair = st.checkbox("Exclude vehicles with 'fair' condition")

if exclude_fair:
    filtered_data = filtered_data[filtered_data['condition'] != 'fair']

# Checkbox for excluding "salvage" condition vehicles
exclude_salvage = st.checkbox("Exclude vehicles with 'salvage' condition")

if exclude_salvage:
    filtered_data = filtered_data[filtered_data['condition'] != 'salvage']

# Create the histogram
fig_odometer = px.histogram(
    filtered_data,
    x='odometer',
    nbins=50,
    title='Distribution of Odometer Readings',
)

# Update layout
fig_odometer.update_layout(
    xaxis_title="Odometer (miles)",
    yaxis_title="Number of Listings",
    title_font_size=20,
    title_x=0.5,  # Center the title
    showlegend=True,  # Enable the legend
)

# Add mean and median lines
mean_odometer = filtered_data['odometer'].mean()
median_odometer = filtered_data['odometer'].median()

fig_odometer.add_vline(
    x=mean_odometer,
    line_width=2,
    line_dash="dash",
    line_color="black",
)

fig_odometer.add_vline(
    x=median_odometer,
    line_width=2,
    line_dash="dash",
    line_color="red",
)

# Add dummy traces for the legend
from plotly import graph_objects as go

fig_odometer.add_trace(
    go.Scatter(
        x=[None], y=[None], mode='lines',
        name="Mean Odometer", line=dict(color="black", dash="dash")
    )
)
fig_odometer.add_trace(
    go.Scatter(
        x=[None], y=[None], mode='lines',
        name="Median Odometer", line=dict(color="red", dash="dash")
    )
)

# Display the histogram
st.plotly_chart(fig_odometer)

# Chart: Distribution of Car Prices
st.header("Distribution of Car Prices (Below $100K)")
filtered_data_price = vehicles_us[vehicles_us['price'] < 100000]
fig_price = px.histogram(
    filtered_data_price,
    x='price',
    nbins=40,
    title='Distribution of Car Prices (Below $100K)',
)
fig_price.update_layout(
    xaxis_title='Car Price (USD)',
    yaxis_title='Number of Listings',
    title_font_size=20,
    title_x=0.5,
    showlegend=True
)
fig_price.update_traces(marker_color='blue', opacity=0.7)
st.plotly_chart(fig_price)

# Chart: Price vs Odometer by Condition
st.header("Price vs Odometer by Condition")
filtered_data_scatter = vehicles_us[(vehicles_us['price'] < 100000) & (vehicles_us['odometer'] < 400000)]
fig_scatter = px.scatter(
    filtered_data_scatter,
    x='odometer',
    y='price',
    color='condition',
    title='Price vs Odometer by Condition',
    labels={'odometer': 'Odometer (miles)', 'price': 'Price (USD)'},
    hover_data=['model']
)
fig_scatter.update_traces(marker=dict(opacity=0.6, size=5))
fig_scatter.update_layout(
    xaxis_title='Odometer (miles)',
    yaxis_title='Price (USD)',
    title_font_size=20,
    title_x=0.5,
    template='plotly_white'
)
st.plotly_chart(fig_scatter)

# Chart: Price vs Vehicle Year by Condition
st.header("Price vs Vehicle Year by Condition")
current_year = 2024
vehicles_us['age'] = current_year - vehicles_us['model_year']
filtered_data_year = vehicles_us[(vehicles_us['age'] < 65) & (vehicles_us['price'] < 100000)]
fig_year = px.scatter(
    filtered_data_year,
    x='model_year',
    y='price',
    color='condition',
    title='Price vs Vehicle Year by Condition',
    labels={'model_year': 'Vehicle Year', 'price': 'Price (USD)'},
    hover_data=['model', 'model_year']
)
fig_year.update_traces(marker=dict(opacity=0.6, size=5))
fig_year.update_layout(
    xaxis_title='Vehicle Year',
    yaxis_title='Price (USD)',
    title_font_size=20,
    title_x=0.5,
    template='plotly_white'
)
st.plotly_chart(fig_year)