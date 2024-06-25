import json

"""
"UsuarioID": 1,
"Nombre": "Derek George",
"Email": "potterrebecca@yahoo.com",
"FechaRegistro": "2022-12-11"

"""
def agregar_usuario(nombre:str, email:str, fechaRegistro:str):
    
    with open("biblioteca.json", mode = "r") as agregarUsuario:
        leerJson = json.load(agregarUsuario)
        
        usuario = {
        "UsuarioID": len(leerJson["Usuario"]) + 1,
        "Nombre": nombre,
        "Email": email,
        "FechaRegistro": fechaRegistro 
        }
        leerJson["Usuario"].append(usuario)

    with open("biblioteca.json", mode = "w") as agregarUsuario:
        json.dump(leerJson, agregarUsuario, indent = 4)
        print("usuario agregado correctamente")

def editar_usuario(usuarioID:int, nombre:str, email:str, fechaRegistro:str):
    with open("biblioteca.json", mode = "r") as editarUsuario:
        leerJson = json.load(editarUsuario)
        usuarioEncontrado = False
        
        for usuario in leerJson["Usuario"]:
            if usuario["UsuarioID"] == usuarioID:
                usuario["Nombre"] = nombre
                usuario["Email"] = email
                usuario["FechaRegistro"] = fechaRegistro
                usuarioEncontrado = True
                break
            
        if not usuarioEncontrado:
            print("no se encontro el usuario")
        else:
            with open("biblioteca.json", mode = "w") as editarUsuario:
                json.dump(leerJson, editarUsuario, indent = 4)
                print("usuario editado correctamente")

def eliminar_usuario(usuarioID:int):
    with open("biblioteca.json", mode = "r") as eliminarUsuario:
        leerJson = json.load(eliminarUsuario)
        usuarioEncontrado = False
        
        for i, usuario in enumerate(leerJson["Usuario"]):
            if usuario["UsuarioID"] == usuarioID:
                leerJson["Usuario"].pop(i)
                usuarioEncontrado = True
                break
            
        if not usuarioEncontrado:
            print("no se encontro el usuario")
        else:
            for j in range(i, len(leerJson["Usuario"])):
                leerJson["Usuario"][j]["UsuarioID"] -= 1

            with open("biblioteca.json", mode = "w") as eliminarUsuario:
                json.dump(leerJson, eliminarUsuario, indent = 4)
                print("usuario eliminado correctamente")

def buscar_usuario():
    with open("biblioteca.json", mode = "r") as eliminarUsuario:
        leerJson = json.load(eliminarUsuario)
        print(leerJson["Usuario"])