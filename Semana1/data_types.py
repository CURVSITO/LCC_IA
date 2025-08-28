import math
# # String data type
# # Asignacion literal
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

# #Casting a number to a string
# decada = 2010
# print(type(decada))
# print(decada)
# frase = "Yo soy de la decada de los " + str(decada) + "."
# print(frase)
# #Multiples lineas
# multilinea = '''
# Hola,
# Como estas?
#            Bien, y tu
# '''
# print(multilinea)

# #Escapar de caracteres especiales
# frase = "\"El respeto al derecho ajeno es la paz\"\nBenito Juarez\n1864"
# print(frase)

# # String Methods
# print(first)
# print(first.lower()) #Todo minuscula
# print(first.upper()) #Todo mayuscul
# print(first) #Se mantiene igual

# print(frase.title()) #mayusc a letra inicial de cada palabra
# print(frase.replace("paz", "pez")) #Reemplaza el texto solicitado por otro proporcionado

# print(len(frase))
# frase += "            "
# print(len(frase))
# print(len(frase.strip()))

#Construir un menu
title = "menu".upper()
print(title.center(30, "="))
print("Latte".ljust(16, ".") + "$70".rjust(4))
print("Cupcake".ljust(16, ".") + "$60".rjust(4))
print("Cookie".ljust(16, ".") + "$65".rjust(4))

#String index values
print(first[1]) #Index empieza a contar desde valor 0
print(first[0])
print(first[-1]) #Ultima letra
print(first[1:-1]) 
print(first[0:]) 

#Metodos que dan datos en booleanos
print(first.startswith("J"))
print(first.endswith("e"))

#Datos tipo booleano
mivalor = True
x = bool(False)
print(type(x))
print(isinstance(x , bool))
print(isinstance(mivalor , bool))

#Datos tipo numerico

#tipo integer y float
price = 99.99
best_price = int(80) - float(price*.1)
print(type(price))
print(best_price)
print(isinstance(best_price, float))

#complex type
valor_comp = 6+5j
print(type(valor_comp))
print(valor_comp)
print(valor_comp.real)
print(valor_comp.imag)

#Funcion preconstruidas para numeros
print(abs(best_price))
print(round(best_price))
print(round(best_price, 2))
print(" ")
print(math.pi)
print(math.sqrt(16))
print(math.ceil(best_price))
print(math.floor(best_price))