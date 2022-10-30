######################Inicio Algoritmo Merge_Sort ##########################################
from __future__ import division
from turtle import distance

def merge_sort(array):
    if len(array)<2: #constante
        return
    mid = len(array)//2 #constante
    left_array = array[:mid] #constante
    right_array = array[mid:] #constante
    print(left_array, right_array) #constante
    merge_sort(left_array) #lineal
    merge_sort(right_array) #lineal
    left_index = 0 #constante
    right_index = 0 #constante
    array_index = 0 #constante

    while left_index < len(left_array) and right_index < len(right_array): #cuadratico

        if left_array[left_index] < right_array[right_index]: #constante
            array[array_index] = left_array[left_index] #constante
            left_index += 1
        else:
            array[array_index] = right_array[right_index] #constante
            right_index += 1 #constante
        array_index += 1 #constante

    if left_index < len(left_array): #constante
        del array[array_index:] #constante
        array += left_array[left_index:] #constante
    elif right_index < len(right_array): #constante
        del array[array_index:] #constante
        array += right_array[right_index:] #constante

    return array #constante

array = [6, 20, 5, 8, 9, 21]
print(merge_sort(array))

#6/2=3 se divide en dos para sacar la mitad
#[6, 20, 5]  [8, 9, 21] se forman 2 grupos para realizar el merge
#[6] [20, 5] se encuentra el primer orden del grupo
#[20] [5] se encuentra el segundo grupo
#[8] [9,21] finaliza con el tercer grupo
#[5, 6, 8, 9, 20, 21] realiza la union de los tres grupos encontrados
######################Fin Algoritmo Merge_Sort ##########################################
######################inicio Algoritmo Shell_Sort #############################################
def shell_sort(array):
    num = len(array)#constante
    division = 2#constante
    distance = num//division#contante
    
    while distance > 0:#cuadratica
      index_to_delete = []#constante
      for i in range(distance, num):#cuadratica
        temp = array[i]#constante
        j = i#constante
        while j >= distance and array[j-distance] >= temp:#cuadratica
            if array[j-distance] == temp:#constante
                index_to_delete.append(j)#constante
            array[j] = array[j-distance]#constante
            j -= distance#constante
        array[j] = temp#constante
      index_to_delete=list(set(index_to_delete))#constante
      index_to_delete.sort()#lineal
      
      if index_to_delete:#constante
          for i in index_to_delete[-1::-1]:#cuadratica
              del array[i]#constante
      division *= 2#constante
      num = len(array)#constante
      distance = num//division#constante
if __name__ == '__main__':#constante
    elements = [6, 20, 5, 8, 9, 21]#constante
    print(f'Given unsorted list elements: {elements}')#constante
    shell_sort(elements)#lineal
    print(f'Show list elements after of sorting : {elements}')#constante

#6/2 = 3
#Inicio
#6 < 20 si [6, 20, 5, 8, 9, 21]
#20 < 5 no [6, 20, 5, 8, 9, 21]
#6 < 5 no [6, 5, 20, 8, 9, 21]
#5 < 6 si [5, 6, 20, 8, 9, 21]
#Segunda revisión
#3/2 = 1.5 = 1
#5 < 6 si [5, 6, 20, 8, 9, 21]
#6 < 20 si [5, 6, 20, 8, 9, 21]
#20 < 8 no [5, 6, 20, 8, 9, 21]
#20 < 9 no [5, 6, 8, 9, 20, 21]
#20 < 21 si [5, 6, 8, 9, 20, 21]
#[5, 6, 8, 9, 20, 21]