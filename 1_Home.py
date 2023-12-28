import streamlit as st

st.set_page_config(
    page_title = 'Multipage App'
)

st.title('Explore the Dynamics of Ride Prices and Weather')


# Introduction
st.markdown(
    """
    <div style="padding: 30px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); color: #333; text-align: justify;">
        <h2 style="font-family: 'Montserrat', sans-serif; font-size: 28px; margin-bottom: 20px;">Dive into the Impact of Weather on Ride Prices</h2>
        <p style="font-family: 'Open Sans', sans-serif; font-size: 18px; line-height: 1.6;">
            Discover why Uber and Lyft prices fluctuate based on weather conditions. The interplay of factors, especially weather, plays a crucial role in shaping ride prices.
        </p>
        <p style="font-family: 'Open Sans', sans-serif; font-size: 18px; line-height: 1.6;">
            Rainy days and scorching heat influence user behavior, leading to increased demand and surge pricing. But it goes beyond that – different weather types impact ride duration, routes, and overall ride experiences.
        </p>
        <p style="font-family: 'Open Sans', sans-serif; font-size: 18px; line-height: 1.6;">
            Our extensive data on rides, prices, and weather is ready to unveil the intricate connection between weather conditions and ride prices.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)