from pyspark.ml.feature import OneHotEncoder, StringIndexer
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("spark").getOrCreate()

df1 = spark.createDataFrame([
    (0, "7-11"),
    (1, "7-11"),
    (2, 'Fami'),
    (3, "OK"),
    (4, 'Fami'),
    (5, 'Hi-Life'),
    (6, '7-11')
], ["id", "category"])

stringIndexer = StringIndexer(inputCol="category", outputCol="categoryIndex")
model = stringIndexer.fit(df1)
indexed = model.transform(df1)
encoder = OneHotEncoder(inputCol="categoryIndex", outputCol="result", dropLast=False)
encoded = encoder.transform(indexed)
encoded.show()

spark.sparkContext.stop()