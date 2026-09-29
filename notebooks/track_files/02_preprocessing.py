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
import pandas as pd                                     # Manejar DataFrames
from pathlib import Path                                # Manejar rutas

# %% [markdown]
# # 2. Paths

# %%
PROJECT_ROOT = Path.cwd().parent
PROJECT_ROOT

# %% [markdown]
# # 3. Import data

# %%
df = pd.read_csv(PROJECT_ROOT / 'data' / 'clean' / 'clean_data.csv')

# %%
df.info()

# %% [markdown]
# # 4. Transform binary sex

# %%
df['Sex'] = df['Sex'].map({'female': 0, 'male': 1})

# %%
df.info()

# %% [markdown]
# # 5. Drop unnecessary features

# %% [markdown]
# PassengerId, Name y Ticket dificilmente nos pueda dar alguna señal importante, asi que las eliminaremos

# %%
total_categories_passengerid = df['PassengerId'].nunique()
total_categories_name = df['Name'].nunique()
total_categories_ticket = df['Ticket'].nunique()
total_rows_xtrain = len(df)

# %%
print(f"""
Categorias diferentes por filas totales
PassengerId: {total_categories_passengerid}/{total_rows_xtrain}
Name: {total_categories_name}/{total_rows_xtrain}
Ticket: {total_categories_ticket}/{total_rows_xtrain}
""")

# %% [markdown]
# Eliminar

# %%
df.drop(columns=['PassengerId', 'Name', 'Ticket'], inplace=True)

# %%
df.info()

# %% [markdown]
# # 6. Save

# %% [markdown]
# Guardaremos cada DataFrame para que esté listo para ser utilizado en modeling

# %%
df.to_csv(PROJECT_ROOT / 'data' / 'processed' / 'processed_data.csv', index=False)
