class Venta:
    def __init__(self):
        self.__id_venta = None
        self.__fecha = None
        self.__cliente = None
        self.__productos = {}  # Diccionario de productos: {'producto': {'cantidad': x, 'precio_unitario': y}}
        self.__total = 0.0

    # Getters para acceder a los atributos privados
    def get_id_venta(self):
        return self.__id_venta

    def get_fecha(self):
        return self.__fecha

    def get_cliente(self):
        return self.__cliente

    def get_productos(self):
        return self.__productos

    def get_total(self):
        return self.__total

    # Setters para modificar los atributos privados
    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_productos(self, productos):
        self.__productos = productos

    def calcular_total(self):
        total = 0.0
        for producto, detalles in self.__productos.items():
            total += detalles['cantidad'] * detalles['precio_unitario']
        self.__total = total

    # Método para mostrar los detalles de la venta
    def mostrar_detalle(self):
        print(f"ID Venta: {self.__id_venta}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente}")
        print("Productos:")
        for producto, detalles in self.__productos.items():
            print(f" - {producto}: {detalles['cantidad']} unidades a ${detalles['precio_unitario']} c/u")
        print(f"Total: ${self.__total:.2f}")

# Función principal para gestionar una venta
def main():
    # Crear una nueva venta
    venta = Venta()

    # Solicitar datos de la venta al usuario
    id_venta = input("Ingrese el ID de la venta: ")
    fecha = input("Ingrese la fecha de la venta (DD/MM/AAAA): ")
    cliente = input("Ingrese el nombre del cliente: ")

    # Crear el diccionario de productos
    productos = {}
    productos_permitidos = ['Producto A', 'Producto B', 'Producto C']

    for producto in productos_permitidos:
        print(f"Ingresando datos para {producto}:")
        cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
        precio_unitario = float(input(f"Ingrese el precio unitario de {producto}: "))
        productos[producto] = {'cantidad': cantidad, 'precio_unitario': precio_unitario}

    # Asignar los valores a la instancia de Venta
    venta.set_id_venta(id_venta)
    venta.set_fecha(fecha)
    venta.set_cliente(cliente)
    venta.set_productos(productos)

    # Calcular el total de la venta
    venta.calcular_total()

    # Mostrar los detalles de la venta
    print("\nDetalles de la Venta:")
    venta.mostrar_detalle()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
