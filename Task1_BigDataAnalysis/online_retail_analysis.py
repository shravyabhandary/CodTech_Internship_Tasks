from pyspark.sql import SparkSession

# Step 1: Create Spark session
spark = SparkSession.builder \
    .appName("Online Retail Analysis") \
    .getOrCreate()

# Step 2: Load CSV file
df = spark.read.csv("C:/Users/hp/Desktop/OnlineRetail.csv", header=True, inferSchema=True)

# Step 3: Show first 5 rows
print("Showing first 5 rows:")
df.show(5)

# Step 4: Count total rows
print("Total number of records:", df.count())

# Step 5: Summary statistics
print("Dataset summary:")
df.describe().show()

# Step 6: Country-wise transaction count
print("Top 10 countries by transaction count:")
df.groupBy("Country").count().orderBy("count", ascending=False).show(10)

# Step 7: Most sold products
print("Top 10 most sold products:")
df.groupBy("Description").sum("Quantity").orderBy("sum(Quantity)", ascending=False).show(10)

# Step 8: End Spark session
spark.stop()
