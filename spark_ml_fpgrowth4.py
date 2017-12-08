data = [["a", "b", "c"], ["a", "b", "d", "e"], ["a", "c", "e"], ["a", "c", "f"]]

from pyspark.context import SparkContext

from pyspark.ml.fpm import FPGrowth

rdd = SparkContext.parallelize(data, 2)

model = FPGrowth.train(rdd, 0.6, 2)