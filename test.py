def advance(word1,word2,i,j):
    if word1[i] == word2[j]:
        return word1,word2,i+1,j+1
def delete(word1,word2,i,j):
    word1.pop(i)
    return word1,word2,i,j
def replace(word1,word2,i,j):
    word1[i] = word2[j]
    return word1,word2,i+1,j+1
def insert(word1,word2,i,j):
    try:
        word1.insert(i, word2[j])
    except IndexError:
        word1.append(word2[j])
    return word1,word2,i+1,j+1
def kill(word1,word2,i,j):
    word1 = word1[:i]
    return word1,word2,i,j
#
advance_Cost = 1
delete_Cost = 1
replace_Cost = 2
insert_Cost = 1
kill_Cost = 4
#
def calcular_mejor_coste(word1,word2,i,j,advance_Cost,delete_Cost,replace_Cost,insert_Cost,kill_Cost,operaciones,costos):
    if i == len(word1) and j == len(word2):
        return costos,operaciones
    if i == len(word1):
        word1,word2,i,j = insert(word1,word2,i,j)
        operaciones.append('insert '+ str(word1))
        costos.append(insert_Cost)
        return calcular_mejor_coste(word1,word2,i,j,advance_Cost,delete_Cost,replace_Cost,insert_Cost,kill_Cost,operaciones,costos)
    if j == len(word2):
        print("palabras que faltan por borrar" + str(word1[i:]))
        to_delete = len(word1[i:])
        if to_delete*delete_Cost<kill_Cost:        
            word1,word2,i,j = delete(word1,word2,i,j)
            operaciones.append('delete '+ str(word1))
            costos.append(delete_Cost)
            return calcular_mejor_coste(word1,word2,i,j,advance_Cost,delete_Cost,replace_Cost,insert_Cost,kill_Cost,operaciones,costos)
        else:
            word1,word2,i,j = kill(word1,word2,i,j)
            operaciones.append('kill '+ str(word1))
            costos.append(kill_Cost)
            return calcular_mejor_coste(word1,word2,i,j,advance_Cost,delete_Cost,replace_Cost,insert_Cost,kill_Cost,operaciones,costos)
    if word1[i] == word2[j]:
        word1,word2,i,j = advance(word1,word2,i,j)
        operaciones.append('advance '+ str(word1))
        costos.append(advance_Cost)
        return calcular_mejor_coste(word1,word2,i,j,advance_Cost,delete_Cost,replace_Cost,insert_Cost,kill_Cost,operaciones,costos)
    
operaciones = []
operaciones2 = []
word1 = ['a','b']
word2 = ['a','b','c','s']
calcular_mejor_coste(word1[:],word2[:],0,0,advance_Cost,delete_Cost,replace_Cost,insert_Cost,kill_Cost,operaciones,[])
calcular_mejor_coste(word2,word1,0,0,advance_Cost,delete_Cost,replace_Cost,insert_Cost,kill_Cost,operaciones2,[])
for op in operaciones:
    print(op)
print('----------------------------------')
for op in operaciones2:
    print(op)

