package com.uuu.sbt.demo

import org.apache.log4j.{Level, Logger}
import org.apache.spark.{SparkConf, SparkContext}

object HelloSbt4_reduce {
  def main(args: Array[String]): Unit = {
    Logger.getLogger("org").setLevel(Level.WARN)
    val config = new SparkConf().setAppName("SimpleSpark1").setMaster("local[*]")
    val sc = new SparkContext(config)
    val rdd1 = sc.makeRDD(Array(("A", 1), ("B", 3), ("C", 5), ("D", 7), ("E", 9), ("F", 11)))
    println("add reduce (always get the same result):")
    println(rdd1.reduce((x, y) => {
      (x._1 + y._1, x._2 + y._2)
    }))
    println("sub reduce (may get different result):")
    println(rdd1.reduce((x, y) => {
      (x._1 + y._1, x._2 - y._2)
    }))

    println("connect successfully, prepare to do something...")
    sc.stop()
  }
}
