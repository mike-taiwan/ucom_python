package com.uuu.sbt.demo

import org.apache.log4j.{Level, Logger}
import org.apache.spark.{SparkConf, SparkContext}

object HelloSbt1_spark_shell {
  def main(args: Array[String]): Unit = {
    Logger.getLogger("org").setLevel(Level.WARN)
    val config = new SparkConf().setAppName("SimpleSpark1").setMaster("local[*]")
    val sc = new SparkContext(config)
    println("connect successfully, prepare to do something...")
    val textFile = sc.textFile("data\\yarn.cmd");
    textFile.map(_.toUpperCase).take(5).foreach(println)
    sc.stop()
  }
}