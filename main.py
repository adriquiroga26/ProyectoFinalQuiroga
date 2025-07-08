import sys
from utilidades import centrar_texto, pausar, limpiar_pantalla
from base_datos import crear_base_de_datos
from colorama import init, Fore, Style
init(autoreset=True)

def mostrar_menu_principal():
    limpiar_pantalla()
    print(centrar_texto("=" * 60))
    print(Fore.CYAN + Style.BRIGHT + centrar_texto("SISTEMA DE CONTROL DE STOCK -COSMETICA NATURAL"))
    print(centrar_texto("=" * 60))
    print(centrar_texto(""))
    print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("1. Alta de productos"))
    print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("2. Actualización de productos"))
    print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("3. Consulta de productos"))
    print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("4. Eliminación de productos"))
    print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("5. Informes y Reportes"))
    print(Fore.MAGENTA + Style.BRIGHT + centrar_texto("6. Salir"))
    print(centrar_texto(""))
    print(centrar_texto("=" * 60))
    print(Fore.CYAN + Style.BRIGHT + centrar_texto("By Adriana Quiroga"))
    print(Fore.CYAN + Style.BRIGHT + centrar_texto("Todos los derechos reservados 2025"))
    print(centrar_texto("=" * 60))
   
   
def main():
    crear_base_de_datos()
    
    while True:
        mostrar_menu_principal()

        try:
            opcion = input(Fore.CYAN + Style.BRIGHT + centrar_texto("Seleccione una opción (1-6): ")).strip()
            match opcion:
                case "1":
                    from altas import registrar_producto
                    registrar_producto()                    
                 
                case "2":
                    from actualizaciones import actualizar_producto
                    actualizar_producto()
                    
                case "3":
                    from consultas import consultar_producto
                    consultar_producto()       
                    
                case "4":
                    from eliminaciones import eliminar_producto
                    eliminar_producto()
                    
                case "5":
                    from reportes import menu_informes
                    menu_informes()    
                    
                case "6":
                    limpiar_pantalla()
                    print(Fore.CYAN + Style.BRIGHT +centrar_texto("¡Gracias por usar el sistema!"))
                    print(Fore.CYAN + Style.BRIGHT +centrar_texto("Hasta luego"))
                    sys.exit()
                case _:
                    print(Fore.RED + centrar_texto("Opción inválida. Seleccione una opción del 1 al 5.")
                    )
                    pausar()

        except KeyboardInterrupt:
            limpiar_pantalla()
            print(Fore.RED + centrar_texto("Programa interrumpido por el usuario"))
            sys.exit()
        except Exception as e:
            print(Fore.RED + centrar_texto(f"Error inesperado: {str(e)}"))
            pausar()


if __name__ == "__main__":
    main()
        
        