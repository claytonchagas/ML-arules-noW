import sqlite3
# import pandas as pd

from pyspark.ml.fpm import FPGrowth
from pyspark.sql import SparkSession

# from mlxtend.preprocessing import OnehotTransactions
# from mlxtend.frequent_patterns import apriori

from timeit import default_timer as timer

if __name__ == "__main__":

    start = timer()

    spark = SparkSession \
        .builder \
        .appName("FPGrowthExample") \
        .getOrCreate()

    conn = sqlite3.connect('/home/clayton/Documentos/input/exec_mineracao/.noworkflow/db.sqlite')
    cursor = conn.cursor()

    cursor.execute("""select trial.id as trial_id, module.name as module_name from trial inner join dependency on 
    dependency.trial_id = trial.id inner join module on dependency.module_id = module.id""")

    result = cursor.fetchall()

    cursor.execute("""select count(trial.id) from trial""")

    counter = cursor.fetchall()

    print("Tupla: ", counter)

    counterIntList = []

    # counterInt = [int(c[0]) for c in counter]

    for n in counter:
        counterIntList.append(n[0])
        print("Tupla2List: ", counterIntList)
        counterInt = counterIntList[-1]
        print("List2int: ", counterInt)

    conn.close()

    dataset = []

    print(result)

    # for count in result:
    #     counter = count[0]
    #
    # print(counter)

    for i in range(counterInt):
        dataset.append((i,[]))

    for linha in result:
        dataset[linha[0]-1][1].append(linha[1])

    # for m in range(counter):
    #     dataset.append([])
    #     for linha in result:
    #         if linha[0] == m+1:
    #             dataset[m].append(linha[1])

    for i in range(10,100):
        dataset.append((i, ['a','b','c']))
        counterInt+=1

    print(dataset)
    for m in range(counterInt):
        print(len(dataset[m]))
        print(dataset[m])

    df = spark.createDataFrame(dataset, ["id", "items"])

    # df = spark.createDataFrame([
    #     (0, dataset[0]),
    #     (1, dataset[1]),
    #     (2, dataset[2]),
    #     (3, dataset[3]),
    #     (4, dataset[4]),
    #     (5, dataset[5]),
    #     (6, dataset[6]),
    #     (7, dataset[7]),
    #     (8, dataset[8]),
    #     (9, dataset[9]),
    # ], ["id", "items"])

    # df = spark.read.csv('example.csv')

    # oht = OnehotTransactions()
    # oht_ary = oht.fit(dataset).transform(dataset)
    # df = pd.DataFrame(oht_ary, columns=oht.columns_)
    # print(df)
    # df.to_csv('example.csv')

    fpGrowth = FPGrowth(itemsCol="items", minSupport=0.5, minConfidence=0.5)

    model = fpGrowth.fit(df)
    model.freqItemsets.show()
    model.associationRules.show()
    model.transform(df).show()

    # apriori(df, min_support=0.9)

    spark.stop()

    end = timer()
    print(end - start, "seg.")