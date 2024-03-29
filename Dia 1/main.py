## ------------------------------------------
## ------ Ejercicio 1 ------
## ------------------------------------------

#Impresion en consola 
print("Hola Mundo")

# ------ Datos primitivos ------

#1. String
texto = "Campus"
print (texto)
print(type(texto))
#2. Int
Numero = 10
print(Numero)
print (type(Numero))
#3. Float
Decimal = 3.5
print(Decimal)
print (type(Decimal))
#4. Double
DecimalDouble = 3.141632132132133213
print (DecimalDouble)
print (type(DecimalDouble))
#5. Boolean
booleano = True
print (booleano)
print (type(booleano))

# ------ Entradas parte del usuario ------

entradaUsuario = input("Ingresa tu nombre ")
print ("Tu nombre es ", entradaUsuario)

# ------ Entradas parte del usuario con definicion de tipo de dato primitivo ------

entradaUsuarioNum = input("Ingresa tu edad ")
numeroFinal = int(entradaUsuarioNum)
print ("Tu edad es ", numeroFinal)

# ------ Ciclos ------
# Ciclo for
for i in range (5,10,2) : # for i in range (desde, hasta, pasos) :
    print (i)

# Ciclo while
booleanito = True
while booleanito == True :
    print ("sigo vivo")
    booleanito = False

# ------ Condicionales ------

texto1 = "campus"
if texto1 == "campus" :
    print ("Soy camper")
else :
    print ("No soy camper")


# ------ Funciones ------
# 1. Función con parámetros y con retorno
def suma(a, b):
    resultado = a + b
    return resultado

# Uso de la función
valor1 = 5
valor2 = 3
resultado_suma = suma(valor1, valor2)

print(f"La suma de {valor1} y {valor2} es: {resultado_suma}")

# 2. Función sin parámetros y con retorno
def obtener_numero():
    return 42

# Uso de la función
resultado = obtener_numero()

print(f"El número obtenido es: {resultado}")

# 3. Función con parámetros y sin retorno
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Uso de la función
nombre_usuario = "Daniel"
saludar(nombre_usuario)


# 4. Función sin parámetros y sin retorno
def saludar():
    print("¡Hola, mundo!")

# Uso de la función
saludar()


# ------ Arrays ------

nombres =["Juan", "Pedro", "Roberto", "Luciana", "Mariana"]
print (nombres[0])#0 es la primera posicion del array
print (nombres[1])
print (nombres[2])
print (nombres[3])
print (nombres[4])

## Desarrollado por DANIEL ALEJANDRO LATORRE RUIZ - CC 1005257201


