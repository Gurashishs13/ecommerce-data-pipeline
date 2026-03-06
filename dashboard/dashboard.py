import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/orders_raw.csv")

# Page title
st.title("Ecommerce Data Engineering Dashboard")

# Metrics
total_orders = len(df)
total_revenue = (df["price"] * df["quantity"]).sum()

st.metric("Total Orders", total_orders)
st.metric("Total Revenue", total_revenue)

# Revenue by city
city_sales = df.groupby("city")["price"].sum().reset_index()

fig_city = px.bar(city_sales, x="city", y="price", title="Revenue by City")

st.plotly_chart(fig_city)

# Top products
product_sales = df.groupby("product")["price"].sum().reset_index()

fig_product = px.bar(product_sales, x="product", y="price", title="Top Products")

st.plotly_chart(fig_product)

# Orders over time
orders_time = df.groupby("order_date").size().reset_index(name="orders")

fig_time = px.line(orders_time, x="order_date", y="orders", title="Orders Over Time")

st.plotly_chart(fig_time)