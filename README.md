# E-Commerce Data Engineering Pipeline

## Project Overview

This project demonstrates an end-to-end data engineering pipeline built using Python, Snowflake, Spark, and Streamlit.

The pipeline simulates an e-commerce system where order data is generated, stored in a cloud data warehouse, processed using Spark, and visualized through a dashboard.

---

## Architecture

![Architecture](architecture.png)

---

## Tech Stack

Python  
SQL  
Snowflake  
Apache Spark  
Streamlit  
GitHub

---

## Pipeline Steps

1. Data Generation

A Python script generates synthetic e-commerce order data.

2. Data Storage

Data is uploaded to Snowflake cloud data warehouse.

3. Data Processing

Spark is used to transform raw order data.

4. Data Analysis

SQL queries calculate business metrics like revenue and product demand.

5. Visualization

A Streamlit dashboard displays sales insights.

---

## Dashboard Features

Total revenue KPI  
Sales by city  
Product demand  
Interactive filters

---

## How to Run the Project

Install dependencies

pip install pandas pyspark snowflake-connector-python streamlit python-dotenv

Run dashboard

streamlit run dashboard/dashboard.py

---

## Author

Gurashish Singh