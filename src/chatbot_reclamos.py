import openai

# Configura tu API Key (debes reemplazar "TU_API_KEY" con tu clave real)
openai.api_key = "TU_API_KEY"

def generar_reclamo(orden, producto_esperado, producto_recibido):
    """Genera un mensaje automático para la tienda vendedora en caso de error en el pedido."""
    
    if producto_esperado == producto_recibido:
        return f"✅ El producto recibido ({producto_recibido}) coincide con la orden. No se requiere reclamo."

    prompt = f"""
    Actúa como un asistente de servicio al cliente especializado en devoluciones.

    Un cliente ha reportado un error en su pedido y necesita asistencia.

    📦 **Orden N° {orden}**
    - Producto esperado: {producto_esperado}
    - Producto recibido: {producto_recibido}

    🎯 **Solicitud**: Genera un mensaje claro y profesional para notificar al vendedor sobre el error
    y solicitar una solución rápida, ya sea reemplazo del producto o reembolso.

    El mensaje debe ser corto, directo y mantener un tono formal.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",  # Puedes usar "gpt-3.5-turbo" si no tienes acceso a GPT-4
        messages=[
            {"role": "system", "content": "Eres un asistente de atención al cliente."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )

    return response["choices"][0]["message"]["content"]

# Ejemplo de uso
if __name__ == "__main__":
    print(generar_reclamo("12345", "Celular X", "Celular Y"))
