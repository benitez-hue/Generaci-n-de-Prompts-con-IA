import smtplib
from email.mime.text import MIMEText

def enviar_reclamo_email(orden, producto_esperado, producto_recibido, proveedor, email_proveedor):
    """
    Genera y envía un email al proveedor en caso de error en el pedido.
    """

    # Si el producto recibido es el correcto, no se genera reclamo
    if producto_esperado == producto_recibido:
        return f"✅ El producto recibido ({producto_recibido}) coincide con la orden. No se requiere reclamo."

    # Generar mensaje de reclamo
    asunto = f"🔴 Reclamo: Error en Orden {orden}"
    mensaje = f"""
    📦 **Orden N° {orden}**  
    **Error detectado en el pedido.**  
    - **Producto esperado:** {producto_esperado}  
    - **Producto recibido:** {producto_recibido}  

    Solicitamos la corrección del error sin costos adicionales, según el acuerdo comercial vigente.

    🔹 **Proveedor responsable:** {proveedor}  
    📧 **Email del proveedor:** {email_proveedor}  
    """

    # Configuración del correo (Modificar con tus datos)
    remitente = "empresa@logistica.com"  # 📌 Cambiar por el correo real
    servidor_smtp = "smtp.example.com"  # 📌 Servidor SMTP de la empresa
    usuario = "empresa@logistica.com"  # 📌 Usuario SMTP
    contraseña = "password123"  # 📌 Contraseña del correo (¡Usar variables de entorno!)

    # Enviar el email
    try:
        msg = MIMEText(mensaje, "plain")
        msg["Subject"] = asunto
        msg["From"] = remitente
        msg["To"] = email_proveedor

        with smtplib.SMTP(servidor_smtp, 587) as server:
            server.starttls()
            server.login(usuario, contraseña)
            server.sendmail(remitente, email_proveedor, msg.as_string())

        return f"📩 Email de reclamo enviado a {email_proveedor} con éxito."

    except Exception as e:
        return f"⚠️ Error al enviar el email: {str(e)}"

# 🔥 **Prueba del código**
if __name__ == "__main__":
    print(enviar_reclamo_email("12345", "Notebook Pro", "Notebook Estándar", "Proveedor XYZ", "proveedor@empresa.com"))
