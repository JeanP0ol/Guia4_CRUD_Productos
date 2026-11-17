
import json


def cargar_productos():
    with open("productos.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_productos(productos):
    with open("productos.json", "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)


def crear_producto(id_producto, nombre, descripcion, precio, cantidad):
    productos = cargar_productos()

    for producto in productos:
        if producto["id"] == id_producto:
            raise ValueError("Ya existe un producto con ese ID")

    if id_producto <= 0 or precio < 0 or cantidad < 0:
        raise ValueError("El ID debe ser positivo, y el precio y la cantidad no pueden ser negativos")

    if not nombre.strip() or not descripcion.strip():
        raise ValueError("El nombre y la descripcion son obligatorios")

    nuevo_producto = {
        "id": id_producto,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(nuevo_producto)
    guardar_productos(productos)

    return nuevo_producto


def leer_producto(id_producto):
    productos = cargar_productos()

    for producto in productos:
        if producto["id"] == id_producto:
            return producto

    raise ValueError("No existe un producto con ese ID")


def actualizar_producto(id_producto, nombre, descripcion, precio, cantidad):
    productos = cargar_productos()

    for producto in productos:
        if producto["id"] == id_producto:

            if precio < 0 or cantidad < 0:
                raise ValueError("El precio y la cantidad no pueden ser negativos")

            if not nombre.strip() or not descripcion.strip():
                raise ValueError("El nombre y la descripcion son obligatorios")

            producto["nombre"] = nombre
            producto["descripcion"] = descripcion
            producto["precio"] = precio
            producto["cantidad"] = cantidad

            guardar_productos(productos)
            return producto

    raise ValueError("No existe un producto con ese ID")


def eliminar_producto(id_producto):
    productos = cargar_productos()

    for producto in productos:
        if producto["id"] == id_producto:
            productos.remove(producto)
            guardar_productos(productos)
            return producto

    raise ValueError("No existe un producto con ese ID")


def main():
    while True:
        print("\n=== REGISTRO DE PRODUCTOS ===")
        print("1. Crear producto")
        print("2. Consultar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        try:
            if opcion == "1":
                id_producto = int(input("ID: "))
                nombre = input("Nombre: ")
                descripcion = input("Descripcion: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))

                crear_producto(id_producto, nombre, descripcion, precio, cantidad)
                print("Producto registrado correctamente.")

            elif opcion == "2":
                id_producto = int(input("Ingrese el ID del producto: "))

                producto = leer_producto(id_producto)

                print("\n=== PRODUCTO ENCONTRADO ===")
                print("ID:", producto["id"])
                print("Nombre:", producto["nombre"])
                print("Descripcion:", producto["descripcion"])
                print("Precio:", producto["precio"])
                print("Cantidad:", producto["cantidad"])

            elif opcion == "3":
                id_producto = int(input("Ingrese el ID del producto a actualizar: "))

                nombre = input("Nuevo nombre: ")
                descripcion = input("Nueva descripcion: ")
                precio = float(input("Nuevo precio: "))
                cantidad = int(input("Nueva cantidad: "))

                actualizar_producto(id_producto, nombre, descripcion, precio, cantidad)
                print("Producto actualizado correctamente.")

            elif opcion == "4":
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))

                eliminar_producto(id_producto)
                print("Producto eliminado correctamente.")

            elif opcion == "5":
                print("Saliendo del programa...")
                break

            else:
                print("Opcion no valida.")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
