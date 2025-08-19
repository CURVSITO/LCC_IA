#assignment
nombre = 'Jorge '
print(nombre)
#addition or sustraction
print(2+2)
print("Jorge " + "Carlos")
print(nombre + "Carlos")
#multiplication
print(2*2)
#division
print(2 / 2)
#round division
print(24 // 5)
print(round(24 / 5))
#obtener residuo
print(24 % 5)
#potencia
print(2 ** 5)
#holds value
edad = 18
edad += 1
print(edad)
edad -= 1 #applies to any other operator
print (edad)
#es igual a| Responde en Booleano= True o False
print(nombre == edad)
print(edad == 18)
#no es igual a | Responde en Booleano
print(edad != 18)
print(edad != nombre)
#mayor que o mayor o igual que y menor que y menor o igual que | Responde en Booleano
print(10 > 5)
print(10 < 5)
print(10 >= 10)
print(10 <= 5)
#Operadores Booleanos
x = True
y = False
z = True
print(not x)
print(not y)
#"and" busca hasta llegar a un valor verdadero
print(x and y)
print(y and x)
#"or" busca hasta a llegar uno u otro valor que sea verdadero
print(y or x)
print(x or y)
#Operadores Condicionales
#Indica la condicion si
if edad >= 18:
    print('Puedes pasar tilin')
#Indica que si no se cumple realize tal
else:
    print('A tu casa bro')
# Ternary Operator
print('Puedes pasar tilin') if edad >= 18 else print('A tu casa bro')