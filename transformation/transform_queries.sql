-- revenue by product

SELECT
product,
SUM(total_price) as total_sales
FROM orders_clean
GROUP BY product
ORDER BY total_sales DESC;


-- revenue by city

SELECT
city,
SUM(total_price) as revenue
FROM orders_clean
GROUP BY city;


-- top customers

SELECT
customer_id,
SUM(total_price) as spending
FROM orders_clean
GROUP BY customer_id
ORDER BY spending DESC
LIMIT 10;