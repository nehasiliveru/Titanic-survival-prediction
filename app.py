import streamlit as st
import joblib
import pandas as pd

# Load the ML model
model = joblib.load('titanic_model.pkl')

# Add custom CSS using Streamlit's markdown to change text color and font size
st.markdown("""
    <style>
        /* Change the color and font size of the title and description text */
        .stTitle, .stHeader {
            color: white !important;
        }

        /* Increase font size for the description text */
        .stMarkdown {
            color: white !important;
            font-size: 20px !important;  /* Increase the font size */
        }

        /* Customize the prediction result's color */
        .stSuccess {
            color:white  !important; 
            font-size: 20px !important;
            font-weight: bold;
        }

        .stError {
            color: maroon !important;  /* Bright red color */
            font-size: 20px !important;
            font-weight: bold;
        }

        .stInfo {
            color: #17a2b8 !important;  /* Bright blue color */
            font-size: 20px !important;
            font-weight: bold;
        }

        /* Ensure the background image is properly applied */
        .stApp {
            background-image: url('https://img.freepik.com/premium-photo/titanic-ship-braving-stormy-seas-with-dramatic-seascape-background-concept-titanic-ship-stormy-seas-dramatic-seascape-background_918839-129885.jpg');  /* Replace with actual image URL */
            background-size: cover;
            background-position: center;
            height: 100vh;  /* Full viewport height */
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: -1;
        }

        /* Sidebar styling */
        .css-1d391kg .stSidebar .sidebar-content {
            background-color: rgba(44, 62, 80, 0.9);  /* Dark color with transparency */
            border-radius: 10px;
            color: white;
        }

        /* Styling for the predict button */
        .stButton>button {
            background-color: #28a745;  /* Green color */
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }

        .stButton>button:hover {
            background-color: #218838;  /* Darker green on hover */
        }

        /* Font customization */
        body {
            font-family: 'Arial', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("Titanic Survival Predictor")
st.write("This app predicts whether a passenger is likely to survive the Titanic disaster based on their information.")

# Sidebar for user inputs
st.sidebar.header("Passenger Information")
pclass = st.sidebar.selectbox("Passenger Class (Pclass)", [1, 2, 3], help="Select the passenger's class")
age = st.sidebar.slider("Age", 0, 100, 25, help="Select the passenger's age")
sibsp = st.sidebar.slider("Number of Siblings/Spouses aboard", 0, 8, 0)
parch = st.sidebar.slider("Number of Parents/Children aboard", 0, 8, 0)
fare = st.sidebar.slider("Fare", 0.0, 500.0, 50.0, step=0.1)
gender = st.sidebar.radio("Gender", ['male', 'female'], help="Select the passenger's gender")
embarked = st.sidebar.radio("Embarked", ['C', 'Q', 'S'], help="Port of embarkation")

# Encode categorical inputs
male = 1 if gender == 'male' else 0
embarked_Q = 1 if embarked == 'Q' else 0
embarked_S = 1 if embarked == 'S' else 0

# Create input data
input_data = pd.DataFrame({
    'Pclass': [pclass],
    'Age': [age],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Fare': [fare],
    'male': [male],
    'Q': [embarked_Q],
    'S': [embarked_S]
})

# Prediction
if st.button("Predict Survival"):
    prediction = model.predict(input_data)
    result = "Survived" if prediction[0] == 1 else "Did not survive"
    
    # Display the result with custom colors
    if prediction[0] == 1:
        st.markdown(f'<p class="stSuccess">The passenger is likely to: {result}</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p class="stError">The passenger is likely to: {result}</p>', unsafe_allow_html=True)
