# Análisis de Actitudes hacia el Aborto

Este proyecto analiza las actitudes de los participantes en una encuesta sobre el aborto, considerando variables sociodemográficas como la escolaridad y la religión.

## 📊 Variables consideradas

- **Escolaridad**: 
  - 1: Primaria
  - 2: Secundaria
  - 3: Técnico
  - 4: Preparatoria
  - 5: Licenciatura
  - 6: Maestría
  - 7: Doctorado

- **Religión**: 
  - 1: Católica
  - 2: Cristiana
  - 3: Testigo de Jehová
  - 4: No tengo

## 📁 Estructura del repositorio

```
📦analisis-actitudes-aborto/
 ┣ 📂data/
 ┃ ┗ 📄Base_de_Likert.csv
 ┣ 📂plots/
 ┃ ┗ actitudes_por_escolaridad.png
 ┃ ┗ actitudes_por_religion.png
 ┣ 📄analisis_actitudes.py
 ┣ 📄requirements.txt
 ┗ 📄README.md
```

## ✅ Requisitos

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

Guarda tus datos en la carpeta `data/` y ejecuta:

```bash
python analisis_actitudes.py
```

Los gráficos se guardarán automáticamente en la carpeta `plots/`.