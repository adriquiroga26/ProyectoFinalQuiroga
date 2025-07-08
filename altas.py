import sqlite3
from utilidades import centrar_texto, pausar, limpiar_pantalla, validar_precio, validar_cantidad
from colorama import init, Fore, Style
init(autoreset=True)


def registrar_producto():
    limpiar_pantalla()
    print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
    print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("ALTA DE PRODUCTOS"))
    print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("=" * 60))
    print(centrar_texto(""))
    while True:
        nombre = input(centrar_texto("Nombre del producto (0 para cancelar): ")).strip().title()
        if nombre == "0":
            return None
        if not nombre:
            print(Fore.YELLOW + centrar_texto("El nombre es obligatorio"))
            pausar()
            continue
        break

    while True:
        descripcion = input(centrar_texto("Descripción (0 para cancelar): ")).strip()
        if descripcion == "0":
            return None
        if not descripcion:
            print(Fore.YELLOW + centrar_texto("La descripción es obligatoria"))
            pausar()
            continue
        break
    
    while True:    
        cantidad = input(centrar_texto("Cantidad disponible (0 para cancelar): ")).strip()
        if cantidad == "0":
            return None
        if not cantidad:
            print(Fore.YELLOW + centrar_texto("La cantidad es obligatoria"))
            pausar()
            continue
        if not validar_cantidad(cantidad):
            print(Fore.RED + centrar_texto("Cantidad inválida, sólo números enteros"))
            pausar()
            continue
        break
        
    while True:      
        precio = input(centrar_texto("Precio (0 para cancelar): ")).strip()
        if precio == "0":
            return None
        if not precio:
            print(Fore.YELLOW + centrar_texto("El precio es obligatorio"))
            pausar()
            continue
        if not validar_precio(precio):
            print(Fore.RED + centrar_texto("Precio inválido, sólo números"))
            pausar()
            continue
        break     
       
    while True:  
        print(centrar_texto("Categoría: 1- Rostro, 2- Cuidados diarios, 3- Maquillaje, 4- Cabello, 5- Perfumería"))                            
        categoria = input(centrar_texto("Ingrese opción (0 para cancelar): ")).strip()
        
        if categoria == "0":
            return None
        
        if not categoria:
            print(Fore.YELLOW + centrar_texto("La categoría es obligatoria."))
            pausar()
            continue

        if not categoria.isdigit():
            print(Fore.RED + centrar_texto("Debe ingresar un número válido."))
            pausar()
            continue

        if int(categoria) not in range(1, 6):
            print(Fore.RED + centrar_texto("Ingrese un número entre 1 y 5."))
            pausar()
            continue

        break

    categoria = int(categoria)      
    cantidad = int(cantidad)
    precio = float(precio)

    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT
            )
        """)

        cursor.execute("""
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, descripcion, cantidad, precio, categoria))

        conexion.commit()
        conexion.close()

        print(Fore.GREEN + centrar_texto("Producto registrado correctamente"))
        pausar()

    except Exception as e:
        print(Fore.RED + centrar_texto(f"Error al registrar producto: {e}"))
        pausar()

if __name__ == "__main__":
    registrar_producto() 
        