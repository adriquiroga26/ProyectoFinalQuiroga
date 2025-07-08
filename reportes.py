import sqlite3
from utilidades import centrar_texto, limpiar_pantalla, pausar
from colorama import init, Fore, Style
init(autoreset=True)


def menu_informes():
    while True:
        limpiar_pantalla()
        print(Fore.BLUE + Style.BRIGHT + centrar_texto("=" * 60))
        print(Fore.BLUE + Style.BRIGHT + centrar_texto("INFORMES Y REPORTES"))
        print(Fore.BLUE + Style.BRIGHT + centrar_texto("=" * 60))
        print(centrar_texto(""))
        print(centrar_texto("1. Listar productos con stock bajo"))
        print(centrar_texto("2. Productos ordenados por categoría"))
        print(centrar_texto("3. Productos más caros"))
        print(centrar_texto("4. Valor total del inventario"))
        print(centrar_texto("0. Volver al menú principal"))
        print(Fore.BLUE + Style.BRIGHT + centrar_texto("=" * 60))

        opcion = input(centrar_texto("Seleccione una opción: ")).strip()

        if opcion == "0":
            break

        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        if opcion == "1":
            limpiar_pantalla()
 
            print(centrar_texto("PRODUCTOS CON STOCK IGUAL O INFERIOR A UN LÍMITE"))
            print(Fore.BLUE + Style.BRIGHT + centrar_texto("=" * 60))
            
            try:
                limite = int(input(centrar_texto("Ingrese el límite de stock: ")))
            except ValueError:
                print(Fore.RED + centrar_texto("Debe ingresar un número entero válido."))
                pausar()
                return
            print("")
            cursor.execute("SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad ASC", (limite,))

            productos = cursor.fetchall()
            if productos:
                for p in productos:
                    print(centrar_texto(f"{p[1]} | Stock: {p[3]} unidades"))
                    print(Fore.BLUE + Style.BRIGHT + centrar_texto("-" * 60))
            else:
                print(Fore.GREEN + centrar_texto("Todos los productos tienen stock suficiente."))
            pausar()

        elif opcion == "2":
            limpiar_pantalla()
            print(centrar_texto("PRODUCTOS ORDENADOS POR CATEGORÍA"))
            print(Fore.BLUE + Style.BRIGHT + centrar_texto("=" * 60))
            cursor.execute("SELECT categoria, nombre, cantidad FROM productos ORDER BY categoria, nombre")
            productos = cursor.fetchall()
            if productos:
                categoria_actual = ""
                for cat, nom, cant in productos:
                    if cat != categoria_actual:
                        print()
                        print(centrar_texto(f"Categoría: {cat}"))
                        categoria_actual = cat
                    print(centrar_texto(f"   - {nom} ({cant} unidades)"))
                    print(Fore.BLUE + Style.BRIGHT + centrar_texto("-" * 60))
            else:
                print(Fore.RED + centrar_texto("No hay productos cargados."))
            pausar()

        elif opcion == "3":
            limpiar_pantalla()
            print(centrar_texto("LOS CINCO PRODUCTOS MÁS CAROS"))
            print(Fore.BLUE + Style.BRIGHT + centrar_texto("=" * 60))
            cursor.execute("SELECT nombre, precio FROM productos ORDER BY precio DESC LIMIT 5")
            productos = cursor.fetchall()
            if productos:
                for p in productos:
                    print(centrar_texto(f"{p[0]} | Precio: ${p[1]:.2f}"))
                    print(Fore.BLUE + Style.BRIGHT + centrar_texto("-" * 60))
            else:
                print(Fore.RED + centrar_texto("No hay productos disponibles."))
            pausar()

        elif opcion == "4":
            limpiar_pantalla()
            print(centrar_texto("VALOR TOTAL DEL INVENTARIO"))
            print(Fore.BLUE + Style.BRIGHT + centrar_texto("=" * 60))
            cursor.execute("SELECT SUM(precio * cantidad) FROM productos")
            total = cursor.fetchone()[0]
            if total:
                print(centrar_texto(f"Valor estimado total: ${total:.2f}"))
                print(Fore.BLUE + Style.BRIGHT + centrar_texto("=" * 60))
                print("")
            else:
                print(Fore.YELLOW + centrar_texto("No hay productos registrados."))
            pausar()

        else:
            print(Fore.RED + centrar_texto("Opción inválida"))
            pausar()

        conexion.close()

if __name__ == "__main__":
   menu_informes()