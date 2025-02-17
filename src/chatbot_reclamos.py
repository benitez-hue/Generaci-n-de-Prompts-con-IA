import openai
import os

# Cargar API Key desde variable de entorno
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)  # Nuevo cliente OpenAI

def generar_reclamo(orden, producto_esperado, producto_recibido):
    prompt = f"""
    Actúa como un asistente de servicio al cliente especializado en devoluciones.
    Un cliente ha reportado un error en su pedido y necesita asistencia.
    📦 **Orden N° {orden}**
    - Producto esperado: {producto_esperado}
    - Producto recibido: {producto_recibido}
    El mensaje debe ser corto, directo y mantener un tono formal.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente de servicio al cliente experto en devoluciones."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    
    return response.choices[0].message.content

