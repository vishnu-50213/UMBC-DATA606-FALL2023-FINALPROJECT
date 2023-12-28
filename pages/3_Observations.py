import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn import preprocessing


# Containers for different sections
dataset = st.container()
observations = st.container()
features = st.container()
# Load dataset
df = pd.read_csv('/Users/vishnuken49gmail.com/Desktop/streamlit/Data/rideshare_kaggle.csv')
# Preprocessing: Removing null values and some columns
df = df.dropna()
df = df.drop(['id', 'timezone', 'timestamp', 'visibility.1'], axis=1)

# Section: Dataset Overview

with dataset:
    st.header('Boston Uber and Lyft Ride Details')
    st.subheader('Sample data before preparing it for machine learning')
    st.write(df.head(5))

    # Data distribution among days
    st.subheader('Data distribution among days')
    fig = px.bar(data_frame=df.groupby('day').size().reset_index(name="counts").round(2), 
                 x='day', y="counts", barmode="group")
    fig.update(layout_showlegend=False)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    # Additional Plots
    con1 = st.container()


    with con1:
        # Pie chart for cab_type distribution
        st.subheader('Distribution of Cab Types')
        fig = px.pie(df, names='cab_type', labels=['Uber', 'Lyft'],
                     color='cab_type', color_discrete_map={'Uber': 'SpringGreen', 'Lyft': 'DodgerBlue'})
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        
    # Create an expander for the group options
    with st.expander("Balanced Features"):
        # Inside the expander, create a radio button to select the group
       selected_option = st.radio( 'select folowing options' ,["Car Type", "Starting Position"], key="group_selection")

        # Display plots based on the selected group
    if selected_option == "Car Type":
        # Bar chart for ride count per name
        st.subheader('Ride Count per Name')
        fig1 = px.bar(data_frame=df.groupby('name').size().reset_index(name="counts").round(2),
                    x='name', y="counts", color='name')
        fig1.update(layout_showlegend=False)
        st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

    elif selected_option == "Starting Position":
        # Bar chart for ride count per source
        st.subheader('Ride Count per Source')
        fig2 = px.bar(data_frame=df.groupby('source').size().reset_index(name="counts").round(2),
                    x='source', y="counts", color='source')
        fig2.update(layout_showlegend=False)
        st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
        
    st.subheader('Number of ride data I have from different weather types')
    fig = fig = px.bar(data_frame=df.groupby('short_summary').size().reset_index(name="counts").round(2).sort_values(by=['counts'], ascending=False), 
            x='short_summary', y="counts" ,
            color='short_summary')
    fig.update(layout_showlegend=False)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        ## Key observations
    st.header('Key Observations')
    st.markdown("* Data is well balanced, but there is an imbalance in weather situations.")
    st.markdown("* Trips are evenly distributed every day, with noticeable distributions among different vehicles (Uber, Lyft).")
    

# Section: Observations
with observations:
    st.header('Critical Observations')

    # Calculate price per mile (PPM)
    df['PPM'] = df['price'].div(df['distance'])
    df['PPM'] = df['PPM'].round(2)

    # Container for observations
    con1 = st.container()
    con2 = st.container()

    with con1:
        # Average PPM for UberX with respect to weather type
        st.subheader('Average PPM for UberX with Respect to Weather Type')
        uberx_df = df[df['name'] == 'UberX']
        pivot_df_uberx = uberx_df.pivot_table(index=['name', 'short_summary'], values='PPM', aggfunc='mean').reset_index().round(2).sort_values(by=['PPM'], ascending=False)
        fig = px.bar(pivot_df_uberx, x='short_summary', y='PPM', color='short_summary',
                     title='Average PPM for UberX with Respect to Weather Type',
                     labels={'PPM': 'Average Price Per Mile', 'short_summary': 'Weather Type', 'name': 'Cab Type'},
                     text='PPM')
        fig.update(layout_showlegend=False)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    with con2:
        # Average PPM for UberX with respect to source
        st.subheader('Average PPM for UberX with Respect to Source')
        uberx_df = df[df['name'] == 'UberX']
        pivot_df_uberx = uberx_df.pivot_table(index=['name', 'source'], values='PPM', aggfunc='mean').reset_index().round(2).sort_values(by=['PPM'], ascending=False)
        fig = px.bar(pivot_df_uberx, x='source', y='PPM', color='source',
                     title='Average PPM for UberX with Respect to Source',
                     labels={'PPM': 'Average Price Per Mile', 'source': 'Source', 'name': 'Cab Type'},
                     text='PPM')
        fig.update(layout_showlegend=False)
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    
    st.markdown("Observing the data, a clear class difference in vehicles, starting with sharing luxury vehicles, was identified. This underscores the significance of cab type as a key feature in predicting prices.")
    st.markdown("A detailed examination of PPM with respect to various weather types (rain, fog, clear, etc.) revealed differences in UberX prices for each weather condition. Small changes in PPM, even in foggy conditions, signify Uber's consideration of driving conditions and driver availability concerning weather.")
    st.markdown("Extending the analysis to locations, it was observed that prices from stations are higher compared to normal values. This suggests that busy locations have an impact on prices.")

with features:
    Important_features = ['hour','day','month','distance','surge_multiplier','apparentTemperatureLow','temperatureLow','precipIntensityMax','source','destination','cab_type','name']
    st.markdown("""
    <div style="background-color:#f5f5f5; padding:10px; border-radius:5px;">
        <h2 style="color:#008080;">Important Features</h2>
        <p style="font-size:16px;">Here are the important features in the dataset:</p>
        <ul style="list-style-type:square; font-size:14px;">
            {}
        </ul>
    </div>
""".format(''.join(['<li>{}</li>'.format(feature) for feature in Important_features])), unsafe_allow_html=True)
    st.markdown("""
    ### Note
    This list of important features is based on the analysis performed during feature engineering and overall data exploration.
    Adjustments to the list may be made based on further insights or modeling requirements.
""")

