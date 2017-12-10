import sqlite3
import pandas as pd

from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

from timeit import default_timer as timer

start = timer()

# conn = sqlite3.connect('/home/clayton/Documentos/input/exec_mineracao/.noworkflow/db.sqlite')
conn = sqlite3.connect('/home/clayton/Documentos/input/scriptsall/.noworkflow/db.sqlite')
cursor = conn.cursor()

cursor.execute("""select trial.id as trial_id, module.name as module_name from trial inner join dependency on 
dependency.trial_id = trial.id inner join module on dependency.module_id = module.id""")

result = cursor.fetchall()

cursor.execute("""select count(trial.id) from trial""")

counter = cursor.fetchall()

print("Tupla: ", counter)

counterIntList = []

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
    dataset.append([])

for linha in result:
    dataset[linha[0] - 1].append(linha[1])

# for m in range(counterInt):
#     dataset.append([])
#     for linha in result:
#         if linha[0] == m+1:
#             dataset[m].append(linha[1])

# for i in range(10,100):
#     dataset.append(['a','b','c'])
#     counterInt+=1

print(dataset)
for m in range(counterInt):
    # print(len(dataset[m]))
    print(dataset[m])

oht = OnehotTransactions()
oht_ary = oht.fit(dataset).transform(dataset)
df = pd.DataFrame(oht_ary, columns=oht.columns_)
print(df)
df.to_csv('example.csv')
# print(apriori(df, min_support=0.5))
print(apriori(df, min_support=0.9, use_colnames=True))
frequent_itemsets = apriori(df, min_support=0.9, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
print(frequent_itemsets)
print(association_rules(frequent_itemsets, metric="confidence", min_threshold=0.9))

end = timer()
print(end - start, "seg.")
