import streamlit as st
import pandas as pd
import joblib

# 1. Load the trained model pipeline
model = joblib.load('house_price_model.pkl')

st.title("🏡 House Price Prediction App")
st.write("Enter the property details below and let the XGBoost model predict the estimated price!")

# 2. Sidebar inputs for property specifications
st.sidebar.header("Property Features")

gr_liv_area = st.sidebar.number_input("Above Grade Living Area (GrLivArea)", min_value=300, max_value=6000, value=1500)
overall_qual = st.sidebar.slider("Overall Material & Finish Quality (OverallQual)", min_value=1, max_value=10, value=6)
year_built = st.sidebar.number_input("Year Built", min_value=1800, max_value=2026, value=2005)
total_bsmt_sf = st.sidebar.number_input("Total Basement Square Feet (TotalBsmtSF)", min_value=0, max_value=3000, value=800)
first_flr_sf = st.sidebar.number_input("First Floor Square Feet (1stFlrSF)", min_value=300, max_value=4000, value=1000)
second_flr_sf = st.sidebar.number_input("Second Floor Square Feet (2ndFlrSF)", min_value=0, max_value=3000, value=500)
garage_cars = st.sidebar.selectbox("Garage Capacity (Cars)", [0, 1, 2, 3, 4], index=2)
lot_area = st.sidebar.number_input("Total Lot Area (LotArea)", min_value=1000, max_value=100000, value=10000)

neighborhood = st.sidebar.selectbox("Neighborhood", ['CollgCr', 'Veenker', 'Crawfor', 'NoRidge', 'Mitchel', 'Somerst', 'OldTown', 'BrkSide', 'Gilbert', 'NridgHt', 'NWAmes', 'Other'])
ms_zoning = st.sidebar.selectbox("MS Zoning Classification", ['RL', 'RM', 'C (all)', 'FV', 'RH'])
exterior_1st = st.sidebar.selectbox("Exterior Covering (Exterior1st)", ['VinylSd', 'MetalSd', 'Wd Sdng', 'HdBoard', 'BrkFace', 'Other'])
kitchen_qual = st.sidebar.selectbox("Kitchen Quality", ['Ex', 'Gd', 'TA', 'Fa'])

# Engineering features exactly like the training script
yr_sold = 2026
house_age = yr_sold - year_built
total_sf = total_bsmt_sf + first_flr_sf + second_flr_sf


input_data = pd.DataFrame({
    'GrLivArea': [gr_liv_area],
    'OverallQual': [overall_qual],
    'YearBuilt': [year_built],
    'TotalSF': [total_sf],
    'HouseAge': [house_age],
    'GarageCars': [garage_cars],
    'LotArea': [lot_area],
    'Neighborhood': [neighborhood],
    'MSZoning': [ms_zoning],
    'Exterior1st': [exterior_1st],
    'KitchenQual': [kitchen_qual]
})

# 3. Prediction Button
if st.button("Predict House Price 🚀"):
    prediction = model.predict(input_data)
    st.success(f"💰 The estimated price for this property is: **${prediction[0]:,.2f}**")