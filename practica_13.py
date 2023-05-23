class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Función para crear un nuevo usuario
def create_user():
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    return User(username, password)

# Función para guardar los datos del usuario en un archivo de texto
def save_user(user):
    with open("usuarios.txt", "a") as file:
        file.write(f"{user.username},{user.password}\n")

# Función para leer los datos del usuario desde el archivo de texto
def read_users():
    try:
        with open("usuarios.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No se pudo abrir el archivo.")

def main():
    option = 's'
    while option.lower() == 's':
        new_user = create_user()
        save_user(new_user)
        print("Usuario creado exitosamente.")
        option = input("¿Desea crear otro usuario? (s/n): ")

    print("Usuarios registrados:")
    read_users()

if __name__ == "__main__":
    main()
