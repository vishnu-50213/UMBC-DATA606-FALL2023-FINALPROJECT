import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import plotly.express as px

# Function to train the neural network
def train_neural_network(X_train, y_train):
    tf.random.set_seed(42)
    model = Sequential()
    model.add(Dense(10, activation='relu', input_dim=X_train.shape[1]))
    model.add(Dense(20, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(optimizer='adam', loss='mse', metrics=['mae', 'mse'])

    epochs = 25
    history = model.fit(X_train, y_train, epochs=epochs, validation_split=0.2, batch_size=128)

    return model, history

# Function to make predictions
def make_predictions(model, scaler, user_input):
    user_input_scaled = scaler.transform(user_input.astype('float32'))
    prediction = model.predict(user_input_scaled)[0][0]
    return prediction

df = pd.read_csv('/Users/vishnuken49gmail.com/Desktop/streamlit/Data/rideshare_kaggle.csv')
# Preprocessing: Removing null values and some columns
df = df.dropna()
df = df.drop(['id', 'timezone', 'timestamp', 'visibility.1'], axis=1)
# subseting data based on weather balance
num_instances_per_short_summary_class = 6000
df_temp = []

for short_summary_class in df['short_summary'].unique():
    temp = df[df['short_summary'] == short_summary_class].sample(n=num_instances_per_short_summary_class, random_state=42)
    df_temp.append(temp)

df_small = pd.concat(df_temp)

df1 = df_small[['price', 'distance', 'surge_multiplier', 'temperatureLow', 'apparentTemperatureLow', 'precipIntensityMax', 'source', 'destination', 'cab_type', 'name']]

# Ensure 'price' column is numeric
df1['price'] = pd.to_numeric(df1['price'], errors='coerce')

# Check for missing values
missing_values = df1.isnull().sum()
if missing_values.any():
    st.warning("There are missing values in the dataset. Please handle or impute them.")

# Extract continuous and categorical columns
continuous_columns = df1.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_columns = df1.select_dtypes(include=['object', 'category']).columns.tolist()

# Generate dummy variables for categorical columns, including null values
dummy_features = pd.get_dummies(df1[cat_columns], drop_first=True, dummy_na=True)

# Concatenate dummy features with the original dataframe
df1 = pd.concat([df1, dummy_features], axis=1)

# Drop the original categorical columns
df1.drop(cat_columns, axis=1, inplace=True)

df1.rename(columns = {'source_nan':'source_Back Bay',"destination_nan":"destination_Back Bay","cab_type_nan":"cab_type_Lyft","name_nan":"name_Black"}, inplace = True)

X = df1.drop('price', axis=1)
y = df1['price']

# Ensure 'y' is numeric
y = pd.to_numeric(y, errors='coerce')

# Train a neural network model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=3)
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train the neural network
model, history = train_neural_network(X_train_scaled, y_train)

# Streamlit app
st.title('Neural Network Price Prediction')

# Sidebar for user input
st.sidebar.header('User Input')

# Date input
user_date = st.sidebar.date_input('Select Date', pd.to_datetime('today'))

# Time input
user_time = st.sidebar.time_input('Select Time', pd.to_datetime('12:00'))

# Source selection dropdown
selected_source = st.sidebar.selectbox('Select Source', df1.filter(like='source_').columns)

# Destination selection dropdown
selected_destination = st.sidebar.selectbox('Select Destination', df1.filter(like='destination_').columns)

# Cab type selection dropdown
selected_cab_type = st.sidebar.selectbox('Select Cab Type', df1.filter(like='cab_type_').columns)

# Name selection dropdown
selected_name = st.sidebar.selectbox('Select Name', df1.filter(like='name_').columns)

# Other feature inputs
user_input = {}
for feature in X.columns:
    if feature.startswith('source_') or feature.startswith('destination_') or feature.startswith('name_'):
        # Set the selected source, destination, and name to 1 and others to 0
        user_input[feature] = 1 if feature == selected_source or feature == selected_destination or feature == selected_name else 0
    elif feature.startswith('cab_type_'):
        # Set the selected cab_type to 1 and others to 0
        user_input[feature] = 1 if feature == f'cab_type_{selected_cab_type.lower()}' else 0
    elif feature in ['temperatureLow', 'precipIntensityMax']:
        # Sliders for temperature and precipitation intensity
        min_val = float(df1[feature].min())
        max_val = float(df1[feature].max())
        user_input[feature] = st.sidebar.slider(f'Select {feature}', min_val, max_val, min_val)
    else:
        # Sliders for other numerical features
        user_input[feature] = st.sidebar.slider(f'Select {feature}', float(df1[feature].min()), float(df1[feature].max()), float(df1[feature].mean()))
# Convert date and time to numerical representations
user_input['date'] = user_date.toordinal()  # Convert date to a numerical representation
user_input['time'] = user_time.hour * 60 + user_time.minute  # Convert time to minutes since midnight

# Make predictions
user_input_df = pd.DataFrame([user_input], columns=user_input.keys())

# Ensure the order of features matches the order used during fit
user_input_df = user_input_df[X.columns]

user_input_scaled = scaler.transform(user_input_df.astype('float32'))
prediction = make_predictions(model, scaler, user_input_df)

# Display predictions
st.subheader('Prediction')
st.write(f'Predicted Trip Fare: ${prediction:,.2f}')

# Line plot for training curves
st.subheader('Model Training Curves')

# Extract metrics from history
training_loss = history.history['loss']
validation_loss = history.history['val_loss']
training_mae = history.history['mae']
validation_mae = history.history['val_mae']

# Create a DataFrame for plotting
history_df = pd.DataFrame({
    'Epoch': range(1, len(training_loss) + 1),
    'Training Loss': training_loss,
    'Validation Loss': validation_loss,
    'Training MAE': training_mae,
    'Validation MAE': validation_mae
})

# Melt the DataFrame for easier plotting
history_melted = pd.melt(history_df, id_vars='Epoch', var_name='Metric', value_name='Value')

# Line plot for metrics
fig = px.line(history_melted, x='Epoch', y='Value', color='Metric',
              labels={'Value': 'Metric Value', 'Epoch': 'Epoch'},
              title='Model Training Curves')

# Display the plot
st.plotly_chart(fig)
