import streamlit as st
import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.title("E-Commerce Sales Dashboard")

# Snowflake connection
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

# Query data
cur = conn.cursor()
cur.execute("SELECT * FROM ORDERS")

df = pd.DataFrame(cur.fetchall(), columns=[x[0] for x in cur.description])

st.subheader("Raw Orders Data")
st.dataframe(df)

# Revenue column
df["REVENUE"] = df["PRICE"] * df["QUANTITY"]

# Sidebar filter
cities = st.sidebar.multiselect(
    "Select City",
    options=df["CITY"].unique(),
    default=df["CITY"].unique()
)

filtered_df = df[df["CITY"].isin(cities)]

# Total revenue
total_revenue = filtered_df["REVENUE"].sum()

st.metric("Total Revenue", total_revenue)

# Sales by city
city_sales = filtered_df.groupby("CITY")["REVENUE"].sum()

st.subheader("Sales by City")
st.bar_chart(city_sales)

# Product orders
product_orders = filtered_df.groupby("PRODUCT")["QUANTITY"].sum()

st.subheader("Product Orders")
st.bar_chart(product_orders)


daily_sales = filtered_df.groupby("ORDER_DATE")["REVENUE"].sum()

st.subheader("Daily Revenue Trend")

st.line_chart(daily_sales)

total_orders = len(filtered_df)

st.metric("Total Orders", total_orders)