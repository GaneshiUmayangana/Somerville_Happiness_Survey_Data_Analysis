import numpy as np
import pickle
import pandas as pd
import streamlit as st

# Load the trained model with error handling
try:
    with open("E:\\FourthYear\\ST 4035 - Data Science\\Group_Project\\App\\model.pkl", "rb") as pickle_in:
        best_dt_model = pickle.load(pickle_in)
except Exception as e:
    st.error(f"Error loading model: {e}")

# Function to predict happiness using the loaded model
def predict_happiness(features):
    features_df = pd.DataFrame([features], columns=[
        'LifeSatisfaction5ptnum', 'SomervilleSatisfaction5ptnum', 'NeighborhoodSatisfaction5ptnum',
        'Service311QualitySatisfaction5ptnum', 'CityServicesQualitySatisfaction5ptnum', 'CrimeViolenceConcern3ptnum',
        'BluebikesSatisfaction5ptnum', 'IncomePerNumberInHousehold', 'BusBicycleLanesSatisfaction5ptnum',
        'ParksProximitySatisfaction5ptnum', 'HousingConditionSatisfaction5ptnum', 'GroceryProximitySatisfaction5ptnum',
        'NeighborsRelationshipSatisfaction5ptnum', 'CleanlinessNeighborhoodSatisfaction5ptnum', 
        'SevereWeatherResponseSatisfaction5ptnum', 'RentasPercentofIncome', 'RentMortgagePerBedroom', 
        'BeautyNeighborhoodSatisfaction5ptnum', 'GettingAroundConvenienceSatisfaction5ptnum',
        'CityServicesInformationAvailabilitySatisfaction5ptnum',
    ])
    prediction = best_dt_model.predict(features_df)
    return prediction[0]

def main():
    # Display an image at the top
    st.image("Happy.jpg", width=700)  # Adjust width as necessary
    # HTML for styling
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">HAPPINESS PREDICTOR</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Create input fields for each feature with appropriate scales
    LifeSatisfaction = st.slider("Life Satisfaction (1-5)", 1, 5)
    SomervilleSatisfaction = st.slider("Somerville Satisfaction (1-5)", 1, 5)
    NeighborhoodSatisfaction = st.slider("Neighborhood Satisfaction (1-5)", 1, 5)
    Service311QualitySatisfaction = st.slider("311 Service Quality Satisfaction (1-5)", 1, 5)
    CityServicesQualitySatisfaction = st.slider("City Services Quality Satisfaction (1-5)", 1, 5)
    CrimeViolenceConcern = st.slider("Crime Violence Concern (1-3)", 1, 3)
    BluebikesSatisfaction = st.slider("Bluebikes Satisfaction (1-5)", 1, 5)
    IncomePerNumberInHousehold = st.number_input("Income Per Number In Household", min_value=0)
    BusBicycleLanesSatisfaction = st.slider("Bus/Bicycle Lanes Satisfaction (1-5)", 1, 5)
    ParksProximitySatisfaction = st.slider("Parks Proximity Satisfaction (1-5)", 1, 5)
    HousingConditionSatisfaction = st.slider("Housing Condition Satisfaction (1-5)", 1, 5)
    GroceryProximitySatisfaction = st.slider("Grocery Proximity Satisfaction (1-5)", 1, 5)
    NeighborsRelationshipSatisfaction = st.slider("Neighbors Relationship Satisfaction (1-5)", 1, 5)
    CleanlinessNeighborhoodSatisfaction = st.slider("Cleanliness Neighborhood Satisfaction (1-5)", 1, 5)
    SevereWeatherResponseSatisfaction = st.slider("Severe Weather Response Satisfaction (1-5)", 1, 5)
    RentasPercentofIncome = st.number_input("Rent as Percent of Income", min_value=0.0, max_value=100.0)
    RentMortgagePerBedroom = st.number_input("Rent/Mortgage Per Bedroom", min_value=0)
    BeautyNeighborhoodSatisfaction = st.slider("Beauty Neighborhood Satisfaction (1-5)", 1, 5)
    GettingAroundConvenienceSatisfaction = st.slider("Getting Around Convenience Satisfaction (1-5)", 1, 5)
    CityServicesInformationAvailabilitySatisfaction = st.slider("City Services Information Availability Satisfaction (1-5)", 1, 5)

    # Gather inputs into a list in the correct order
    features = [
        LifeSatisfaction, SomervilleSatisfaction, NeighborhoodSatisfaction, Service311QualitySatisfaction,
        CityServicesQualitySatisfaction, CrimeViolenceConcern, BluebikesSatisfaction, IncomePerNumberInHousehold,
        BusBicycleLanesSatisfaction, ParksProximitySatisfaction, HousingConditionSatisfaction, 
        GroceryProximitySatisfaction, NeighborsRelationshipSatisfaction, CleanlinessNeighborhoodSatisfaction, 
        SevereWeatherResponseSatisfaction, RentasPercentofIncome, RentMortgagePerBedroom, 
        BeautyNeighborhoodSatisfaction, GettingAroundConvenienceSatisfaction, CityServicesInformationAvailabilitySatisfaction
    ]

    # When 'Predict' button is clicked
    if st.button("Predict"):
        result = predict_happiness(features)
        st.success(f"The predicted happiness status is: {'Unhappy' if result == 1 else 'Happy'}")

if __name__ == '__main__':
    main()
