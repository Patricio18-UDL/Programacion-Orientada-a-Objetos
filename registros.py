class Empleados:
    def __init__(self, id_empleado, nombre, apellido, sexo, edad):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.nomina_calculada = False

    def calculaNomina(self):
        self.nomina_calculada = True
        print("-> Acción: Nomina calculada con exito para el empleado:", self.nombre, self.apellido)


class Bombas:
    def __init__(self, id_bomba, numerobomba, estado, modelo, litrosbomba):
        self.id_bomba = id_bomba
        self.numerobomba = numerobomba
        self.estado = estado
        self.modelo = modelo
        self.litrosbomba = litrosbomba

    def actualizar(self, nuevo_estado):
        self.estado = nuevo_estado
        print("-> Acción: Bomba numero", self.numerobomba, "actualizada a estado:", self.estado)


class Gasolina:
    def __init__(self, id_combustible, tipo, precio, octanaje, proveedor):
        self.id_combustible = id_combustible
        self.tipo = tipo
        self.precio = precio
        self.octanaje = octanaje
        self.proveedor = proveedor

    def ajustePrecio(self, nuevo_precio):
        self.precio = nuevo_precio
        print("-> Acción: El precio del combustible", self.tipo, "se ha ajustado a:", self.precio)


class Venta:
    def __init__(self, id_venta, fecha, litrosvendidos, pagototal, metododepago):
        self.id_venta = id_venta
        self.fecha = fecha
        self.litrosvendidos = litrosvendidos
        self.pagototal = pagototal
        self.metododepago = metododepago
        self.activa = True

    def anularVenta(self):
        self.activa = False
        print("-> Acción: La venta con ID", self.id_venta, "ha sido anulada.")


class Tienda:
    def __init__(self, id_producto, nombre_articulo, precio_unitario, stock, categoria):
        self.id_producto = id_producto
        self.nombre_articulo = nombre_articulo
        self.precio_unitario = precio_unitario
        self.stock = stock
        self.categoria = categoria

    def consultarStock(self):
        print("-> Acción: Producto:", self.nombre_articulo, "| Stock actual:", self.stock, "unidades.")


emp1 = Empleados(101, "Carlos", "Patricio", "Hombre", 19)
emp2 = Empleados(102, "Ana", "Gomez", "Mujer", 25)

bomba1 = Bombas(1, 4, "Activa", "Tokheim", 1250.5)
bomba2 = Bombas(2, 5, "Mantenimiento", "Gilbarco", 0.0)

gas1 = Gasolina(501, "Magna", 22.50, 87, "Pemex")
gas2 = Gasolina(502, "Premium", 24.80, 91, "Mobil")

venta1 = Venta(9001, "2026-05-20", 40.0, 900.0, "Efectivo")
venta2 = Venta(9002, "2026-05-20", 25.0, 620.0, "Tarjeta")

prod1 = Tienda(301, "Aceite para Motor", 150.0, 15, "Automotriz")
prod2 = Tienda(302, "Agua Purificada", 20.0, 50, "Bebidas")


print("\n=== CLASE: EMPLEADOS ===")
print("Datos del registro:", emp1.id_empleado, emp1.nombre, emp1.apellido, emp1.sexo, emp1.edad, "| Nomina:", emp1.nomina_calculada)
emp1.calculaNomina()

print("\n=== CLASE: BOMBAS ===")
print("Datos del registro:", bomba1.id_bomba, bomba1.numerobomba, bomba1.estado, bomba1.modelo, bomba1.litrosbomba)
bomba1.actualizar("Fuera de Servicio")

print("\n=== CLASE: GASOLINA ===")
print("Datos del registro:", gas1.id_combustible, gas1.tipo, gas1.precio, gas1.octanaje, gas1.proveedor)
gas1.ajustePrecio(22.90)

print("\n=== CLASE: VENTA ===")
print("Datos del registro:", venta1.id_venta, venta1.fecha, venta1.litrosvendidos, venta1.pagototal, venta1.metododepago, "| Activa:", venta1.activa)
venta1.anularVenta()

print("\n=== CLASE: TIENDA ===")
print("Datos del registro:", prod1.id_producto, prod1.nombre_articulo, prod1.precio_unitario, prod1.stock, prod1.categoria)
prod1.consultarStock()
print("")