
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar archivo CSV
df = pd.read_csv("data/Base_de_Likert.csv", encoding="latin-1")

# Calcular promedio de actitudes (columnas que inician con 'R')
actitudes_cols = [col for col in df.columns if col.startswith("R")]
df["Promedio_Actitudes"] = df[actitudes_cols].mean(axis=1)

# Mapear etiquetas legibles
escolaridad_labels = {
    1: "Primaria", 2: "Secundaria", 3: "Técnico", 4: "Preparatoria",
    5: "Licenciatura", 6: "Maestría", 7: "Doctorado"
}
religion_labels = {
    1: "Católica", 2: "Cristiana", 3: "Testigo de Jehová", 4: "No tengo"
}
df["Escolaridad_Label"] = df["Escolaridad"].map(escolaridad_labels)
df["Religión_Label"] = df["Religión"].map(religion_labels)

# Estilo de gráficos
sns.set(style="whitegrid")

# Gráfico: Actitudes promedio por Escolaridad
plt.figure(figsize=(12, 6))
sns.boxplot(x="Escolaridad_Label", y="Promedio_Actitudes", data=df, palette="Set3")
plt.title("Actitudes promedio según Escolaridad")
plt.xlabel("Escolaridad")
plt.ylabel("Promedio de Actitudes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/actitudes_por_escolaridad.png")
plt.show()

# Gráfico: Actitudes promedio por Religión
plt.figure(figsize=(10, 6))
sns.boxplot(x="Religión_Label", y="Promedio_Actitudes", data=df, palette="Set2")
plt.title("Actitudes promedio según Religión")
plt.xlabel("Religión")
plt.ylabel("Promedio de Actitudes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/actitudes_por_religion.png")
plt.show()
