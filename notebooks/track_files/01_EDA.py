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
import pandas as pd                 # Manejar DataFrames
from pathlib import Path            # Manejar rutas
import matplotlib.pyplot as plt     # Gráficos matplotlib
import seaborn as sns               # Gráficos seaborn
import numpy as np                  # Cálculos con numpy

# %% [markdown]
# # 2. Get data

# %% [markdown]
# Obtener dirección de carpetas necesarias

# %%
PROJECT_ROOT = Path.cwd().parent
print(PROJECT_ROOT)

# %%
FIGURES_PATH = PROJECT_ROOT / 'outputs' / 'figures'
print(FIGURES_PATH)

# %% [markdown]
# Leer train

# %%
df = pd.read_csv(PROJECT_ROOT / 'data' / 'raw' / 'train.csv')

# %% [markdown]
# # 3. Initial analysis

# %% [markdown]
# Info

# %%
df.info()

# %% [markdown]
# Head

# %%
df.head()

# %% [markdown]
# Describe

# %%
df.describe()

# %% [markdown]
# # 4. Raw EDA

# %% [markdown]
# Esto será una exploración inicial de los datos sucios

# %% [markdown]
# Vamos a generar una constante para siempre organizar en orden 0-1, o sea "Not survived" y "Survived". Otra constante para el orden en palabras. Y otra para definir colores para cada valor.

# %%
SURVIVED_ORDER = [0, 1]
SURVIVED_ORDER_STR = ['Not survived', 'Survived']
SURVIVED_COLORS = ["#ff4343", "#3a68fd"]

# %% [markdown]
# Además crearemos un DataFrame que de sobrevivientes y otro de no sobrevivientes, lo cual puede ayudar en ciertos casos.

# %%
df_survivors = df[df['Survived'] == 1].copy()
df_no_survivors = df[df['Survived'] == 0].copy()

# %% [markdown]
# ## 4.1 Survival distribution

# %% [markdown]
# Contar

# %%
count_survived = df['Survived'].value_counts().reindex(SURVIVED_ORDER)
count_survived

# %%
plt.pie(
    count_survived,
    labels=['Not survived', 'Survived'],
    autopct='%1.2f%%',
    pctdistance=0.7,
    wedgeprops={
        'edgecolor': 'black',
        'linewidth': 2,
        'width': 0.5
    },
    colors=SURVIVED_COLORS
)

plt.legend()
plt.tight_layout()
plt.title('Survival rate')

plt.savefig(FIGURES_PATH / '01_survival_rate.png', bbox_inches='tight')
plt.show()

# %% [markdown]
# ## 4.2 Pclass

# %% [markdown]
# ### 4.2.1 Proportions of Pclass

# %%
df.head()

# %%
count_total_pclass = df['Pclass'].value_counts().reindex([1, 2, 3])
count_total_pclass

# %%
plt.figure(figsize=(10, 5))

count_total_pclass.plot(
    kind='bar',
    color=SURVIVED_COLORS[1],
    edgecolor='black',
    linewidth=2

)
plt.grid(axis='y', linestyle='--', alpha=0.5, color=SURVIVED_COLORS[0])

plt.xticks(rotation=0)

plt.xlabel('Pclass')
plt.ylabel('Count')
plt.title('Count of Pclass passengers')


plt.savefig(FIGURES_PATH / '02_count_pclass.png', bbox_inches='tight')
plt.show()

# %% [markdown]
# ### 4.2.2 Survived rate by Pclass

# %% [markdown]
# Contar por cada tipo de Pclass

# %%
count_pclass_1 = df[df['Pclass'] == 1]['Survived'].value_counts()
count_pclass_1

# %%
count_pclass_2 = df[df['Pclass'] == 2]['Survived'].value_counts()
count_pclass_2

# %%
count_pclass_3 = df[df['Pclass'] == 3]['Survived'].value_counts()
count_pclass_3

# %% [markdown]
# Visualizar cada proporción

