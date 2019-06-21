package com.uuu.sbt.demo

import org.apache.log4j.{Level, Logger}
import org.apache.spark.{SparkConf, SparkContext}

object HelloSbt5_reduce {
  def main(args: Array[String]): Unit = {
    Logger.getLogger("org").setLevel(Level.WARN)
    val config = new SparkConf().setAppName("SimpleSpark1").setMaster("local[*]")
    val sc = new SparkContext(config)
    val textFile = sc.textFile("data\\yarn.cmd")
    println(textFile.map(l => l.split("\\s+").size).collect().mkString("[", ",", "]"))
    println("max word:", textFile.map(l => l.split("\\s+").size).reduce((a, b) => if (a > b) a else b))
    println("connect successfully, prepare to do something...")
    sc.stop()
  }
}
