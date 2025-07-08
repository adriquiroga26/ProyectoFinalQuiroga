import sqlite3
from utilidades import centrar_texto, limpiar_pantalla, pausar
from colorama import init, Fore, Style
init(autoreset=True)


def consultar_producto():
    while True:
        limpiar_pantalla()
        print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
        print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("CONSULTA DE PRODUCTOS"))
        print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
        print(centrar_texto(""))
        print(centrar_texto("1. Consultar producto por ID"))
        print(centrar_texto("2. Ver todos los productos"))
        print(centrar_texto("0. Volver al menú principal"))
        print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))

        opcion = input(centrar_texto("Seleccione una opción: ")).strip()

        if opcion == "0":
            break

        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        if opcion == "1":
            id = input(centrar_texto("Ingrese el ID del producto: ")).strip()
            if not id.isdigit():
                print(centrar_texto("ID inválido. Debe ser un número entero."))
                conexion.close()
                pausar()
                continue

            cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
            producto = cursor.fetchone()

            limpiar_pantalla()
            if producto:
                print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
                print(centrar_texto("=== DETALLES DEL PRODUCTO ==="))
                print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
                print(centrar_texto(f"ID: {producto[0]}"))
                print(centrar_texto(f"Nombre: {producto[1]}"))
                print(centrar_texto(f"Descripción: {producto[2]}"))
                print(centrar_texto(f"Cantidad: {producto[3]}"))
                print(centrar_texto(f"Precio: ${producto[4]:.2f}"))
                print(centrar_texto(f"Categoría: {producto[5]}"))
                print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
            else:
                print(centrar_texto("No se encontró un producto con ese ID."))

            conexion.close()
            pausar()

        elif opcion == "2":
            cursor.execute("SELECT * FROM productos ORDER BY id")
            productos = cursor.fetchall()

            limpiar_pantalla()
            if productos:
                print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
                print(centrar_texto("=== LISTADO DE PRODUCTOS ==="))
                print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
                print()
                for p in productos:
                    print(centrar_texto(f"ID: {p[0]} | Nombre: {p[1]} | Cantidad: {p[3]} | Precio: ${p[4]:.2f}"))
                    print(centrar_texto("-" * 50))
            else:
                print(Fore.YELLOW + centrar_texto("No hay productos cargados en el inventario."))

            conexion.close()
            pausar()

        else:
            conexion.close()
            print(Fore.RED + centrar_texto("Opción inválida"))
            pausar()

if __name__ == "__main__":
    consultar_producto() 