# %%
pclass_groups_data = [count_pclass_1, count_pclass_2, count_pclass_3]
pclass_options = ['Pclass 1', 'Pclass 2', 'Pclass 3']

# %%
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

# Iterar sobre cada grupo, obteniendo indice para el axes y nombre de la pclass (se hace reindex para ordenar la data en orden 0-1)
for i, (data, pclass) in enumerate(zip(pclass_groups_data, pclass_options)):
    data = data.reindex(SURVIVED_ORDER)
    ax[i].pie(
        data,
        colors=SURVIVED_COLORS,
        autopct='%1.2f%%',
        wedgeprops={
            'width': 0.5,
            'edgecolor': 'black',
            'linewidth': 2
        },
        pctdistance=0.7,
    )
    ax[i].set_title(pclass, pad=-50)

fig.legend(SURVIVED_ORDER_STR, fontsize='13')

fig.suptitle('Survival rate by Pclass')

plt.savefig(FIGURES_PATH / '03_survival_rate_by_pclass', bbox_inches='tight')
plt.show()

# %% [markdown]
# ## 4.3 Sex

# %% [markdown]
# ### 4.3.1 Sex distribution

# %%
count_sex = df['Sex'].value_counts()
count_sex

# %%
plt.figure(figsize=(10, 5))

count_sex.plot(
    kind='bar',
    color=SURVIVED_COLORS[1],
    edgecolor='black',
    linewidth=2
)

plt.grid(axis='y', linestyle='--', alpha=0.5, color=SURVIVED_COLORS[0])

plt.xticks(rotation=0)

plt.xlabel('Sex')
plt.ylabel('Count')

plt.savefig(FIGURES_PATH / '04_count_sex.png', bbox_inches='tight')
plt.show()

# %% [markdown]
# ### 4.3.2 Survived rate by Sex

# %%
df.head()

# %%
group_sex_survived = df.groupby('Sex')['Survived'].value_counts().unstack()
group_sex_survived

# %%
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

for i, sex in enumerate(group_sex_survived.index):
    survival_values = group_sex_survived.loc[sex]
    survival_values = survival_values.reindex(SURVIVED_ORDER)

    ax[i].pie(
        survival_values,
        colors=SURVIVED_COLORS,
        autopct='%1.2f%%',
        pctdistance=0.7,
        wedgeprops={
            'width': 0.5,
            'linewidth': 2,
            'edgecolor': 'black'
        }
    )
    ax[i].set_title(sex.capitalize())

fig.subplots_adjust(wspace=0)
fig.legend(SURVIVED_ORDER_STR)
fig.suptitle('Survival rate by Sex')

plt.savefig(FIGURES_PATH / '05_survival_rate_by_sex.png', bbox_inches='tight')
plt.show()

# %% [markdown]
# ## 4.4 Age

# %% [markdown]
# ### 4.4.1 Age distribution

# %%
df.head()

# %%
plt.figure(figsize=(10, 5))

sns.histplot(
    df['Age'],
    color=SURVIVED_COLORS[1],
    edgecolor='black',
    linewidth=2,
    kde=True
)

plt.grid(axis='y', linestyle='--', alpha=0.5, color=SURVIVED_COLORS[0])

plt.title('Age Distribution')

plt.savefig(FIGURES_PATH / '06_age_distribution.png')
plt.show()

# %% [markdown]
# ### 4.4.2 Age distribution in survivors/no survivors

# %%
plt.figure(figsize=(10, 5))


sns.histplot(
    df_survivors['Age'],
    color=SURVIVED_COLORS[1],
    label='Survived',
    kde=True
)

sns.histplot(
    df_no_survivors['Age'],
    color=SURVIVED_COLORS[0],
    alpha=0.6,
    label='Not survived',
    kde=True
)

plt.legend()

plt.title('Age Distribution in survived/no survived groups')

plt.savefig(FIGURES_PATH / '06_01_age_distribution_in_survived_no_survived_groups.png')
plt.show()

