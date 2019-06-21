package com.uuu.sbt.demo

import org.apache.log4j.{Level, Logger}
import org.apache.spark.{SparkConf, SparkContext}

object HelloSbt3_reduce {
  def main(args: Array[String]): Unit = {
    Logger.getLogger("org").setLevel(Level.WARN)
    val config = new SparkConf().setAppName("SimpleSpark1").setMaster("local[*]")
    val sc = new SparkContext(config)
    var rdd1 = sc.makeRDD(1 to 10)
    val result = rdd1.reduce(_ + _)
    var rdd2 = sc.makeRDD(1 to 20)
    val result2 = rdd2.reduce((x, y) => {
      x + y
    })
    println("answer1=%d, answer2=%d".format(result, result2))
    println("connect successfully, prepare to do something...")
    sc.stop()
  }
}