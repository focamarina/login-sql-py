from getpass import getpass
import time


print("""
        Opciones para el usuario:

        1. Iniciar sesion
        2. Registrasrse

        escriba SALIR para cerrar el programa
""")

option = input('Elija una opcion: ')

if option == 'SALIR':
    exit
elif option.isdigit() == True:
    option = int(option)

    if option == 1:
        username = input("Ingrese el nombre de usuario: ")
        pwd = getpass(prompt='Ingrese su contraseña: ')
        print('Iniciando sesion...')
        time.sleep(2)
        print(username)
        print(pwd)

    elif option == 2:
        name = input('¿Cual es su nombre?: ')
        surname = input('¿Cual es su apellido?: ')
        email = input('Ingrese su email: ')
        username = input('Cree un nombre de usuario: ')
        phone = input(
            'Ingrese su numero de telefono (Con codigo de pais (+54) y codigo de area (351)): ')
        brth = input('Ingrese su fecha de nacimiento (YYYY-MM-DD): ')
        cpl = input(
            'Ingrese su pais, provincia y localidad (Hacerlo seguidos de coma: España, Madrid, Madrid): ')
        pwd = getpass('Escriba una contraseña: ')
        print('\nGracias por registrarse! Bienvenido '+name+'!')

    else:
        print('Numero incorrecto!')

else:
    print('Ups...! Ha ocurrido un error')
