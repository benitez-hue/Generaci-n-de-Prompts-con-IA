# generar_qr.py
import qrcode

def generar_codigo_qr(info_devolucion, nombre_archivo="codigo_qr.png"):
    """Genera un código QR con los datos de devolución."""
    qr = qrcode.make(info_devolucion)
    qr.save(nombre_archivo)
    print(f"✅ Código QR generado y guardado como {nombre_archivo}")

# Ejemplo de uso
if __name__ == "__main__":
    generar_codigo_qr("Orden: 12345 - Punto de devolución: Sucursal A")
