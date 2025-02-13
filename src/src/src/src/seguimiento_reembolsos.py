# seguimiento_reembolsos.py
import time

def seguimiento_reembolso(orden, estado):
    """Simula la actualización del estado del reembolso y validación de devolución."""
    print(f"📌 Verificando estado del reembolso para la orden {orden}...")
    time.sleep(2)

    if estado.lower() == "producto recibido":
        print(f"✅ Reembolso procesado para la orden {orden}. Será acreditado en 3 días hábiles.")
    else:
        print(f"⚠️ Aún no hemos recibido el producto de la orden {orden}. Envíe la devolución lo antes posible.")

# Ejemplo de uso
if __name__ == "__main__":
    seguimiento_reembolso("12345", "producto recibido")