# %% [markdown]
# ### 4.4.3 See age groups survivors rates

# %% [markdown]
# Dividiremos en grupos cada 10 años para ver probabilidades de sobrevivir

# %%
bins = [i for i in range(0, 100, 10)]

age_groups = pd.cut(df['Age'], bins=bins)

# observed=True es para que si hay un grupo que no tiene ningún registro, no considera ese grupo
age_group_surv_rate = df.groupby(age_groups, observed=True)['Survived'].mean()
age_group_surv_rate

# %% [markdown]
# Ahora graficar

# %%
plt.figure(figsize=(15, 5))

age_group_surv_rate.plot(
    kind='bar',
    color=SURVIVED_COLORS[1],
    edgecolor='black',
    linewidth=2
)

plt.grid(axis='y', color=SURVIVED_COLORS[0], linestyle='--', alpha=0.5)

plt.xlabel('Group Age')
plt.ylabel('Probability')

plt.xticks(rotation=0)

plt.title('Probability of survive by age groups')

plt.savefig(FIGURES_PATH / '07_probability_of_survive_by_age_groups.png', bbox_inches='tight')
plt.show()

# %% [markdown]
# ## 4.5 SibSp

# %%
df.head()

# %% [markdown]
# Contar cada categoría

# %%
value_counts_of_sibsp = df['SibSp'].value_counts()
value_counts_of_sibsp

# %% [markdown]
# Obtener probabilidades de sobrevivencia de cada uno

# %%
sibsp_group_surv_rate = df.groupby('SibSp')['Survived'].mean()
sibsp_group_surv_rate

# %% [markdown]
# Graficar

# %%
plt.figure(figsize=(15, 5))

sibsp_group_surv_rate.plot(
    kind='bar',
    color=SURVIVED_COLORS[1],
    edgecolor='black',
    linewidth=2
)

plt.grid(axis='y', color=SURVIVED_COLORS[0], linestyle='--', alpha=0.5)

plt.xlabel('Number of siblings/spouses')
plt.ylabel('Probability')

plt.xticks(rotation=0)

plt.title('Probability of survive by SibSp')

plt.savefig(FIGURES_PATH / '08_probability_of_survive_by_sibsp.png', bbox_inches='tight')
plt.show()

# %% [markdown]
# ## 4.6 Parch

# %%
df.head()

# %% [markdown]
# Contar categorías

# %%
value_counts_of_parch = df['Parch'].value_counts()
value_counts_of_parch

# %% [markdown]
# Ver probabilidades de sobreviviencia

# %%
parch_group_surv_rate = df.groupby('Parch')['Survived'].mean()
parch_group_surv_rate

# %% [markdown]
# Graficar

# %%
plt.figure(figsize=(15, 5))

parch_group_surv_rate.plot(
    kind='bar',
    color=SURVIVED_COLORS[1],
    edgecolor='black',
    linewidth=2
)

plt.grid(axis='y', color=SURVIVED_COLORS[0], linestyle='--', alpha=0.5)

plt.title('Probability of survive by Parch')

plt.xlabel('Number of parents/children')
plt.ylabel('Probability')

plt.xticks(rotation=0)


plt.savefig(FIGURES_PATH / '09_probability_of_survive_by_parch.png', bbox_inches='tight')
plt.show()

# %% [markdown]
# ## 4.7 Fare

# %% [markdown]
# ### 4.7.1 Fare distribution histogram

# %%
df.head()

# %%
plt.figure(figsize=(15, 5))

sns.histplot(
    df['Fare'],
    color=SURVIVED_COLORS[1]
)

plt.grid(axis='y', linestyle='--', color=SURVIVED_COLORS[0], alpha=0.5)

plt.title('Fare distribution')

plt.savefig(FIGURES_PATH / '10_fare_distribution.png', bbox_inches='tight')
plt.show()

