# AGENTS.md — Fundamentos de la Ciencia de Datos (UNICEN)

Repo de cursada universitaria, **no es un proyecto de software**. El objetivo es aprender la
materia y rendirla. Todo lo que se escriba acá va a ser evaluado por docentes, no por una
plataforma: priorizá que el razonamiento sea correcto y esté explícito sobre supuestos.

## Estructura

- `docs/Material/` — PDFs de las 8 clases de teoría. **Fuente de verdad de la syllabus.**
  Solo lectura: no editar ni renombrar (los nombres son inconsistentes y hay links de cátedra).
- `docs/Tps/` — **PDFs con las consignas de los Prácticos 1–7.** Es el enunciado de cada TP:
  antes de escribir código, leer el PDF del práctico. Solo lectura.
- `docs/Clases practicas/` — slides de las clases prácticas (Python, acceso a datos, análisis
  preliminar). Contienen los Colab de referencia (`ciencia-datos-unicen-practica-N-python.ipynb`).
- `Tp1/` — scripts planos (`EjercicioN.py`). El Práctico 1 pide 10 ejercicios y hay 5 resueltos
  (faltan 6–10: diccionario con promedio, Fibonacci, palíndromo, clase `Rectángulo` y `Cuadrado`
  que hereda de ella).
- `Tp2/` — notebooks (`EjercicioN.ipynb`) + los pocos datasets ya bajados.

Los TP van a migrar de `TpN/` a `docs/Tps/` con su propio `docs/Tps/venv*` cuando se organicen;
hasta entonces los TP viejos quedan en `TpN/` y los nuevos también.

## Comandos

No hay build, test, lint, typecheck, CI, `requirements.txt` ni `package.json`. No inventar
comandos de ese tipo ni dejar de ejecutarlos "por costumbre". La verificación es **ejecutar**:

```bash
source Tp2/venvTp2/bin/activate   # venv local por TP, ver "Entorno"
jupyter lab                       # o: jupyter notebook
```

Para leer un PDF de clase o de TP (los nombres exactos están más abajo):

```bash
pdftotext -layout "docs/Material/Clase_4.pdf" -
```

## Prácticos: qué hay que hacer y con qué datos

`docs/Tps/` contiene un PDF por práctico. Leer el PDF **antes** de tocar el repo.

| Práctico | Tema | Se entrega | Datos | Requiere |
|---|---|---|---|---|
| 1 | Ejercicios básicos de Python (10) | no | — | — |
| 2 | Acceso a datos: leer CSV/XLSX, `describe()`, análisis exploratorio | no | `ObesityDataSet_raw_and_data_sinthetic`, `netflix_titles`, `catalogo_streaming_argentina_2024.xlsx` | `wget`, `pandas`, `openpyxl` |
| 3 | Perfilado, hipótesis bivariadas, correlación y scatter | no | los 3 del P2 | **`ydata-profiling`** (es la librería que da `ProfileReport`), `matplotlib` |
| 4 | Nulos, encoding de `GENRE`, hipótesis de recaudaciones y duración | **sí** | `movies.csv`, `food.zip` | `zipfile` (stdlib), preprocesamiento de texto |
| 5 | Visualización: qué gráfico para cada pregunta | **sí** | `ObesityDataSet_raw...`, `netflix_titles`, `food` | **`matplotlib`/`seaborn`** |
| 6 | Tests de hipótesis: elegir test y validar supuestos | **sí** | `Life Expectancy Data.csv`, `Life-Expectancy-Data-Updated.csv`, health & sleep statistics (Kaggle) | **`scipy.stats`, `scikit-learn`, `matplotlib`** |
| 7 | PCA, biplot, t-SNE, UMAP | **sí** | `ObesityDataSet_raw...`, `datospractico6csdatos.xlsx` (pestañas Proteins / Classic Wines / Arroyos) | **`scikit-learn`, `scipy`, `umap-learn`**, `openpyxl` (multi-hoja) |

Los prácticos son **acumulativos**: el P3 extiende el P2, el P5 reutiliza los datos del P2/P3/P4
y el P7 vuelve sobre `ObesityDataSet_raw_and_data_sinthetic`. Respetar los nombres de columnas y
el preprocesamiento del previo en vez de empezar de cero.

**Cada PDF termina con "preguntas tipo parcial ... con papel y lápiz"** (en el P2, P4, P5, P6 y
P7). No son código: son el formato real del examen. Contestarlas implica justificar con
supuestos explícitos (normalidad, homocedasticidad, mecanismo del faltante, representatividad de
la muestra), no sacar un número.

## Entrega y TPE

Del PDF `docs/Clases practicas/Clase Práctica 1 - 2026 - ...pdf`, textual y en mayúsculas:

