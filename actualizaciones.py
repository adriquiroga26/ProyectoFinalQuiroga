import sqlite3
from utilidades import centrar_texto, pausar, limpiar_pantalla, validar_precio, validar_cantidad
from colorama import init, Fore, Style
init(autoreset=True)


def actualizar_producto():
    limpiar_pantalla()
    print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
    print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("ACTUALIZACIÓN DE PRODUCTOS"))
    print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
        
    id = input(centrar_texto("Ingrese el ID del producto a modificar (0 para cancelar): ")).strip()
        
    if id == "0":
        return None    
    
    if not id.isdigit():
        print(centrar_texto(Fore.RED + "ID inválido"))
        pausar()
        return
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    producto = cursor.fetchone()

    if not producto:
        print(Fore.RED + centrar_texto("No se encontró un producto con ese ID"))
        conexion.close()
        pausar()
        return

    while True:
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
        producto = cursor.fetchone()

        limpiar_pantalla()
        print(centrar_texto("¿Qué desea modificar?"))
        print(centrar_texto("-" * 60))
        print(centrar_texto(f"Nombre: {producto[1]}"))
        print(centrar_texto(f"Descripción: {producto[2]}"))
        print(centrar_texto(f"Cantidad: {producto[3]}"))
        print(centrar_texto(f"Precio: {producto[4]}"))
        print(centrar_texto(f"Categoría: {producto[5]}"))
        print(centrar_texto("-" * 60))
        print(centrar_texto("-" * 60))
        print(centrar_texto("1. Modificar nombre"))
        print(centrar_texto("2. Modificar descripción"))
        print(centrar_texto("3. Modificar cantidad"))
        print(centrar_texto("4. Modificar precio"))
        print(centrar_texto("5. Modificar categoría"))
        print(centrar_texto("0. Volver"))

        opcion = input(centrar_texto("Seleccione una opción: ")).strip()

        if opcion == "0":
            break

        if opcion == "1":
            nombre = input(centrar_texto("Nuevo nombre (Enter para omitir): ")).strip().title()
            if not nombre:
                continue
            try:
                cursor.execute("UPDATE productos SET nombre = ? WHERE id = ?", (nombre, id))
                conexion.commit()
                print(Fore.GREEN +centrar_texto(" Nombre actualizado correctamente"))
            except Exception as e:
                print(Fore.RED + centrar_texto(f"Error al guardar el cambio: {e}"))
            pausar()

        elif opcion == "2":
            descripcion = input(centrar_texto("Nueva descripción (Enter para omitir): ")).strip()
            if not descripcion:
                continue
            try:
                cursor.execute(f"UPDATE productos SET descripcion = ? WHERE id = ?", (descripcion, id))
                conexion.commit()
                print(Fore.GREEN + centrar_texto("Descripcion actualizada correctamente"))
            except Exception as e:
                print(Fore.RED + centrar_texto(f"Error al guardar el cambio: {e}"))
            pausar()

        elif opcion == "3":
            cantidad = input(centrar_texto("Nueva cantidad (Enter para omitir): ")).strip()
            if not cantidad:
                continue
            if not validar_cantidad(cantidad):
                print(Fore.RED + centrar_texto("Cantidad inválida"))
                pausar()
                continue
            try:
                cursor.execute(f"UPDATE productos SET cantidad = ? WHERE id = ?", (cantidad, id))
                conexion.commit()
                print(Fore.GREEN + centrar_texto("Cantidad actualizada correctamente"))
            except Exception as e:
                print(Fore.RED + centrar_texto(f"Error al guardar el cambio: {e}"))
            pausar()
            

        elif opcion == "4":
            precio = input(centrar_texto("Nuevo precio (Enter para omitir): ")).strip()
            if not precio:
                continue
            precio = validar_precio(precio)
            if precio is None:
                print(Fore.RED + centrar_texto("Precio inválido"))
                pausar()
                continue
            try:
                cursor.execute(f"UPDATE productos SET precio = ? WHERE id = ?", (precio, id))
                conexion.commit()
                print(Fore.GREEN + centrar_texto("Precio actualizado correctamente"))
            except Exception as e:
                print(Fore.RED + centrar_texto(f"Error al guardar el cambio: {e}"))
            pausar()                      
            
        elif opcion == "5":
            print(centrar_texto("1: Rostro, 2: Cuidados diarios, 3: Maquillaje, 4: Cabello, 5: Perfumería"))
            categoria = input(centrar_texto("Nueva categoría (Enter para omitir): ")).strip()

            if not categoria:
                continue

            if not categoria.isdigit():
                print(Fore.RED + centrar_texto("Debe ingresar un número válido."))
                pausar()
                continue

            if int(categoria) not in range(1, 6):
                print(Fore.RED + centrar_texto("Ingrese un número entre 1 y 5."))
                pausar()
                continue

            categoria = int(categoria)

            try:
                cursor.execute("UPDATE productos SET categoria = ? WHERE id = ?", (categoria, id))
                conexion.commit()
                print(Fore.GREEN + centrar_texto("Categoría actualizada correctamente"))
            except Exception as e:
                print(Fore.RED + centrar_texto(f"Error al guardar el cambio: {e}"))
            pausar()
    
        else:
            print(Fore.RED + centrar_texto("Opción inválida"))
            pausar()
            continue
    conexion.close()
    

if __name__ == "__main__":
    actualizar_producto() 