# %% [markdown]
# ### 4.7.2 Fare distribution in no survivors and survivors

# %%
fig, ax = plt.subplots(figsize=(12, 5))

ax.boxplot(
    [df_no_survivors['Fare'], df_survivors['Fare']],
    tick_labels=SURVIVED_ORDER_STR,
    patch_artist=True,                                   # Habilitar relleno de cajas

    boxprops={                                           # Propiedades de la caja
        'facecolor': SURVIVED_COLORS[1],                 # Color de la caja
        'edgecolor': 'black',                            # Color borde de la caja
        'linewidth': 2                                   # Grosor borde de la caja
    },

    medianprops={                                        # Propiedades de la linea de mediana
        'color': SURVIVED_COLORS[0],                     # Color
        'linewidth': 2                                   # Grosor
    },

    whiskerprops={                                       # Propiedades de los bigotes
        'color': 'black',                                # Color
        'linewidth': 2                                   # Grosor
    },

    capprops={                                           # Propiedades de las barras horizontales al final de los bigotes
        'color': 'black',                                # Color
        'linewidth': 2                                   # Grosor
    }
)

plt.ylabel('Fare')

plt.title('Fare distribution in no survivors/survivors')

plt.savefig(FIGURES_PATH / '11_fare_dist_boxplot_surv_no_surv.png', bbox_inches='tight')
plt.show()

# %% [markdown]
# ### 4.7.3 Log Fare distribution in no survivors and survivors

# %% [markdown]
# Para poder ver más explicitamente las diferencias de los grupos, aplicaremos logaritmo en los fare de cada grupo.

# %%
df_log_fare_survivors = df_survivors.copy()
df_log_fare_no_survivors = df_no_survivors.copy()

# Se utilizó log1p ya que hay fare en 0 y el log de 0 daría -infinito, asi que log1p hacer log(x + 1)
df_log_fare_survivors['Fare'] = np.log1p(df_log_fare_survivors['Fare'])
df_log_fare_no_survivors['Fare'] = np.log1p(df_log_fare_no_survivors['Fare'])

# %% [markdown]
# Graficar (aplicar misma lógica de gráfico anterior)

# %%
fig, ax = plt.subplots(figsize=(12, 5))

ax.boxplot(
    [df_log_fare_no_survivors['Fare'], df_log_fare_survivors['Fare']],
    tick_labels=SURVIVED_ORDER_STR,
    patch_artist=True,                                   # Habilitar relleno de cajas

    boxprops={                                           # Propiedades de la caja
        'facecolor': SURVIVED_COLORS[1],                 # Color de la caja
        'edgecolor': 'black',                            # Color borde de la caja
        'linewidth': 2                                   # Grosor borde de la caja
    },

    medianprops={                                        # Propiedades de la linea de mediana
        'color': SURVIVED_COLORS[0],                     # Color
        'linewidth': 2                                   # Grosor
    },

    whiskerprops={                                       # Propiedades de los bigotes
        'color': 'black',                                # Color
        'linewidth': 2                                   # Grosor
    },

    capprops={                                           # Propiedades de las barras horizontales al final de los bigotes
        'color': 'black',                                # Color
        'linewidth': 2                                   # Grosor
    }
)

plt.ylabel('Log Fare')

plt.title('Log Fare distribution in no survivors/survivors')

plt.savefig(FIGURES_PATH / '12_log_fare_dist_boxplot_surv_no_surv.png', bbox_inches='tight')
plt.show()

# %% [markdown]
# ## 4.8 Cabin

# %%
df.head()

# %% [markdown]
# Cantidad de categorías diferentes

# %%
df['Cabin'].nunique()

# %% [markdown]
# Tiene demasiadas categorías, además muchos nulos

# %%
df.info()

# %% [markdown]
# ## 4.9 Embarked

# %%
df.head()

# %% [markdown]
# Cantidad de categorías diferentes

# %%
df['Embarked'].nunique()

# %% [markdown]
# Cuenta de cada una

