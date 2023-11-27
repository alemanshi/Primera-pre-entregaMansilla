# Registro un usuario nuevo en la DB ylo guardo
def registrar_usuario(DB, usuario, contrasena, archivo):
    if usuario not in DB:
        DB[usuario] = contrasena
        with open(archivo, 'a') as f:
            f.write(f"{usuario},{contrasena}\n")
        print("Usuario registrado exitosamente.")
    else:
        print(f"Error: El usuario '{usuario}' ya está registrado. Elige otro nombre de usuario, por favor.")

# Muestrto la información de los usuarios registrados
def mostrar_informacion(DB):
    print("Usuarios registrados:")
    for usuario, contrasena in DB.items():
        print(f"Usuario: {usuario}, Contraseña: {contrasena}")

# Inicio de sesión
def login(DB, usuario, contrasena):
    if usuario in DB and DB[usuario] == contrasena:
        print("Inicio de sesión exitoso.")
    else:
        print("Error: Usuario o contraseña incorrectos. Intentá nuevamente por favor.")

# Creo o actualizo el archivo con los usuarios que se registran
def creo_archivo_usuarios(DB, archivo):
    with open(archivo, 'w') as f:
        for usuario, contrasena in DB.items():
            f.write(f"{usuario},{contrasena}\n")

# Base de datos vacía
DB_usuarios = {}

# Nombre del archivo para almacenar usuarios
archivo_usuarios = "usuarios.txt"

# Registro usuarios
registrar_usuario(DB_usuarios, "entrega1", "12345", archivo_usuarios)
registrar_usuario(DB_usuarios, "entrega2", "678910", archivo_usuarios)

# Usuarios registrados
mostrar_informacion(DB_usuarios)

# Creo / actualizo archivo con usuarios registrados
creo_archivo_usuarios(DB_usuarios, archivo_usuarios)

# Intento de inicio de sesión de usuario NO registrados
login(DB_usuarios, "entrega3", "54321")

