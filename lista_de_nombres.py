def ordenar_nombres(nombres):
    """
    Esta función toma una lista de nombres y los ordena alfabéticamente.
    
    Args:
        nombres (list): Una lista de nombres de personas.
    
    Returns:
        list: Una nueva lista con los nombres ordenados alfabéticamente.
    """
    # Utilizamos el método sorted para ordenar los nombres en orden alfabético
    nombres_ordenados = sorted(nombres)
    
    return nombres_ordenados

def main():
    # Lista de nombres de personas desordenada
    nombres = ["Juan", "Ana", "Pedro", "María"]
    
    # Llamamos a la función ordenar_nombres para obtener la lista de nombres ordenados
    nombres_ordenados = ordenar_nombres(nombres)
    
    # Imprimimos los nombres ordenados
    print("Nombres ordenados alfabéticamente:")
    for nombre in nombres_ordenados:
        print(nombre)

if __name__ == "__main__":
    main()