# String data type
# Asignacion literal
first = "Jorge"
last = "Cardenas"

# print(type(first))
# print(type(first == str))
# print(type(first)== str)
# print(isinstance(first, str)) #Comprueba si pertenece a str 

#Funcion constructora
# pizza = str("Pesto")
# print(type(pizza))
# print(type(pizza == str))
# print(type(pizza)== str)
# print(isinstance(pizza, str))

#Concatenation
# fullname = first + " " + last
# print(fullname)
# fullname += " " + "Camara"
# print(fullname)

#Casting a number to a string
decada = 2010
print(type(decada))
print(decada)
frase = "Yo soy de la decada de los " + str(decada) + "."
print(frase)
#Multiples lineas
multilinea = '''
Hola,
Como estas?
           Bien, y tu
'''
print(multilinea)

#Escapar de caracteres especiales
frase = "\"El respeto al derecho ajeno es la paz\"\nBenito Juarez\n1864"
print(frase)

# String Methods
print(first)
print(first.lower()) #Todo minuscula
print(first.upper()) #Todo mayuscul
print(first) #Se mantiene igual

print(frase.title()) #mayusc a letra inicial de cada palabra
print(frase.replace("paz", "pez")) #Reemplaza el texto solicitado por otro proporcionado

print(len(frase))
frase += "            "
print(len(frase))
print(len(frase.strip()))
