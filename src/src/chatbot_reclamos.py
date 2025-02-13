# chatbot_reclamos.py
def generar_reclamo(orden, producto_esperado, producto_recibido):
    """Genera un mensaje de reclamo en caso de error en la entrega del producto."""
    if producto_esperado == producto_recibido:
        return "✅ Producto correcto, no se requiere reclamo."
    
    return f"📢 Reclamo generado para la orden {orden}. Producto esperado: {producto_esperado}, Producto recibido: {producto_recibido}."

# Ejemplo de uso
if __name__ == "__main__":
    print(generar_reclamo("12345", "Celular X", "Celular Y"))
