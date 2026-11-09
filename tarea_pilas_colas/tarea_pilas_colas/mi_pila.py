from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.

    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)

    ⛔ Mismas prohibiciones que MiLista: ningún método ni función prediseñada de list,
       ni comprensiones. Solo datos[i], while, for i in range(), if, aux y self.cantidad.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):                      # ✅ resuelto + mejora (sin repetidos)
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        if self.buscar(pasajero.numero) != -1:        # mejora: el número es clave única
            print(f"  ⚠ Ya existe un pasajero con el número {pasajero.numero}")
            return False
        self.datos[self.cantidad] = pasajero          # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del TOPE al FONDO
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):    # cantidad-1, ..., 1, 0  (hacia atrás)
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTADO (tabla 3) · recorre SIEMPRE del tope al fondo -------
    def desapilar(self):
        # Solo puede salir el TOPE. No se corre nada: el cajón queda vacío.
        if self.cantidad == 0:
            return None
        pasajero = self.datos[self.cantidad - 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1
        return pasajero

    def ver_tope(self):
        # Mirar el tope sin sacarlo
        if self.cantidad == 0:
            return None
        return self.datos[self.cantidad - 1]

    def buscar(self, numero):
        # Búsqueda lineal DEL TOPE AL FONDO: la posición que devuelve es la de datos[]
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)               # reutilizo buscar (ya recorre del tope)
        if posicion == -1:
            return False
        self.datos[posicion].destino = nuevo_destino  # nadie cambia de lugar
        self.datos[posicion].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        # ⚠ No se puede sacar del medio: se desapila a una pila AUXILIAR
        # hasta encontrarlo, se descarta, y se devuelven los demás.
        auxiliar = MiPila(self.capacidad)
        encontrado = False

        while self.cantidad > 0 and not encontrado:
            pasajero = self.desapilar()               # siempre sale el tope
            if pasajero.numero == numero:
                encontrado = True                     # este se descarta
            else:
                auxiliar.apilar(pasajero)             # los demás esperan en la auxiliar

        # Al devolverlos, el orden original se recupera (se invierte dos veces)
        while auxiliar.cantidad > 0:
            self.apilar(auxiliar.desapilar())
        return encontrado

    def copiar(self):
        # Se apila del FONDO al TOPE (0 → cantidad-1) para que el tope siga siendo el mismo
        nueva = MiPila(self.capacidad)
        for i in range(self.cantidad):
            nueva.apilar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0
