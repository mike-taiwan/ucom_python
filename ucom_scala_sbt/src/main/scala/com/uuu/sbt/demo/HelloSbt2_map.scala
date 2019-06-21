package com.uuu.sbt.demo

import org.apache.log4j.{Level, Logger}
import org.apache.spark.{SparkConf, SparkContext}

object HelloSbt2_map {
  def main(args: Array[String]): Unit = {
    Logger.getLogger("org").setLevel(Level.WARN)
    val config = new SparkConf().setAppName("SimpleSpark1").setMaster("local[*]")
    val sc = new SparkContext(config)
    val textFile = sc.textFile("data\\yarn.cmd")
    val mapResult1 = textFile.map(l => l.split("\\s+"))
    println(mapResult1.collect())
    mapResult1.foreach(l => println(l.mkString("^","|","$")))
    val mapResult2 = textFile.flatMap(l=>l.split("\\s+"))
    println(mapResult2.collect().mkString("^","|","$"))
    sc.stop()
  }
}

