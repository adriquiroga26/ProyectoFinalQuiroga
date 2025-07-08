import sqlite3
from utilidades import centrar_texto, limpiar_pantalla, pausar
from colorama import init, Fore, Style
init(autoreset=True)


def eliminar_producto():
    while True:
        limpiar_pantalla()
        print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
        print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("ELIMINACIÓN DE PRODUCTOS"))
        print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
        print(centrar_texto(""))
        
        id = input(centrar_texto("Ingrese el ID del producto a eliminar (0 para volver): ")).strip()

        if id == "0":
            return

        if not id.isdigit():
            print(Fore.RED + centrar_texto("ID inválido. Debe ser un número entero."))
            pausar()
            continue

        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
        producto = cursor.fetchone()

        if not producto:
            print(Fore.RED + centrar_texto("No se encontró un producto con ese ID."))
            conexion.close()
            pausar()
            continue

        limpiar_pantalla()
        print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
        print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("CONFIRMACIÓN DE ELIMINACIÓN"))
        print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
        print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
        print(centrar_texto(f"ID: {producto[0]}"))
        print(centrar_texto(f"Nombre: {producto[1]}"))
        print(centrar_texto(f"Descripción: {producto[2]}"))
        print(centrar_texto(f"Cantidad: {producto[3]}"))
        print(centrar_texto(f"Precio: ${producto[4]:.2f}"))
        print(centrar_texto(f"Categoría: {producto[5]}"))
        print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
        confirmacion = input(centrar_texto("¿Está seguro que desea eliminar este producto? (s/n): ")).strip().lower()

        if confirmacion == "s":
            try:
                cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
                conexion.commit()
                print(Fore.GREEN + centrar_texto("Producto eliminado correctamente."))
            except Exception as e:
                print(Fore.RED + centrar_texto(f"Error al eliminar el producto: {e}"))
        else:
            print(Fore.RED + centrar_texto("Operación cancelada por el usuario."))

        conexion.close()
        pausar()
if __name__ == "__main__":
    eliminar_producto() 