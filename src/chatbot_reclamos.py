def generar_reclamo(orden, producto_esperado, producto_recibido):
    if producto_esperado == producto_recibido:
        return f"✅ El producto recibido ({producto_recibido}) coincide con la orden. No se requiere reclamo."

    return f"""
    📦 **Orden N° {orden}**
    El cliente esperaba recibir un **{producto_esperado}**, pero recibió un **{producto_recibido}**.
    Se recomienda contactar al proveedor para gestionar la devolución o reposición del producto.
    """

# Prueba:
if __name__ == "__main__":
    print(generar_reclamo("12345", "Celular X", "Celular Y"))
