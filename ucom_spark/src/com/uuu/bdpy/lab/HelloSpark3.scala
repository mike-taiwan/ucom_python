package com.uuu.bdpy.lab

import org.apache.log4j.{Level, Logger}
import org.apache.spark.ml.feature.{OneHotEncoder, StringIndexer}
import org.apache.spark.sql.SparkSession
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.SparkSession

object HelloSpark3 {
  def main(args: Array[String]): Unit = {
    Logger.getLogger("org").setLevel(Level.WARN)
    val spark = SparkSession.builder.master("local[*]").appName("demo2").getOrCreate
    println("connect successfully, prepare to do something...")
    val df1 = spark.createDataFrame(Seq(
      (0, "apple"),
      (1, "banana"),
      (2, "citron"),
      (3, "apple"),
      (4, "apple"),
      (5, "citron")
    )).toDF("id", "category")

    val indexer = new StringIndexer().setInputCol("category").setOutputCol("categoryIndex").fit(df1)
    val indexed = indexer.transform(df1)
    val encoder = new OneHotEncoder()
      .setInputCol("categoryIndex")
      .setOutputCol("categoryVec")
      .setDropLast(false)
    val encoded = encoder.transform(indexed)
    println("print the result")
    encoded.show()
    spark.sparkContext.stop()
  }
}