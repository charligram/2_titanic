# 🧪 Proyecto predicciones sobrevivientes del Titanic
## ❓ Planteamiento del proyecto
En los datos de los sobrevivientes del Titanic existen ciertas características claves que aumentan o disminuyen las probabilidades de que el pasajero sobreviva al lamentable evento. La idea principal de este proyecto es lograr predecir si un pasajero sobrevive a partir de sus datos.

## ℹ️ Dataset
Recurso: Kaggle

Link: https://www.kaggle.com/competitions/titanic

Registros: 891

## 🎯 Objectives
- Identificar características más influyentes
- Generar modelo de ML predictor de sobrevivientes

## 🧹 data cleaning
- Completar valores faltantes en la edad (Age) con la mediana de los registros
- Eliminar columna de la cabina (Cabin) debido a su pobre cantidad de registros no nulos
- Completar datos faltantes en el lugar de embarcación del pasajero (Embarked) con el valor que mas se repita (moda)
- Completar valores faltantes en el las tarifas (Fare) con la mediana de los registros

## 🔎 EDA
Los gráficos que se muestran a continuación se tratan de los principales hallazgos y consideraciónes más importantes, el resto de visualizaciones se pueden encontrar en la carpeta outputs/figures/

### General survival rate
A modo general, dentro de la tragedia del titanic, los pasajeros sobrevivieron en un 38.38%

![survival_rate](outputs/figures/01_survival_rate.png)

### Pclass
La tasa de supervivencia disminuty progresivamente entre primera, segunda y tercera clase.

![pclass_survival_rate](outputs/figures/03_survival_rate_by_pclass.png)

### Sex
La mayoría de las personas abordo del crucero eran hombres. Además los hombres también tiene una tasa de sobrevivencia bastante baja en comparación a las mujeres.

![count_sex](outputs/figures/04_count_sex.png)

![sex_survival_rate](outputs/figures/05_survival_rate_by_sex.png)

### Age
Los pasajeros a modo general tenian entre unos 15 a 40 años, en cuanto a distribución respecta, en el grupo de sobrevivientes como no sobrevivientes es más común encontrar personas en esas edades, aunque se vuelve más común encontrar personas jóvenes (-10 años) en el grupo de sobrevivientes. Dicho esto, se puede aprecia en el segundo gráfico que las personas entre 0-10 años son las que más probabilidades tienen de sobrevivir.

![age_distribution_groups](outputs/figures/06_01_age_distribution_in_survived_no_survived_groups.png)

![age_survival_rate](outputs/figures/07_probability_of_survive_by_age_groups.png)

### SibSp
Aparentemente las personas que estaban con 1 hermano/a o esposo/a tenian las posibilidades más altas de sobrevivir, estas posibilidades decrecen con cada vez más acompañantes de este tipo.

![probability_survive_sibsp](outputs/figures/08_probability_of_survive_by_sibsp.png)

### Parch
En cuanto a padres o hijos, los pasajeros que más sobrevivieron tenian entre 1 a 3 acompañantes de este tipo.

![probability_survive_parch](outputs/figures/09_probability_of_survive_by_parch.png)

### Fare
La tarifa del ticket de la embarcación parece estar completamente concentrada por debajo de los 50. Además, la segunda visualización nos muestra una pequeña tendencia en donde los sobrevivientes tienden a tener Fare más altos, sin marcar una diferencia tan fuerte. (El segundo gráfico tiene aplicada una transformación logaritmica a Fare para ver de mejor manera la diferencias en grupos, las medidas en el eje "y" no son exactamente transferibles al real fare)

![fare_distribution](outputs/figures/10_fare_distribution.png)

![fare_distribution_boxplot](outputs/figures/12_log_fare_dist_boxplot_surv_no_surv.png)

### Embarked
Los pasajeros embarcados en C (Chesbourg) tienen una tasa de supervivencia un poco más alta que los embarcados en Q (Queenstown) y S (Southhampton). Esto puede explicarse debido a que en su mayoría, los embarcados en Chesbourg tienen una Pclass más sofisticada.

![probability_survive_embarked](outputs/figures/13_probability_of_survive_by_embarked.png)

![pclass_by_embarked](outputs/figures/14_pclass_by_embarked.png)


## 👤 Autor
Carlos Rojas