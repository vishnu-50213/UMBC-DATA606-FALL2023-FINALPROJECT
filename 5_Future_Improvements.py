# future_improvements_and_challenges.py
import streamlit as st

# Streamlit app
st.title('Future Improvements and Challenges')

## Future Improvements
st.header('Future Improvements')

### 1. Feature Engineering and Model Optimization
st.subheader('1. Feature Engineering and Model Optimization')
st.markdown("The introduction of the Price Per Mile (PPM) variable is a valuable step. However, exploring additional derived features or engineering new variables based on domain knowledge could enhance model predictive power.")

### 2. Handling Location Data
st.subheader('2. Handling Location Data')
st.markdown("While considering pick locations as categorical in the current analysis, future improvements could involve a more nuanced approach. In real-time scenarios, converting locations into continuous variables, such as coordinates or geospatial features, might provide richer insights.")

### 3. Balancing Categorical and Continuous Features
st.subheader('4. Balancing Categorical and Continuous Features')
st.markdown("The dilemma between using only continuous features or only categorical features in regression models presents challenges. Further investigation into advanced encoding techniques and feature selection methods could strike a balance and improve model accuracy.")

## Challenges Faced
st.header('Challenges Faced')

### 1. Variable Selection Dilemma
st.subheader('1. Variable Selection Dilemma')
st.markdown("Balancing the choice between using continuous features or categorical features in regression models posed a challenge. The need to choose between distance and surge multiplier (continuous) versus categorical variables like cab type led to thoughtful considerations.")

### 2. Model Complexity and Accuracy
st.subheader('2. Model Complexity and Accuracy')
st.markdown("Opting for multiple regressions based on cab names addressed certain challenges but raised concerns about model complexity and potential accuracy trade-offs. The need to achieve high accuracy while considering the diverse price ranges associated with different cab names presented difficulties.")

### 3. Decision on Encoding Method
st.subheader('3. Decision on Encoding Method')
st.markdown("The decision to use one-hot encoding for regression models was made to preserve categorical information. However, managing the resulting increase in dimensionality and potential challenges related to model interpretability and computation resources should be addressed in future iterations.")

# Thank You
st.header('Thank You!')
st.markdown("These insights and challenges provide a foundation for future enhancements and learning opportunities. The iterative process of refining models and methodologies is essential for building robust and accurate predictive systems. Thank you for your attention to these findings and considerations.")
