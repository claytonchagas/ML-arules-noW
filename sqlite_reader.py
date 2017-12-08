import sqlite3

import numpy as np

conn = sqlite3.connect('/home/clayton/Documentos/input/exec_mineracao/.noworkflow/db.sqlite')
cursor = conn.cursor()

# cursor.execute("""SELECT * FROM dependency""")
# cursor.execute("""select trial.id as trial_id, trial.script as nome_script, module.id as module_id, module.name as
# module_name, module.version as module_version, module.path as module_path from trial inner join dependency on
# dependency.trial_id = trial.id inner join module on dependency.module_id = module.id""")

cursor.execute("""select trial.id as trial_id, module.name as module_name from trial inner join dependency on 
dependency.trial_id = trial.id inner join module on dependency.module_id = module.id""")

result = cursor.fetchall();

#for linha in result:
#    print(linha)

final_result = [list(i) for i in result]

print(final_result)

print(len(final_result))

for final_result3 in final_result:
    print(final_result3[1:2]) # só os nomes dos módulos
    #print(final_result3[:1]) # só os ids dos trials
    # final_result2 = np.matrix(final_result[3])

# print(final_result2)

# row = list(cursor)[0][0]

# print(row)

conn.close()
