

import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Carga tu DataFrame aquí. Por ejemplo:
df = pd.read_csv('/Users/alejandrovillegas-muro/Library/Mobile Documents/com~apple~CloudDocs/Personal-projects/DataSets/archive/final_combats.csv')

# Lista de columnas numéricas de interés
cols = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'height', 'weight', 'base_experience']

# Filtra el DataFrame solo con las columnas seleccionadas
df_num = df[cols]

# Calcula la matriz de correlación
corr_matrix = df_num.corr()

# Encuentra las 3 correlaciones más altas (positivas o negativas), excluyendo la diagonal
corr_pairs = corr_matrix.unstack()
corr_pairs = corr_pairs[corr_pairs.index.get_level_values(0) != corr_pairs.index.get_level_values(1)]
corr_pairs = corr_pairs.abs().sort_values(ascending=False)

# Elimina duplicados (ya que la matriz es simétrica)
corr_pairs = corr_pairs[~corr_pairs.index.duplicated()]

# Muestra las 3 correlaciones más fuertes
print("Top 3 correlaciones más fuertes (positivas o negativas):")
for (col1, col2), value in corr_pairs.head(3).items():
    print(f"{col1} - {col2}: {corr_matrix.loc[col1, col2]:.3f}")

# BONUS: Visualiza la matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de correlación')
plt.show()
