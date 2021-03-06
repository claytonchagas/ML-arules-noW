from pyspark.ml.fpm import FPGrowth
from pyspark.sql import SparkSession

from timeit import default_timer as timer

if __name__ == "__main__":
    start = timer()

    spark = SparkSession\
        .builder\
        .appName("FPGrowthExample")\
        .getOrCreate()

    df = spark.createDataFrame([
        (0, [1, 2, 5]),
        (1, [1, 2, 3, 5]),
        (2, [1, 2])
    ], ["id", "items"])

    fpGrowth = FPGrowth(itemsCol="items", minSupport=0.5, minConfidence=0.6)
    model = fpGrowth.fit(df)

    # Display frequent itemsets.
    model.freqItemsets.show()

    # Display generated association rules.
    model.associationRules.show()

    # transform examines the input items against all the association rules and summarize the
    # consequents as prediction
    model.transform(df).show()
    # $example off$

    spark.stop()

    end = timer()
    print(end - start)