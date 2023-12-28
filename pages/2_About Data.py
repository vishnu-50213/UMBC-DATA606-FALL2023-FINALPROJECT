import streamlit as st

st.markdown(
    """
    <style>
        body {
            color: #2c3e50;
            background-color: #ecf0f1;
            font-family: 'Arial', sans-serif;
        }
        .container {
            background-color: #3498db;
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .header {
            color: #ecf0f1;
            font-size: 36px;
        }
        .subheader {
            color: #ecf0f1;
            font-size: 24px;
        }
        .markdown {
            text-align: justify;
            line-height: 1.6;
        }
        .link-button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #2ecc71;
            color: #ecf0f1;
            text-decoration: none;
            font-size: 18px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        .link-button:hover {
            background-color: #27ae60;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title 
st.title("About the Dataset")
st.markdown("<hr style='border: 2px solid #3498db;'>", unsafe_allow_html=True)

# introduction with a container
with st.container():
    st.markdown(
        """
        <p class='markdown'>
            <b>Welcome to the Uber and Lyft Dataset for Boston, MA.</b><br>
            This dataset offers a comprehensive collection of information pertaining to ride-sharing services in the vibrant city of Boston. Whether you're an analyst, data scientist, or enthusiast, this dataset provides a rich source of data for exploring and understanding the dynamics of Uber and Lyft operations in the Boston metropolitan area.
        </p>
        """,
        unsafe_allow_html=True
    )


st.header("Data Source")

#  markdown with container
with st.container():
    st.markdown(
        """
        - The dataset has been meticulously curated and compiled from various sources, including ride-sharing APIs, public datasets, and official reports. The data covers a period of time, allowing for temporal analyses and trend identification.
        """
    )

st.header("Key Features")

# markdown with container
with st.container():
    st.markdown(
        """
        - **Ride Details**: Explore a detailed breakdown of individual rides, including timestamps, pickup/drop-off locations, and trip durations.
        - **Pricing Information**: Gain insights into the pricing structures of Uber and Lyft services, including surge pricing during peak hours.
        - **Geographical Information**: Analyze the spatial distribution of rides and understand the areas with high demand for ride-sharing services.
        - **User Ratings**: Investigate user satisfaction levels through the dataset's user rating information for both Uber and Lyft.
        """
    )

st.header("Potential Use Cases")

# markdown with container
with st.container():
    st.markdown(
        """
        - **Transportation Planning**: Understand the patterns of ride demand to assist in urban planning and traffic management.
        - **Pricing Strategy Analysis**: Evaluate the effectiveness of different pricing strategies employed by Uber and Lyft.
        - **User Experience Research**: Investigate user preferences and behavior to enhance the overall ride-sharing experience.
        """
    )

st.header("Dataset Details")

# markdown with container
with st.container():
    st.markdown(
        """
        - **Size**: The dataset comprises 600K records, providing a substantial volume of data for in-depth analysis.
        - **Format**: Data is available in CSV format, ensuring compatibility with a wide range of data analysis tools and programming languages.
        - **Data Fields**: Refer to the dataset documentation for a comprehensive list of fields and their descriptions, ensuring clarity in your analyses.
        """
    )

# Acknowledgments with markdown
st.header("Acknowledgments")
st.markdown(
    """
    
        I would like to express my gratitude to the contributors and organizations that made this dataset possible. 
        Their efforts in collecting and sharing this data contribute significantly to the advancement of transportation research and analytics.
    
    """
)

# Link at the bottom with button
st.markdown(
    """
    <hr style='border: 2px solid #3498db;'>
    <a href='https://www.kaggle.com/datasets/brllrb/uber-and-lyft-dataset-boston-ma' class='link-button'>Explore the Dataset on Kaggle</a>
    """,
    unsafe_allow_html=True
)
