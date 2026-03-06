from pyspark.sql import SparkSession

# create spark session
spark = SparkSession.builder \
    .appName("Ecommerce Data Processing") \
    .getOrCreate()

# read csv
df = spark.read.csv("data/orders_raw.csv", header=True, inferSchema=True)

# show data
df.show()

# transformation
total_sales = df.groupBy("category").sum("price")

# show results
total_sales.show()

# save result
total_sales.write.csv("data/category_sales", header=True)

spark.stop()