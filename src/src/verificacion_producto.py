import cv2
import numpy as np

def verificar_producto(imagen):
    """Simula la verificación de un producto mediante visión por computadora."""
    print(f"📦 Verificando imagen del producto: {imagen}")
    return "✅ Producto verificado (simulación)"

if __name__ == "__main__":
    resultado = verificar_producto("producto_recibido.jpg")
    print(resultado)
