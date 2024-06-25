from funciones import *

def opciones1():
    opciones1 = ("mantenedor de usuarios", "reportes", "salir")
    enumerar = 0
    print("MUNDO LIBRO")
    for i in opciones1:
        enumerar += 1
        print(f"{[(enumerar)]}.-{i}")
        
def opciones2():
    opciones2 = ("agregar usuario", "editar usuario", "eliminar usuario", "buscar usuario", "volver")
    enumerar2 = 0
    print("Mantenedor de Usuarios")
    for i in opciones2:
        enumerar2 += 1
        print(f"{[(enumerar2)]}.-{i}")

def main():
    opciones1()
    while True:
        while True:
            opcion = int(input("selecciones una opcion: "))
            if opcion > 0 and opcion < 4:
                break
            else:
                print("error, opcion invalidad intentelo denuevo")
        if opcion == 1:
            opciones2()
            while True:
                op2 = int(input("selecciones una opcion: "))
                if opcion > 0 and opcion < 6:
                    break
                else:
                    print("error, opcion invalidad intentelo denuevo")

            if op2 == 1:
                nombre = str(input("ingrese el nombre del usuario a agregar: "))
                email = str(input("ingrese el email del usuario a agregar: "))
                fechaRegistro = str(input("ingrese la fecha en la que se registro el usuario: "))
                agregar_usuario(nombre, email, fechaRegistro)
                opciones1()
            elif op2 == 2:
                usuarioID = int(input("ingrese el ID del usuario a Buscar: "))
                nombre = str(input("ingrese el nombre del usuario a agregar: "))
                email = str(input("ingrese el email del usuario a agregar: "))
                fechaRegistro = str(input("ingrese la nueva fecha de registro: "))
                editar_usuario(usuarioID, nombre, email, fechaRegistro)
                opciones1()
            elif op2 == 3:
                usuarioID = int(input("ingrese el ID del usuario que desea eliminar: "))
                eliminar_usuario(usuarioID)
                opciones1()
            elif op2 == 4:
                buscar_usuario()
                opciones1()
            elif op2 == 5:
                opciones1()
        elif opcion == 2:
            pass
        elif opcion == 3:
            break

main()