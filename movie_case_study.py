# Databricks notebook source
display(dbutils.fs.ls("/Volumes/case_study_databricks/movie_case_study/movie_volume_managed/"))

# COMMAND ----------

df = spark.read.option("header", "true").option("inferSchema", "true").csv(
    "/Volumes/case_study_databricks/movie_case_study/movie_volume_managed/movies.csv"
)

# COMMAND ----------

display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

print("Number of rows:", df.count())
print("Number of columns:", len(df.columns))

# COMMAND ----------

display(df.limit(10))

# COMMAND ----------

from pyspark.sql.functions import explode, split, col

genre_df = df.withColumn(
    "genre",
    explode(split(col("genres"), "\\|"))
)

display(genre_df)

# COMMAND ----------

genre_count = genre_df.groupBy("genre").count().orderBy(
    col("count").desc()
)

display(genre_count)