import streamlit as st
import pandas as pd
import requests

# Base URL of the Flask backend inside the Docker network
BACKEND_URL = "http://backend:7860"

# Set the title of the Streamlit app
st.title("SuperKart Sales Prediction App")

# Section for sales prediction
st.subheader("Sales Prediction")

# Collect user input for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area", min_value=0.0, value=0.04)
Product_MRP = st.number_input("Product MRP", min_value=0.0, value=150.0)
Product_Type = st.selectbox("Product Type", [
    "Fruits and Vegetables", "Snack Foods", "Frozen Foods", "Dairy",
    "Household", "Baking Goods", "Canned", "Health and Hygiene",
    "Meat", "Soft Drinks", "Breads", "Hard Drinks", "Others",
    "Starchy Foods", "Breakfast", "Seafood"
])
Store_Size = st.selectbox("Store Size", ["Small", "Medium", "High"])
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
Store_Type = st.selectbox("Store Type", ["Supermarket Type1", "Supermarket Type2", "Food Mart", "Departmental Store"])
Product_Type_Category = st.selectbox("Product Type Category", ["Perishables", "Non Perishables"])

# Construct the data payload, matching the backend API's expected features
product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Product_Type": Product_Type, # Added Product_Type
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Type_Category": Product_Type_Category
}

# Make prediction when the "Predict" button is clicked
if st.button("Predict", type="primary"):
    # Sending the individual product data dictionary to the Flask API endpoint
    response = requests.post(f"{BACKEND_URL}/v1/predict", json=product_data)
    if response.status_code == 200:
        prediction = response.json()['Sales']
        st.success(f"Predicted Product Sales Total: {round(prediction, 2)}")
    else:
        st.error(f"Error: {response.status_code}. Unable to connect to the prediction API.")
