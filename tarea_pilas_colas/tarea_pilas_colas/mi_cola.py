from pasajero import Pasajero


class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.

    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)

    ⛔ Mismas prohibiciones que MiLista: ningún método ni función prediseñada de list,
       ni comprensiones. Solo datos[i], while, for i in range(), if, aux y self.cantidad.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):                     # ✅ resuelto + mejora (sin repetidos)
        if self.cantidad == self.capacidad:
            print("  ⚠ La cola está llena")
            return False
        if self.buscar(pasajero.numero) != -1:        # mejora: el número es clave única
            print(f"  ⚠ Ya existe un pasajero con el número {pasajero.numero}")
            return False
        self.datos[self.cantidad] = pasajero          # se pone a la fila por detrás
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del FRENTE al FINAL
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):                # 0, 1, ..., cantidad-1  (hacia adelante)
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTADO (tabla 3) · recorre SIEMPRE del frente al final -------
    def desencolar(self):
        # Solo puede salir el FRENTE (datos[0]). Todos los demás avanzan un lugar.
        if self.cantidad == 0:
            return None
        frente = self.datos[0]
        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]         # corro a la izquierda
        self.datos[self.cantidad - 1] = None          # el último cajón queda vacío
        self.cantidad = self.cantidad - 1
        return frente

    def ver_frente(self):
        # Mirar el frente sin sacarlo
        if self.cantidad == 0:
            return None
        return self.datos[0]

    def buscar(self, numero):
        # Búsqueda lineal DEL FRENTE AL FINAL
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)               # reutilizo buscar (ya recorre del frente)
        if posicion == -1:
            return False
        self.datos[posicion].destino = nuevo_destino  # nadie cambia de lugar
        self.datos[posicion].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        # ⚠ No se puede sacar del medio: la fila da UNA vuelta completa.
        # Se desencola `cantidad` veces; el buscado no vuelve a entrar, los demás sí.
        total = self.cantidad
        encontrado = False
        for i in range(total):
            pasajero = self.desencolar()              # siempre sale el frente
            if pasajero.numero == numero:
                encontrado = True                     # este se descarta
            else:
                self.encolar(pasajero)                # los demás vuelven al final
        return encontrado

    def copiar(self):
        # Se encola del FRENTE al FINAL: la copia queda en el mismo orden
        nueva = MiCola(self.capacidad)
        for i in range(self.cantidad):
            nueva.encolar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0
