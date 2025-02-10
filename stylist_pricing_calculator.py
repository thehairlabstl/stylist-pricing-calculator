import streamlit as st
import pandas as pd

def calculate_price(color_used, unit_cost, duration, hourly_rate, overhead_cost, target_margin):
    product_cost = color_used * unit_cost
    labor_cost = (duration / 60) * hourly_rate
    total_cost = product_cost + labor_cost + overhead_cost
    recommended_price = total_cost / (1 - target_margin)
    return total_cost, recommended_price

# Load product data
product_data = {
    "Oligo Lightener": 3.50,
    "Oligo Developer 20 Vol": 2.00,
    "Oligo Toner": 4.00,
    "Redken Shades EQ": 4.50,
    "Wella Koleston": 3.75
}

st.title("Stylist Pricing Calculator")

# Inputs
selected_product = st.selectbox("Select Product", list(product_data.keys()))
unit_cost = product_data[selected_product]
color_used = st.number_input("Amount of Color Used (oz/ml)", min_value=0.0, format="%.2f")
duration = st.number_input("Appointment Duration (minutes)", min_value=1, step=1)
stylist_level = st.selectbox("Stylist Level", ["Junior", "Mid-Level", "Senior"])
target_margin = st.slider("Target Profit Margin (%)", 0, 50, 25) / 100

# Stylist hourly rates
stylist_rates = {"Junior": 25, "Mid-Level": 35, "Senior": 50}
hourly_rate = stylist_rates[stylist_level]

overhead_cost = 10  # Fixed overhead cost per service

if st.button("Calculate Price"):
    total_cost, recommended_price = calculate_price(color_used, unit_cost, duration, hourly_rate, overhead_cost, target_margin)
    
    st.write(f"### Total Cost: ${total_cost:.2f}")
    st.write(f"### Recommended Price: ${recommended_price:.2f}")
