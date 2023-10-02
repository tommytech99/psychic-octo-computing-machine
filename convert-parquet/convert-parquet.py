from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("MyExample").getOrCreate()
df = spark.read.parquet("train-00000-of-00001-a09b74b3ef9c3b56.parquet")
df.write.csv("train-00000-of-00001-a09b74b3ef9c3b56.csv")