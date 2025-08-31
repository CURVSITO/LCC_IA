datos = ['Jorge', 18, True] #En una lista puedo tener datos de diversos tipos
datos2 = ['Pedrito']
listavacia = []
print("Jorge" in datos)
print(datos[0]) #De lista datos, valor posicion(Index) 0 que es 'Jorge'
print(datos[-1]) #Acepta valores negativos para los ultimos valores
print(datos.index(True))
print(datos[0:1]) #No abarca el valor 1
print(datos[0:])
print(len(datos)) #Cuantos valores hay en la lista datos
datos.append('Agustino') #Agrega valor a la lista datos
print(datos)
datos += ['Juan']
print(datos)
datos.extend(['Roberto', 'Faustiano']) #Agrega los valores de esta lista a datos
print(datos)

# datos.extend(datos2)
# print(datos)
datos.insert(2, 'Carlos')
print(datos)
datos[0:0] = ['Benicio', 'Alex'] #Agrega valor a la posicion especificada de la lista datos, puede reemplazarlos si es indicado
print(datos)
datos.remove('Agustino')
print(datos)
print(datos.pop()) #Quita el ultimo valor de la lista y lo imprime
print(datos) #La lista ya fue modificado por el pop

del datos [0]
print(datos)

#del datos #borra la lista completamente
print(datos)
# datos.clear()
print(datos)
# datos.sort() #No acomoda datos de diferentes types
datos2[0:0] = ['David', 'gustavo']
datos2.sort()
print(datos2)
datos2.sort(key=str.lower) 
print(datos2)

nums = [35, 7, 4, 89]
nums.reverse()
print(nums)
# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

#hacer una copia
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)
print(type(nums))

#Tuples son listas que no se pueden alterar
tupol= tuple(('Ariana', 'Taylor', 'Sabrina')) 
print(tupol)
print(type(tupol))
tupol2 = (2,5,6,7) #definidos por "()"
print(tupol2)

newlist = list(tupol)
newlist.append('Rihanna')
newtupol = tuple(newlist)
print(newtupol)

#Unpack si o si se asigna un valor a todo el tuplet
(uno, *dos, tres) = tupol2 #asigna un nombre a cada posicion y el *indica que los numeros que falten para completar estaran ahi
print(uno)
print(dos)
print(tres)
print(tupol.count('Taylor'))