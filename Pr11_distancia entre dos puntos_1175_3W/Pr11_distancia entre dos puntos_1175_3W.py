print(" ")
print("Alvaro Campechano 3W")
print(" ")
import math

def distancia_dirigida(punto1, punto2):
    """
    Calcula la distancia dirigida y el vector entre dos puntos.

    Parameters:
    punto1 (tuple): Las coordenadas del primer punto (x1, y1).
    punto2 (tuple): Las coordenadas del segundo punto (x2, y2).

    Returns:
    tuple: Un tuple que contiene la distancia y el vector.
    
    Example:
    >>> distancia_dirigida((1, 2), (4, 6))
    (5.0, (3, 4))
    """
    x1, y1 = punto1
    x2, y2 = punto2
    
    # Calcular el vector
    vector = (x2 - x1, y2 - y1)
    
    # Calcular la distancia
    distancia = math.sqrt(vector[0]**2 + vector[1]**2)
    
    return distancia, vector

# Ejemplo de uso
if __name__ == "__main__":
    distancia, vector = distancia_dirigida((1, 2), (4, 6))
    print(f"Distancia: {distancia}")  # Debería imprimir 5.0
    print(f"Vector: {vector}")  # Debería imprimir (3, 4)
