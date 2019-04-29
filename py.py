agenda_telefonica = dict()
from time import sleep

print(" Bienvenido a la agenda telefonica")

def imprimir_operacion(nombre_operacion): 
    print()
    print(nombre_operacion)
    print() 

def agregar_contacto():
    print()
    nombre = input("Nombre del contacto para añadir: ")
    numero = input("Numero del contacto para añadir: ")
    agenda_telefonica[nombre] = numero
    nombre_operacion = ("Contacto agregado")
    imprimir_operacion(nombre_operacion)
    

def remover_contacto():
    print()
    nombre = input("Nombre del contacto que quiere borrar: ")
    nombre_operacion = None
    
    
    try:
        del agenda_telefonica[nombre]
    except KeyError:
        imprimir_operacion("Ese contacto no existe")
    else:
        imprimir_operacion("Contacto borrado")

def actualizar_contacto():
    print()
    print("Actualizar contacto")
    print()
    nombre = input("Nombre del contacto que quiere actualizar: ")
    numero = input("Nuevo numero del contacto: ")
    agenda_telefonica[nombre] = numero
    print()
    print("Numero actualizado ")
    print()

def ver_contacto():
    print()
    print(" Ver contacto")
    print()
    nombre = input("Nombre del contacto: ")
    print()
    nombre_operacion = None
    try:
        nombre_operacion = nombre + " tiene asociado el numero " + agenda_telefonica[nombre]
        imprimir_operacion(nombre_operacion)
    except KeyError:
        nombre_operacion = ("Ese nombre no existe")
        
        
def ver_todos_contacto():
    print()
    print("Lista de contactos")
    print()
    nombre_operacion = None
    
    if len(agenda_telefonica) == 0:
        nombre_operacion = ("No dispones de contactos en la agenda")
    else: 
        for contacto in agenda_telefonica:
            if nombre_operacion == None:
                nombre_operacion = "{} tiene asociado el numero {}".format(contacto,agenda_telefonica[contacto])
            else:
                nombre_operacion += "\n{} tiene asociado el numero {}".format(contacto,agenda_telefonica[contacto])
                
    
    imprimir_operacion(nombre_operacion)
            
    print()
    print()

while True:
    sleep(1)
    print("Estas son las operaciones que puedes realizar")
    print("1 - Agregar Contacto")
    print("2 - Remover Contacto")
    print("3 - Actualizar Contacto")
    print("4 - Ver Contacto")
    print("5 - Ver todos los contactos")
    print("6 - Salir")
    
    try:
        print()
        operacion = int(input("Número de la opción que desees: "))
    except ValueError:
        print("Selecciona una operacion valida del 1 al 6")

    else: 
        if operacion == 1:
            agregar_contacto()
        elif operacion == 2:
            remover_contacto()
        elif operacion == 3:
            actualizar_contacto()
        elif operacion == 4:
            ver_contacto()
        elif operacion == 5:
            ver_todos_contacto()
        elif operacion == 6:
            break
        else:
            print("Operacion desconocida")

print()
print("Gracias por usar la agenda telefonica")
