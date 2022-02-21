# Funcion input(), para leer datos de entrada
# Variable = input("Ingrese un número: ")
apodo = input("Ingrese su apodo: ")
print(f"Hola {apodo}")
print('Fin del programa')

# Ejemplo 2
num1 = input("Ingrese un número: ")
num2 = input("Ingrese otro número: ")
result = int(num1) + int(num2)
print("El resultado es: " + str(result))

# Ejemplo 3
# Calificando mi dia del 1 al 5
dia = input("Ingrese un día de la semana: ")
calificar = input("Ingrese una calificación entre 1 y 5: ")
resultadoDiario = dia + ": " + calificar
print("El resultado del día es: " + resultadoDiario)

#Ejemplo 4
#  Se solicita incluir la siguiente información acerca de un libro: titulo, autor
titulo = input("Ingrese el título del libro: ")
autor = input("Ingrese el autor del libro: ")
print(f"El libro {titulo} fue escrito por {autor}") 