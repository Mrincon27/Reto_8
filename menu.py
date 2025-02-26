class MenuItem:
    def __init__(self, nombre: str, precio: float, descuento: float = 0):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento

    def calcular_precio(self) -> float:
        return self.precio - (self.precio * self.descuento / 100)


class Bebida(MenuItem):
    def __init__(self, nombre: str, precio: float, tamano: str, descuento: float = 0):
        super().__init__(nombre, precio, descuento)
        self.tamano = tamano


class Aperitivo(MenuItem):
    def __init__(self, nombre: str, precio: float, para_compartir: bool, descuento: float = 0):
        super().__init__(nombre, precio, descuento)
        self.para_compartir = para_compartir


class PlatoPrincipal(MenuItem):
    def __init__(self, nombre: str, precio: float, es_vegetariano: bool, descuento: float = 0):
        super().__init__(nombre, precio, descuento)
        self.es_vegetariano = es_vegetariano


class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, item: MenuItem):
        self.items.append(item)

    def calcular_total(self) -> float:
        return sum(item.calcular_precio() for item in self.items)

    def __iter__(self):
        return iter(self.items)


menu = [
    Bebida("Coca Cola", 1.5, "500ml", descuento=5),
    Bebida("Agua Mineral", 1.0, "500ml", descuento=0),
    Bebida("Café", 2.0, "Taza", descuento=10),
    Aperitivo("Papas Fritas", 3.5, True, descuento=15),
    Aperitivo("Nachos", 5.0, True, descuento=5),
    Aperitivo("Alitas de Pollo", 6.0, False, descuento=0),
    PlatoPrincipal("Hamburguesa", 8.5, False, descuento=10),
    PlatoPrincipal("Ensalada César", 7.0, True, descuento=0),
    PlatoPrincipal("Pasta Carbonara", 9.0, False, descuento=5),
    PlatoPrincipal("Pizza Margarita", 10.0, True, descuento=20),
]

pedido = Pedido()
pedido.agregar_item(menu[0])  # Coca Cola
pedido.agregar_item(menu[3])  # Papas Fritas
pedido.agregar_item(menu[6])  # Hamburguesa

total = pedido.calcular_total()
print(f"Total del pedido: ${total:.2f}")

print("\nDetalles del pedido:")
for item in pedido:
    print(f"{item.nombre} - ${item.calcular_precio():.2f} (Descuento: {item.descuento}%)")