> NO ENTREGUEN EL TRABAJO ESPECIAL EN COLAB!!! Lo tienen que hacer usando Jupyter Notebooks, y
> entregarlo como repositorio en Github

- El TPE va en **Jupyter Notebooks** (locales), entregado como **repositorio de Github público**.
- El repo del TPE tiene que tener **`.gitignore` de Python** (venv no versionado) y Jupyter
  instalado dentro del venv. Este repo ya cumple la parte del `.gitignore`.
- La cátedra recomienda **Linux o macOS**. Google Colab es solo para los ejemplos de clase.
- Los TP de los prácticos van en Colab o local, a elección (salvo el TPE, que no).

Nota de la misma clase práctica, útil para decidir si guardar outputs: con notebooks "es un bardo
con Git (cada vez que hay una salida nueva, cambia el archivo)".

## Material de clase (índice)

Los nombres de archivo NO son consistentes; usar el path exacto:

| Clase | Tema | Archivo en `docs/Material/` |
|---|---|---|
| 1 | Intro a Ciencia de Datos, roles, calidad de datos, ingeniería de datos | `Clase 1 - Introducción a la ciencia de datos.pptx (1).pdf` |
| 2 | EDA, transformación (encoding, discretización, escalado), datos faltantes | `Clase 2 - Analisis, limpieza y exploración de datos.pdf` |
| 3 | EDA II: medidas de posición/dispersión, asimetría, kurtosis, covarianza/correlación, chi-cuadrado | `Clase 3 - Acceso y análisis de datos (continuacion).pptx.pdf` |
| 4 | Visualización: tipos de gráficos, data-ink ratio, escalas, color, chartjunk | `Clase_4.pdf` |
| 5 | Tests paramétricos y no paramétricos, ANOVA, validación de supuestos | `Clase 5 -Test paramétricos y no paramétricos.pdf` |
| 6 | Multivariado: descomposición espectral, PCA, biplot | `Clase 6 - Análisis Multivariado y Reducción de dimensionalidad (Parte I).pptx.pdf` |
| 7 | Reducción no lineal: t-SNE, UMAP | `Clase 7 - Análisis Multivariado y Reducción de dimensionalidad (Parte II).pptx.pdf` |
| 8 | Clustering: k-means, jerárquico aglomerativo, índices de validación | `Clase 8 - Clustering.pptx.pdf` |

**Limitación de `pdftotext`**: los slides son casi todos imágenes. El texto extraído sale, pero
las **fórmulas, gráficos y diagramas salen en blanco**. Para leer una fórmula hay que abrir el PDF
como imagen. No confiar en el texto extraído como si fuera completo.

## Entorno

- Cada TP tiene su **venv propio y local**, con el nombre `venvTpN`.
- `.gitignore` contiene **solo** `Tp2/venvTp2`. Un venv con otro nombre aparece en `git status`
  como untracked gigante → agregarlo al `.gitignore` al crearlo.
- Los `.ipynb` guardan `kernelspec.display_name = "venvTp2 (3.12.3)"` con `name: "python3"`.
  El binding es por `name`, así que un kernel distinto puede ejecutarse en silencio sin que se note.
  Si se cambia el venv, actualizar el `kernelspec` del notebook.
- Instalado en el venv de Tp2: pandas 3.0.5, numpy 2.5.2, `matplotlib-inline`, `wget`.
  **No están** `matplotlib`, `scipy`, `scikit-learn`, `seaborn`, `statsmodels`, `openpyxl`,
  `umap-learn` — instalarlos si hacen falta y dejarlos anotados (no hay `requirements.txt` donde
  registrarlos). Ojo: `matplotlib-inline` no es `matplotlib`; sin él no hay `plt`.
- Consecuencia concreta: la última celda de `Tp2/Ejercicio2.ipynb` (`to_excel`) **falla** con este
  venv por falta de `openpyxl`. No es un error del TP.

## Datasets — trampas reales

**Ningún dataset de los TP está en el repo**: se bajan en runtime con `wget.download(...)` y caen
en el **directorio de trabajo** con paths relativos. Hay dos hosts distintos:

- `https://ignaciorlando.github.io/datasets/data-science/` — espejo del JTP (J. Ignacio Orlando),
  sirve los datasets de los TP 2, 3, 4, 5, 6 y 7.
- `https://raw.githubusercontent.com/ignaciorlando/duia-ml-datasets/master/LifeExpectancyWHO/`
  — repo distinto, solo para `Life Expectancy Data.csv` del P6. **El nombre del archivo tiene
  espacio** → hay que URL-encodearlo (`%20`) o el request falla.
- `Health and sleep statistics` (P6) está en **Kaggle** con login: no se puede bajar por `wget`,
  hay que bajarlo a mano o usar la API de Kaggle.

