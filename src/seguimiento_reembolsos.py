import time
import requests

def verificar_estado_envio(tracking_number):
    """Simula una consulta a una API de seguimiento de paquetes."""
    url = f"https://api.ejemplo-seguimiento.com/status/{tracking_number}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["status"]
    except:
        return "Error en la consulta"

def seguimiento_reembolso(orden, tracking_number, email_cliente):
    """Verifica el estado de la devolución y procesa el reembolso si corresponde."""
    print(f"📌 Consultando estado de la devolución para la orden {orden}...")

    estado = verificar_estado_envio(tracking_number)
    time.sleep(2)

    if estado.lower() == "entregado":
        print(f"✅ Producto recibido. Reembolso procesado para la orden {orden}.")
    else:
        print(f"⚠️ Producto aún no recibido para la orden {orden}. Estado: {estado}.")

if __name__ == "__main__":
    seguimiento_reembolso("12345", "XYZ987654", "cliente@example.com")
