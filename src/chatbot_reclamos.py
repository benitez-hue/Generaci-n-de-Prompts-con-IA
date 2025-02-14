from openai import OpenAI

api_key = "TU_API_KEY"

def generar_reclamo(orden, producto_esperado, producto_recibido):
    """Genera un mensaje automático para la tienda vendedora en caso de error en el pedido."""
    if producto_esperado == producto_recibido:
        return f"✅ El producto recibido ({producto_recibido}) coincide con la orden. No se requiere reclamo."

    prompt = f"""
    Actúa como asistente de servicio al cliente.
    📦 **Orden N° {orden}**
    - Producto esperado: {producto_esperado}
    - Producto recibido: {producto_recibido}

    🎯 **Solicitud**: Genera un mensaje formal al vendedor notificando el error y solicitando solución.
    """

    client = OpenAI(api_key=api_key)
    response = client.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=100)
    return response["choices"][0]["text"]

if __name__ == "__main__":
    print(generar_reclamo("12345", "Celular X", "Celular Y"))
