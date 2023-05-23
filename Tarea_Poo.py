class Producto:
    def __init__(self, nombre, tipo, cantidad, precio_base):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.cantidad_inicial = cantidad  # Nuevo atributo para almacenar la cantidad inicial
        self.precio_base = precio_base

    def calcular_precio_final(self):
        impuestos = {
            'papeleria': 0.16,
            'supermercado': 0.04,
            'drogueria': 0.12
        }
        impuesto = impuestos.get(self.tipo.lower(), 0)
        precio_final = self.precio_base * (1 + impuesto)
        return round(precio_final, 2)


class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.nombre == producto.nombre:
                print("Error: Ya existe un producto con ese nombre.")
                return
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def visualizar_productos(self):
        if not self.productos:
            print("No se encuentran productos en la tienda.")
        else:
            print("Productos en la tienda:")
            for producto in self.productos:
                print(f"Nombre: {producto.nombre}")
                print(f"Tipo: {producto.tipo}")
                print(f"Cantidad: {producto.cantidad}")
                print(f"Precio base: ${producto.precio_base}")
                print("--------")

    def vender_producto(self, nombre, cantidad):
        producto = self.obtener_producto(nombre)
        if producto:
            if producto.cantidad >= cantidad:
                precio_final = producto.calcular_precio_final()
                total = round(precio_final * cantidad, 2)  # Redondear a dos decimales
                producto.cantidad -= cantidad
                print(f"Se vendieron {cantidad} unidades de {producto.nombre}.")
                print(f"Total a pagar: ${total}")
            else:
                print("No hay suficiente cantidad de producto en la tienda.")
        else:
            print("El producto no existe en la tienda.")

    def abastecer_producto(self, nombre, cantidad):
        producto = self.obtener_producto(nombre)
        if producto:
            producto.cantidad += cantidad
            print(f"Se han abastecido {cantidad} unidades de {producto.nombre}.")
        else:
            print("El producto no existe en la tienda.")

    def cambiar_producto(self, nombre, tipo, cantidad, precio_base):
        producto = self.obtener_producto(nombre)
        if producto:
            producto.tipo = tipo
            producto.cantidad = cantidad
            producto.precio_base = precio_base
            print("Producto actualizado correctamente.")
        else:
            print("El producto no existe en la tienda.")

    def obtener_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def calcular_estadisticas_ventas(self):
        total_ventas = 0
        producto_mas_vendido = None
        producto_menos_vendido = None
        cantidad_mas_vendida = 0
        cantidad_menos_vendida = float('inf')

        for producto in self.productos:
            total_ventas += producto.calcular_precio_final() * producto.cantidad

            unidades_vendidas = producto.cantidad_inicial - producto.cantidad
            if unidades_vendidas > cantidad_mas_vendida:
                producto_mas_vendido = producto.nombre
                cantidad_mas_vendida = unidades_vendidas

            if unidades_vendidas < cantidad_menos_vendida:
                producto_menos_vendido = producto.nombre
                cantidad_menos_vendida = unidades_vendidas

        cantidad_productos = len(self.productos)
        if cantidad_productos > 0:
            promedio_ventas = total_ventas / cantidad_productos
        else:
            promedio_ventas = 0

        total_ventas = round(total_ventas, 2)  # Redondear a dos decimales
        promedio_ventas = round(promedio_ventas, 2)  # Redondear a dos decimales

        print("Estadísticas de ventas:")
        print(f"Producto más vendido: {producto_mas_vendido}")
        print(f"Producto menos vendido: {producto_menos_vendido}")
        print(f"Cantidad total de dinero obtenido: ${total_ventas}")
        print(f"Cantidad de dinero promedio obtenido por unidad de producto vendida: ${promedio_ventas}")


# Ejemplo de uso
tienda = Tienda()

while True:
    print("1. Agregar producto")
    print("2. Visualizar productos")
    print("3. Vender producto")
    print("4. Abastecer producto")
    print("5. Cambiar producto")
    print("6. Calcular estadísticas de ventas")
    print("7. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        tipo = input("Ingrese el tipo del producto (papeleria/supermercado/drogueria): ")
        cantidad = float(input("Ingrese la cantidad del producto: "))  # Convertir a float
        precio_base = float(input("Ingrese el precio base del producto: "))

        producto = Producto(nombre, tipo, cantidad, precio_base)
        tienda.agregar_producto(producto)
    elif opcion == 2:
        tienda.visualizar_productos()
    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))
        tienda.vender_producto(nombre, cantidad)
    elif opcion == 4:
        nombre = input("Ingrese el nombre del producto a abastecer: ")
        cantidad = int(input("Ingrese la cantidad a abastecer: "))
        tienda.abastecer_producto(nombre, cantidad)
    elif opcion == 5:
        nombre = input("Ingrese el nombre del producto a cambiar: ")
        tipo = input("Ingrese el nuevo tipo del producto: ")
        cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        precio_base = float(input("Ingrese el nuevo precio base del producto: "))
        tienda.cambiar_producto(nombre, tipo, cantidad, precio_base)
    elif opcion == 6:
        tienda.calcular_estadisticas_ventas()
    elif opcion == 7:
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
