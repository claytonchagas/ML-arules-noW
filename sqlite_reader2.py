import sqlite3

conn = sqlite3.connect('/home/clayton/Documentos/input/exec_mineracao/.noworkflow/db.sqlite')
cursor = conn.cursor()

# cursor.execute("""SELECT * FROM dependency""")
# cursor.execute("""select trial.id as trial_id, trial.script as nome_script, module.id as module_id, module.name as
# module_name, module.version as module_version, module.path as module_path from trial inner join dependency on
# dependency.trial_id = trial.id inner join module on dependency.module_id = module.id""")

cursor.execute("""select trial.id as trial_id, module.name as module_name from trial inner join dependency on 
dependency.trial_id = trial.id inner join module on dependency.module_id = module.id""")

result = cursor.fetchall()

dataset = []

# ds.append([])

# ds = result

print(result)

for count in result:
    # print(count[0])
    counter = count[0]

print(counter)

# for m in range(counter):
#     print(m)

for m in range(counter):
    dataset.append([])
    for linha in result:
        if linha[0] == m+1:
            dataset[m].append(linha[1])

    # print(linha[1])
    # print(linha[1], linha[0])
    # ds.append(linha[1])

print(dataset)
for m in range(counter):
    print(len(dataset[m]))
    print(dataset[m])
conn.close()
