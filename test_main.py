
import unittest
import json
import os
import tempfile

from main import (
    crear_producto,
    leer_producto,
    actualizar_producto,
    eliminar_producto
)


class TestCRUDProductos(unittest.TestCase):

    def setUp(self):
        self.directorio_original = os.getcwd()
        self.directorio_temporal = tempfile.TemporaryDirectory()
        os.chdir(self.directorio_temporal.name)

        with open("productos.json", "w", encoding="utf-8") as archivo:
            json.dump([], archivo)

    def tearDown(self):
        os.chdir(self.directorio_original)
        self.directorio_temporal.cleanup()

    # PRUEBAS DE CREAR

    def test_crear_producto_exitoso(self):
        producto = crear_producto(
            101, "Teclado", "Teclado USB", 50000, 8
        )

        self.assertEqual(producto["id"], 101)
        self.assertEqual(producto["nombre"], "Teclado")
        self.assertEqual(leer_producto(101), producto)

    def test_crear_producto_repetido(self):
        crear_producto(101, "Teclado", "Teclado USB", 50000, 8)

        with self.assertRaises(ValueError):
            crear_producto(101, "Mouse", "Mouse USB", 30000, 5)

    # PRUEBAS DE CONSULTAR

    def test_leer_producto_exitoso(self):
        crear_producto(102, "Mouse", "Mouse USB", 30000, 5)

        producto = leer_producto(102)

        self.assertEqual(producto["nombre"], "Mouse")
        self.assertEqual(producto["precio"], 30000)

    def test_leer_producto_inexistente(self):
        with self.assertRaises(ValueError):
            leer_producto(999)

    # PRUEBAS DE ACTUALIZAR

    def test_actualizar_producto_exitoso(self):
        crear_producto(103, "Monitor", "Monitor HD", 400000, 3)

        actualizar_producto(
            103, "Monitor LED", "Monitor Full HD", 500000, 4
        )

        producto = leer_producto(103)

        self.assertEqual(producto["nombre"], "Monitor LED")
        self.assertEqual(producto["precio"], 500000)
        self.assertEqual(producto["cantidad"], 4)

    def test_actualizar_producto_inexistente(self):
        with self.assertRaises(ValueError):
            actualizar_producto(
                999, "Monitor", "Monitor LED", 500000, 4
            )

    # PRUEBAS DE ELIMINAR

    def test_eliminar_producto_exitoso(self):
        crear_producto(104, "Audifonos", "Audifonos USB", 80000, 6)

        eliminado = eliminar_producto(104)

        self.assertEqual(eliminado["id"], 104)

        with self.assertRaises(ValueError):
            leer_producto(104)

    def test_eliminar_producto_inexistente(self):
        with self.assertRaises(ValueError):
            eliminar_producto(999)


if __name__ == "__main__":
    unittest.main()
