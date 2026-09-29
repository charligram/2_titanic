# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: venv (3.13.14)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # 1. Imports

# %%
import pandas as pd                                                     # Manejar DataFrames
from pathlib import Path                                                # Manejar rutas
from sklearn.linear_model import LogisticRegression                     # Modelo Logistic
from sklearn.ensemble import RandomForestClassifier                     # Modelo RandomForest
from sklearn.tree import DecisionTreeClassifier                         # Modelo DecisionTree
from sklearn.neighbors import KNeighborsClassifier                      # Modelo K-nearest-neighbors
from sklearn.pipeline import Pipeline                                   # Construir pipelines
from sklearn.preprocessing import StandardScaler, OneHotEncoder         # Escalar valores/Convertir features categóricas en one-hot
from sklearn.impute import SimpleImputer                                # Imputar valores
from sklearn.compose import ColumnTransformer                           # Transformar columnas
from sklearn.model_selection import train_test_split                    # Separar datos de entrenamiento y prueba


# %% [markdown]
# # 2. Paths

# %%
PROJECT_ROOT = Path.cwd().parent

# %% [markdown]
# # 3. Import data

# %%
df = pd.read_csv(PROJECT_ROOT / 'data' / 'processed' / 'processed_data.csv')


# %%
df.info()

# %% [markdown]
# # 4. Separate train/test data

# %% [markdown]
# Separaremos datos de entrenamiento y de prueba, en los datos de entrenamiento realizaremos pruebas de validación cruzada para evaluar estabilidad y rendimiento de los modelos

# %%
X = df.drop(columns=['Survived'])
y = df['Survived']

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %% [markdown]
# # 5. Create Pipeline

# %%
