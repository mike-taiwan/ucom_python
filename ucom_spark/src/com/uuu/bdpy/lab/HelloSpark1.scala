package com.uuu.bdpy.lab

import org.apache.log4j.{Level, Logger}
import org.apache.spark.{SparkConf, SparkContext}

object HelloSpark1 {
  def main(args: Array[String]): Unit = {
    Logger.getLogger("org").setLevel(Level.WARN)
    val config = new SparkConf().setAppName("SimpleSpark1").setMaster("local[*]")
    val sc = new SparkContext(config)
    println("connect successfully, prepare to do something...")
    val textFile1 = sc.textFile("data\\yarn.cmd")
    println("yarn.cmd has:%d lines".format(textFile1.count()))
    val numAs = textFile1.filter(line=>line.contains("a")).count()
    val numBs = textFile1.filter(line=>line.contains("b")).count()
    println(s"Lines with a: $numAs, with b: $numBs")
    sc.stop()
  }
}
