import pandas as pd

# Cargar el DataFrame desde un archivo CSV (puedes cambiar la ruta del archivo)
def cargar_datos(ruta_archivo):
    try:
        df = pd.read_csv(ruta_archivo)
        print("Datos cargados exitosamente.")
        return df
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

# Mostrar información básica del DataFrame
def mostrar_informacion(df):
    print("\nInformación del DataFrame:")
    print(df.info())
    print("\nPrimeras filas del DataFrame:")
    print(df.head())
    print("\nEstadísticas descriptivas:")
    print(df.describe())

# Limpiar datos nulos
def limpiar_datos(df):
    print("\nLimpiando datos nulos...")
    df = df.dropna()  # Eliminar filas con valores nulos
    print("Datos nulos eliminados.")
    return df

# Analizar columnas específicas
def analizar_columna(df, columna):
    if columna in df.columns:
        print(f"\nAnálisis de la columna '{columna}':")
        print(df[columna].value_counts())
        print(f"\nEstadísticas de la columna '{columna}':")
        print(df[columna].describe())
    else:
        print(f"La columna '{columna}' no existe en el DataFrame.")

# Ejemplo de uso
if __name__ == "__main__":
    ruta = "ruta_a_tu_archivo.csv"  # Cambia esto por la ruta de tu archivo
    df = cargar_datos(ruta)
    if df is not None:
        mostrar_informacion(df)
        df = limpiar_datos(df)
        analizar_columna(df, "nombre_columna")  # Cambia "nombre_columna" por una columna de tu DataFrame