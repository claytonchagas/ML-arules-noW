import sqlite3
import pandas as pd

from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori

from timeit import default_timer as timer

start = timer()

conn = sqlite3.connect('/home/clayton/Documentos/input/exec_mineracao/.noworkflow/db2.sqlite')
cursor = conn.cursor()

cursor.execute("""select trial.id as trial_id, module.name as module_name from trial inner join dependency on 
dependency.trial_id = trial.id inner join module on dependency.module_id = module.id""")

result = cursor.fetchall()

conn.close()

dataset = []

print(result)

for count in result:
    counter = count[0]

print(counter)

for m in range(counter):
    dataset.append([])
    for linha in result:
        if linha[0] == m+1:
            dataset[m].append(linha[1])

print(dataset)
for m in range(counter):
    print(len(dataset[m]))
    print(dataset[m])

oht = OnehotTransactions()
oht_ary = oht.fit(dataset).transform(dataset)
df = pd.DataFrame(oht_ary, columns=oht.columns_)
print(df)
df.to_csv('example.csv')
apriori(df, min_support=0.9)

end = timer()
print(end - start, "seg.")