import math

def calcular_media(numeros):
    # Calcula la suma de todos los números en la lista
    suma = sum(numeros)
    # Calcula la media dividiendo la suma entre la cantidad de números
    return suma / len(numeros)

def calcular_desviacion_estandar(numeros):
    # Calcula la media llamando a la función calcular_media
    media = calcular_media(numeros)
    # Calcula la suma de los cuadrados de las diferencias entre cada número y la media
    suma_cuadrados = sum((x - media) ** 2 for x in numeros)
    # Calcula la varianza dividiendo la suma de los cuadrados entre la cantidad de números
    varianza = suma_cuadrados / len(numeros)
    # Calcula la desviación estándar tomando la raíz cuadrada de la varianza
    desviacion_estandar = math.sqrt(varianza)
    return desviacion_estandar

def main():
    # Lista de números de ejemplo
    numeros = [2, 4, 6, 8, 10]
    # Calcula la media de los números
    media = calcular_media(numeros)
    # Calcula la desviación estándar de los números
    desviacion_estandar = calcular_desviacion_estandar(numeros)
    # Imprime la lista de números, la media y la desviación estándar
    print("Lista de números:", numeros)
    print("Media:", media)
    print("Desviación estándar:", desviacion_estandar)

if __name__ == "__main__":
    main()