# %%
value_counts_of_embarked = df['Embarked'].value_counts()
value_counts_of_embarked

# %% [markdown]
# Graficar proporciones

# %%
group_embarked_survived = df.groupby('Embarked')['Survived'].value_counts().unstack()
group_embarked_survived

# %%
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

for i, embarked in enumerate(group_embarked_survived.index):
    survival_values_by_embarked_type = group_embarked_survived.loc[embarked].reindex(SURVIVED_ORDER)

    ax[i].pie(
        survival_values_by_embarked_type,
        colors=SURVIVED_COLORS,
        autopct='%1.2f%%',
        pctdistance=0.7,
        wedgeprops={
            'edgecolor': 'black',
            'linewidth': 2,
            'width': 0.5
        }
    )

    ax[i].set_title(f'Embarked: {embarked}')

fig.legend(SURVIVED_ORDER_STR)

fig.suptitle('Survived rate by Embarked')

plt.savefig(FIGURES_PATH / '13_probability_of_survive_by_embarked.png', bbox_inches='tight')
plt.show()


# %% [markdown]
# Veamos si el lugar de embarcación pueda tener que ver con Pclass

# %%
value_counts_of_pclass_by_embarked = df.groupby('Embarked')['Pclass'].value_counts().unstack()
value_counts_of_pclass_by_embarked

# %%
for embarked_site in value_counts_of_pclass_by_embarked.index:
    print(value_counts_of_pclass_by_embarked.loc[embarked_site])

# %% [markdown]
# Visualizar

# %%
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

for i, embarked_site in enumerate(value_counts_of_pclass_by_embarked.index):

    embarked_group_pclass = value_counts_of_pclass_by_embarked.loc[embarked_site].reindex([1, 2, 3])
    print(embarked_group_pclass)

    ax[i].pie(
        embarked_group_pclass,
        # Función lambda para convertir los % a número crudos utilizando regla de 3, redondeando y dejando 0 decimales.
        autopct=lambda pct: f'{np.round((pct * embarked_group_pclass.sum()) / 100):.0f}',
        colors=[SURVIVED_COLORS[1], "#3DC031", SURVIVED_COLORS[0]],
        wedgeprops={
            'width': 0.5,
            'edgecolor': 'black',
            'linewidth': 2
        },
        pctdistance=0.7
    )

    ax[i].set_title(f'Embarked: {embarked_site}')

fig.suptitle('Pclass by embarked sites')

fig.subplots_adjust(-0.5)

plt.tight_layout()

plt.legend(['Pclass 1', 'Pclass 2', 'Pclass 3'])

plt.savefig(FIGURES_PATH / '14_pclass_by_embarked.png', bbox_inches='tight')
plt.show()

# %% [markdown]
# # 5. Clean data

# %% [markdown]
# ## 5.1 Age

# %% [markdown]
# Falta datos en "Age", pero imputaremos con mediana, por lo que queda para el proceso de separación de datos train/test

# %% [markdown]
# ## 5.2 Cabin

# %%
df.info()

# %% [markdown]
# Como antes vimos que casi todos los Cabin son distintos y además hay muchos nulos, eliminaremos la columna

# %%
df = df.drop(columns=['Cabin'])

# %%
df.info()

# %% [markdown]
# ## 5.3 Embarked

# %% [markdown]
# Embarked tiene pocos nulos, simplemente rellenaremos con el valor más común pero también en train/test

# %%
df.info()

# %% [markdown]
# ## 5.4 Duplicates

# %% [markdown]
# Veamos si tenemos duplicados primero

# %%
df.duplicated().sum()

# %% [markdown]
# Ahora si es que hay personas con nombres duplicados

# %%
df['Name'].duplicated().sum()

# %% [markdown]
# # 6. Save

# %% [markdown]
# Guardar la información en clean

# %%
df.to_csv(PROJECT_ROOT / 'data' / 'clean' / 'clean_data.csv', index=False)
