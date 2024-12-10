""" Administrador de contraseñas """

password_host = {}

def main():
      user_main = input("Ingrese su nombre de usuario: ")
      pass_main = input("Ingrese su contraseña: ")

      """ Validar si el usuario es correcto"""
      if user_main == "admin":
            if pass_main == "12345678":
                  menu()
            else:
                  print("Contraseña incorrecta")
      else:
            print("Usuario no existe")


def menu():
      options = "Menú Principal: \n 1. Agregar Nueva contraseña \n 1. Agregar Nueva contraseña \n 3. Salir \n"
      print(options)
      choice = int(input('Seleccione una opcion: '))

      """ Validar el valor de choice """

      if choice == 1:
            add_password()
      elif choice == 2:
            get_password()
      elif choice == 3:
            main()
      else:
            print("Opción no válida")
            menu()

def add_password():
      site_adding = input("Ingrese el Sitio Web para las credenciales")
      user_adding = input("Ingrese el usuario")
      pass_adding = input("Ingrese la contraseña")
      print("Contraseña añadida")
      password_host[site_adding]={
                                  'usuario': user_adding,
                                  'password': pass_adding
                                  }
      menu()


def get_password():
      site = input("Ingrese el sitio donde se encuentra el archivo")
      print(password_host.get(site))

main()
