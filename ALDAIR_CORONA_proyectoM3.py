import numpy as np  # Biblioteca para manejar arreglos y operaciones matemáticas
import matplotlib.pyplot as plt  # Biblioteca para crear gráficos y visualizar los datos
from collections import Counter  # Permite contar los elementos en una lista de manera eficiente

# Función para simular la máquina de Galton
def simulacion_galton(num_canicas=3000, niveles=12): #Definición de cantidad de canicas y numero de niveles o recipientes
    
    # Simulamos el recorrido de 'num_canicas' a través de 'niveles' de obstáculos.
    # La posición final se obtiene sumando todas las desviaciones.

    decisiones = np.random.randint(0, 2, size=(num_canicas, niveles))  # Genera decisiones aleatorias (0 o 1) para cada canica
    resultados = np.sum(decisiones, axis=1)  # Suma cada fila para obtener el contenedor final de cada canica
    return resultados

# Función para graficar el histograma con los resultados
def graficar_histograma(resultados, niveles=12):
       
    conteo = Counter(resultados)  # Cuenta cuántas canicas terminaron en cada contenedor
    etiquetas = np.arange(niveles + 1)  # Crea etiquetas para los contenedores
    valores = [conteo.get(i, 0) for i in etiquetas]  # Obtiene la cantidad de canicas en cada contenedor
    
    # Valores de edicion para el gradico de barras 
    plt.bar(etiquetas, valores, color='green', edgecolor='black') # color de los ejes y las barras 
    plt.xlabel('Posición Final del Contenedor')  # Etiqueta del eje X
    plt.ylabel('Número de Canicas')  # Etiqueta del eje Y
    plt.title('Simulación de Máquina de Galton')  # Título del gráfico
    plt.xticks(etiquetas)  # Muestra las etiquetas en el eje X
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Agrega una cuadrícula en el eje Y
    
    # Agregar los valores exactos encima de cada barra
    for i, v in enumerate(valores):
        plt.text(etiquetas[i], v + 10, str(v), ha='center', fontsize=10) 
    
    plt.show()

# Ejecutar simulación y graficar
resultados = simulacion_galton()  # Simula la caída de las canicas
graficar_histograma(resultados)  # Genera el gráfico con los resultados
