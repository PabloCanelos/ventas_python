import os
os.system("cls")

def menu():
    while True:
        print("====MENÚ PRINCIPAL====")
        print("=========================")
        print("1.) 🛍️  Realizar una venta")
        print("2.) 📦  Ver stock disponible")
        print("3.) ➕  Ingresar nuevo producto al stock")
        print("4.) 🔄  Actualizar datos de un producto")
        print("5. )📈  Ver ventas realizadas hoy")
        print("6.) 💰  Ver total acumulado de ventas")
        print("7.) 🗑️  Eliminar producto del stock")
        print("8.) 🧾  Ver resumen completo del día")
        print("9. )🚪  Salir del programa")

        opcion = input("ingrese opcion a consultar o escribe 'salir' o presiona 9 \n")
        if opcion =="9"or opcion == "salir":
            print("haz salido del programa")
            break



