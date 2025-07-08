import os
import shutil
from colorama import init, Fore, Style
init(autoreset=True)


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def centrar_texto(texto):
    try:
        ancho_terminal = shutil.get_terminal_size().columns
    except:
        ancho_terminal = 80

    if len(texto) >= ancho_terminal:
        return texto

    espacios = (ancho_terminal - len(texto)) // 2
    return " " * espacios + texto

def pausar():
    input(centrar_texto("Presione Enter para continuar..."))
    
def validar_precio(valor):
    try:
        precio = float(valor)
        if precio < 0:
            return None
        return precio
    except ValueError:
        return None
    
def validar_cantidad(cantidad):
    try:
        cantidad = int(cantidad)
        if cantidad < 0:
            return None
        return cantidad
    except ValueError:
        return None    
