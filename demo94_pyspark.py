from pyspark import SparkContext

sc = SparkContext("local", "my spark app")
lines = sc.textFile("ucom_python\\data\\yarn.cmd")
lines.cache()
print("get total with collect:", lines.collect())
print("get total line count:", lines.count())
print("get first line", lines.first())
print("get first several line", lines.take(8))
print("filter line with 'k' ", lines.filter(lambda s: 'k' in s).count())
print("sample 5 lines:", lines.sample(False, 5))
print('first 9 records:', lines.takeOrdered(9))
lineLengths = lines.map(lambda s: len(s))
print("per line length:", lineLengths.collect())
totalLength = lineLengths.reduce(lambda a, b: a + b)
print("total length=", totalLength)