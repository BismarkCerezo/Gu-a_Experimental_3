from datetime import datetime

from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


# ------------------------- funciones de apoyo ✅ -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_texto(mensaje):
    # Repite hasta que el usuario escriba algo (no acepta vacío)
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("  Este dato no puede quedar vacío.")


def leer_numero_pasajero(mensaje):
    while True:
        numero = leer_entero(mensaje)
        if numero > 0:
            return numero
        print("  El número de pasajero debe ser mayor a 0.")


def leer_cedula(mensaje):
    while True:
        cedula = input(mensaje).strip()
        if cedula.isdigit() and len(cedula) == 10:
            return cedula
        print("  La cédula debe tener exactamente 10 dígitos.")


def leer_edad(mensaje):
    while True:
        edad = leer_entero(mensaje)
        if 0 <= edad <= 120:
            return edad
        print("  La edad debe estar entre 0 y 120.")


def leer_fecha(mensaje):
    while True:
        fecha = input(mensaje).strip()
        try:
            datetime.strptime(fecha, "%Y-%m-%d")     # comprueba el formato AAAA-MM-DD
            return fecha
        except ValueError:
            print("  Fecha inválida. Use el formato AAAA-MM-DD (ej: 2026-11-15).")


def leer_pasajero():
    numero = leer_numero_pasajero("  N.º de pasajero: ")
    nombre = leer_texto("  Nombre: ")
    cedula = leer_cedula("  Cédula: ")
    edad = leer_edad("  Edad: ")
    fecha = leer_fecha("  Fecha de vuelo (AAAA-MM-DD): ")
    destino = leer_texto("  Destino: ")
    asiento = leer_texto("  Asiento: ").upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


# ---------------------- MENÚ 1 · PILA ----------------------
# Patrón de cada opción:  1. LEER (input)  →  2. LLAMAR (método)  →  3. MOSTRAR (print)
def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()
        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if pila.apilar(pasajero):                  # 2. LLAMAR
                print("  ✓ Apilado: ahora es el tope") # 3. MOSTRAR
        elif op == "2":
            pila.listar()
        elif op == "3":
            salio = pila.desapilar()
            if salio is None:
                print("  La pila está vacía")
            else:
                tope = pila.ver_tope()
                if tope is None:
                    print(f"  Salió: {salio.nombre} · la pila quedó vacía")
                else:
                    print(f"  Salió: {salio.nombre} · nuevo tope: {tope.nombre}")
        elif op == "4":
            tope = pila.ver_tope()
            if tope is None:
                print("  La pila está vacía")
            else:
                print(f"  Tope: {tope.nombre} ({tope.numero})")
        elif op == "5":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            posicion = pila.buscar(numero)
            if posicion == -1:
                print("  No existe")
            else:
                print(f"  Encontrado en [{posicion}]: {pila.datos[posicion].nombre}")
        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            destino = leer_texto("  Nuevo destino: ")
            asiento = leer_texto("  Nuevo asiento: ").upper()
            if pila.modificar(numero, destino, asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe")
        elif op == "7":
            numero = leer_entero("  N.º de pasajero a eliminar: ")
            if pila.eliminar_por_numero(numero):
                print(f"  ✓ Pasajero {numero} eliminado; el orden se mantiene")
            else:
                print("  No existe")
        elif op == "8":
            copia = pila.copiar()
            print("  Original:")
            pila.listar()
            print("  Copia (se lista igual):")
            copia.listar()
        elif op == "9":
            estado = "está vacía" if pila.esta_vacia() else "no está vacía"
            print(f"  Longitud: {pila.longitud()} · {estado}")
        elif op == "C":
            nuevos = 0
            for p in datos_prueba():
                if pila.apilar(p):                     # apilar rechaza los números repetidos
                    nuevos = nuevos + 1
            print(f"  ✓ Datos de prueba apilados ({nuevos} nuevos)")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()
        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if cola.encolar(pasajero):                 # 2. LLAMAR
                print("  ✓ Encolado: está al final")   # 3. MOSTRAR
        elif op == "2":
            cola.listar()
        elif op == "3":
            salio = cola.desencolar()
            if salio is None:
                print("  La cola está vacía")
            else:
                frente = cola.ver_frente()
                if frente is None:
                    print(f"  Salió: {salio.nombre} · la cola quedó vacía")
                else:
                    print(f"  Salió: {salio.nombre} · nuevo frente: {frente.nombre}")
        elif op == "4":
            frente = cola.ver_frente()
            if frente is None:
                print("  La cola está vacía")
            else:
                print(f"  Frente: {frente.nombre} ({frente.numero})")
        elif op == "5":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            posicion = cola.buscar(numero)
            if posicion == -1:
                print("  No existe")
            else:
                print(f"  Encontrado en [{posicion}]: {cola.datos[posicion].nombre}")
        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            destino = leer_texto("  Nuevo destino: ")
            asiento = leer_texto("  Nuevo asiento: ").upper()
            if cola.modificar(numero, destino, asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe")
        elif op == "7":
            numero = leer_entero("  N.º de pasajero a eliminar: ")
            if cola.eliminar_por_numero(numero):
                print(f"  ✓ Pasajero {numero} eliminado; el orden se mantiene")
            else:
                print("  No existe")
        elif op == "8":
            copia = cola.copiar()
            print("  Original:")
            cola.listar()
            print("  Copia (se lista igual):")
            copia.listar()
        elif op == "9":
            estado = "está vacía" if cola.esta_vacia() else "no está vacía"
            print(f"  Longitud: {cola.longitud()} · {estado}")
        elif op == "C":
            nuevos = 0
            for p in datos_prueba():
                if cola.encolar(p):                    # encolar rechaza los números repetidos
                    nuevos = nuevos + 1
            print(f"  ✓ Datos de prueba encolados ({nuevos} nuevos)")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma interrumpido por el usuario.")
