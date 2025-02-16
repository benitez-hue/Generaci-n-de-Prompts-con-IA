import openai
import os

# Cargar clave API desde variable de entorno (MUY RECOMENDADO)
openai.api_key = os.getenv("OPENAI_API_KEY")

def generar_reclamo(orden, producto_esperado, producto_recibido):
    """
    Genera un mensaje automático para la tienda vendedora en caso de error en el pedido.
    Optimizado para reducir costos de API y mejorar claridad en el mensaje.
    """

    # Si el producto recibido es el correcto, no se genera un reclamo
    if producto_esperado == producto_recibido:
        return f"✅ El producto recibido ({producto_recibido}) coincide con la orden. No se requiere reclamo."

    # Prompt mejorado con estructura más formal
    prompt = f"""
    Actúa como un asistente de servicio al cliente especializado en devoluciones.
    Un cliente ha reportado un error en su pedido y necesita asistencia.
    📦 **Orden N° {orden}**
    - Producto esperado: {producto_esperado}
    - Producto recibido: {producto_recibido}
    El mensaje debe ser corto, directo y mantener un tono formal.
    """

    # Conexión con OpenAI (Nueva API)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Cambia el modelo si tienes acceso a GPT-4
        messages=[
            {"role": "system", "content": "Eres un asistente de servicio al cliente experto en devoluciones."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100  # Limitamos tokens para reducir costos
    )

    return response["choices"][0]["message"]["content"]

# Ejemplo de uso:
if __name__ == "__main__":
    print(generar_reclamo("12345", "Celular X", "Celular Y"))

    
