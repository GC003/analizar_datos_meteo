import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analizar_datos_meteorologicos(ruta_archivo):
    # Cargar el conjunto de datos utilizando pandas
    datos = pd.read_csv(ruta_archivo)

    # Análisis descriptivo simple
    descripcion = datos.describe()
    print(descripcion)

    # Visualizaciones más avanzadas utilizando seaborn
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Fecha', y='Temperatura', data=datos, marker='o', label='Temperatura')
    sns.lineplot(x='Fecha', y='Humedad', data=datos, marker='o', label='Humedad')
    plt.title('Análisis Meteorológico')
    plt.xlabel('Fecha')
    plt.ylabel('Valores')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    ruta_datos = 'datos/datos_meteorologicos.csv'
    analizar_datos_meteorologicos(ruta_datos)
