def generar_mensaje(nombre, producto):
    """
    Genera un mensaje personalizado para el cliente con el producto que ha comprado.
    """
    return f"{nombre}, tu {producto} está en camino. ¡Gracias por elegirnos! 🚀"

# Prueba del código
if __name__ == "__main__":
    print(generar_mensaje("Laura", "Notebook Pro"))
