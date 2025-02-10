
import streamlit as st
import pandas as pd

def calculate_price(products, duration, hourly_rate, overhead_cost, target_margin):
    product_cost = sum(products.values())  # Sum up all product costs
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

# Allow multiple product selections
selected_products = st.multiselect("Select Products Used", list(product_data.keys()))
products_used = {}
for product in selected_products:
    amount_used = st.number_input(f"Amount of {product} Used (ml)", min_value=0.0, format="%.2f")
    products_used[product] = amount_used * product_data[product]

duration = st.number_input("Appointment Duration (minutes)", min_value=1, step=1)
stylist_name = st.selectbox("Select Stylist", ["Emily", "Sachi", "Rachel", "Gwen", "Brian", "Hailey", "Nikki", "Molly"])
target_margin = 0.20

# Stylist hourly rates
stylist_rates = {
    "Emily": 95,
    "Sachi": 140,
    "Rachel": 80,
    "Gwen": 70,
    "Brian": 80,
    "Hailey": 75,
    "Nikki": 78,
    "Molly": 70
}
hourly_rate = stylist_rates[stylist_name]

overhead_cost = 10  # Fixed overhead cost per service

if st.button("Calculate Price"):
    total_cost, recommended_price = calculate_price(products_used, duration, hourly_rate, overhead_cost, target_margin)
    
    st.write(f"### Total Cost: ${total_cost:.2f}")
    st.write(f"### Recommended Price: ${recommended_price:.2f}")