Trampas sobre los archivos:

- Archivos que **parecen datos pero son la ficha en español** del dataset (23–43 líneas, con CRLF):
  `ObesityDataSet.csv`, `ObesityDataSet_raw_and_data_sinthetic.txt`, `netflix_titles.txt`.
  `pd.read_csv` sobre ellos no da el dataset; lo que se lee con `open()` sí es útil (es lo que
  pide el punto ii del P2).
- El CSV real de obesidad (`ObesityDataSet_raw_and_data_sinthetic.csv`) **no está en el repo**: se
  descarga al correr el notebook. El `.txt` que sí está no lo reemplaza.
- `netflix_titles.csv`: el enunciado del P2 avisa que con la config por defecto de
  `pd.read_csv()` falla la decodificación UTF-8 y que hay que usar `encoding="latin1"`.
  Con ese encoding da **8809 filas × 26 columnas**, de las cuales las últimas 14 aparecen como
  `Unnamed: 12`…`Unnamed: 25` y están vacías por comas finales → dropear explícitamente
  (`usecols=` o `dropna(axis=1, how="all")`, que deja 12 columnas).
  Ojo: con pandas 3.0.5 el error UTF-8 **no se reproduce** (lee bien sin `latin1`), pero ponerlo
  igual, porque es lo que el TP pide mostrar y es lo que da el resultado que documenta el enunciado.
- `datospractico6csdatos.xlsx` (P7) es **multi-hoja** → `read_excel(..., sheet_name=...)` para
  `Proteins`, `Classic Wines` y `Arroyos Fco-Qcas`.

## Notebooks

- `nbformat 4.5`: cada celda tiene `id` explícito. **No regenerar el .ipynb desde cero** (se
  pierden los ids y el diff queda ilegible) — editar el JSON preservando `id` y metadata.
- Patrón de celdas: una celda `markdown` con el título/sección del enunciado, después las celdas
  `code`. Comentarios en español explicando el porqué, no el qué.
- Los `.ipynb` del working tree están guardados **con outputs y `execution_count`** (7 de 9
  celdas de código en Ejercicio1, 2 de 3 en Ejercicio2). El formato de entrega formal todavía no
  está publicado (se define en el TPE, que es más adelante); no asumir que hay que limpiarlos ni
  que hay que guardarlos ejecutados hasta que esté especificado.
- `Tp2/Ejercicio2.ipynb` termina con `raw_dataset.to_excel("netflix_titles.xlsx")`: ese `.xlsx`
  es un artefacto generado, no versionar.

## Convenciones

- **Todo en español**: comentarios, nombres de variables, nombres de archivo, texto de los celdas.
  Los datasets y la terminología de las clases van en español/inglés según el original.
- Nombres de archivo de TP: `EjercicioN.ipynb` / `EjercicioN.py`, `N` correlativo.
- Separadores decimales con coma en el texto; en los DataFrames usar el locale que pida el
  enunciado (`pd.read_csv(..., decimal=",")` es común en los datasets de la cátedra).
- En estadística, **justificar siempre el test elegido**: tipo de variables, supuestos verificados
  (normalidad, homocedasticidad), y qué test se descarta si fallan. La cátedra lo trata como
  error metodológico grave, no como detalle.

## Estado del repo (al 06/10/2026)

Casi nada está commiteado. Solo hay 2 commits:

- tracked: `Tp1/Ejercicio1..5.py` y `Tp2/Ejercicio1.py` (**borrado** en el working tree, reemplazo
  por `Tp2/Ejercicio1.ipynb` — la eliminación sigue sin commitear).
- untracked: todo `docs/` (26 MB de PDFs), los `.ipynb`, los datasets, el `.gitignore` y este
  `AGENTS.md`.

No commitear salvo pedido explícito, y no agregar los PDFs de `docs/` al repo sin confirmarlo
antes (peso: 19 MB en `Material/`, 5,4 MB en `Clases practicas/`).

## Datos de la materia

- Cátedra: Prof. Dra. Daniela Godoy (responsable). Práctica a cargo del JTP Dr. J. Ignacio Orlando.
- Cursada: martes 14–17 hs (2 h teoría + 1 h Práctica Especial) y jueves 14–17 hs (práctica).
- Aprobación: **Examen parcial (con dos recuperatorios) + Trabajo Práctico Especial (TPE)**;
  se necesitan ambos. Promoción con **7 o más** en el parcial/recuperatorio de primera instancia
  **y** en el TPE.
- Aula Moodle: `https://moodle.exa.unicen.edu.ar/course/view.php?id=1134&section=0`
  (no se puede acceder desde acá). Las consignas de los TP **sí** están en `docs/Tps/`; lo que
  no está son las fechas de entrega ni el formato de entrega formal.