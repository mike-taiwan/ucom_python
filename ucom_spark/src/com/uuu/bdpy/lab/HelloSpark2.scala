package com.uuu.bdpy.lab

import org.apache.log4j.{Level, Logger}
import org.apache.spark.sql.SparkSession
import org.apache.spark.{SparkConf, SparkContext}

object HelloSpark2 {
  def main(args: Array[String]): Unit = {
    Logger.getLogger("org").setLevel(Level.WARN)
    val spark = SparkSession.builder().master("local[*]").appName("demo2").getOrCreate();
    val textFile = spark.sparkContext.textFile("data\\yarn.cmd")
    println(textFile.take(2))
    println("print in a pretty way")
    println(textFile.take(2).mkString("Array(","m",")"))
    println("print in alternative way")
    textFile.take(3).foreach(println)
    println("print in alternative way2")
    textFile.collect().foreach(line=>println("[%d]%s".format(line.length,line)))
    println("connect successfully, prepare to do something...")
    spark.sparkContext.stop()
  }
}