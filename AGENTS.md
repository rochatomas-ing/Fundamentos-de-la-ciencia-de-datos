# AGENTS.md — Fundamentos de la Ciencia de Datos (UNICEN)

Repo de cursada universitaria, **no es un proyecto de software**. El objetivo es aprender la
materia y rendirla. Todo lo que se escriba acá va a ser evaluado por docentes, no por una
plataforma: priorizá que el razonamiento sea correcto y esté explícito sobre supuestos.

## Cómo trabajamos — leer esto primero

**El trabajo lo hacen el estudiante y sus compañeros. Yo reviso, corrijo y aviso.**

Esto no es un proyecto de software con un cliente. Es un trabajo académico con defensa oral y nota
individual. El reparto de roles es explícito:

| | Quién | Qué hace |
|---|---|---|
| **Autoría** | El estudiante + su grupo | Escribe el código, elige las hipótesis, redacta el informe, decide los argumentos. **Nada de esto lo hago yo.** |
| **Revisión** | Yo | Leo lo que escribieron, detecto errores, problemas metodológicos y supuestos no declarados, y explico **por qué** están mal. |
| **Corrección** | El estudiante | Implementa los cambios. Yo no edito sus archivos salvo que me lo pida explícitamente. |

Reglas concretas que se derivan de esto:

- **No escribir la notebook, el informe ni los entregables.** Aunque se pueda, aunque "quede más
  prolijo", aunque el enunciado lo pida literalmente. Un trabajo que no puede defenderse en una
  defensa oral grupal e individual es peor que uno con errores discutibles.
- **Revisar por defecto, editar por pedido.** Ante una celda sospechosa, decir qué está mal y por
  qué. No abrir el archivo y corregirlo en silencio: si lo arreglo yo, no lo aprende, y en la
  defensa no va a poder responder.
- **Priorizar el razonamiento.** El valor está en el *porqué*: qué test corresponde, qué supuesto
  se está asumiendo, qué decisión de limpieza se tomó y qué se pierde con ella. Un número sin
  justificación vale cero en esta materia.
- **Señalar los supuestos no declarados.** Muchas veces el error no es de código sino de
  lógica: omitir que las observaciones no son independientes, no declarar qué se hace con los
  nulos, no justificar por qué se descarta una variable. Eso es lo que más cuesta en la corrección.
- **Idioma: español**, siempre, en los mensajes y en las explicaciones.

Lo que sí hago sin que me lo pidan: preparar el entorno, leer los enunciados, verificar que las
librerías estén, señalar las trampas de los datos antes de que el grupo las descubra destruyendo
un análisis, y contrastar lo que hacen contra lo que dice la teoría de las clases.

## Prioridad

**El TPE es lo único que importa.** Los Prácticos 1–7 no se entregan, no tienen fecha y el
estudiante decidió explícitamente no hacerlos. `Tp1/` y `Tp2/` quedan como material histórico:
no completarlos, no arreglarlos, no proponer mejoras. Solo consultar si algo es necesario para
entender un patrón.

Cuando haya que elegir a qué dedicar el tiempo: **TPE > parcial > todo lo demás**.

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
- `Tp2/` — notebooks (`EjercicioN.ipynb`) + los pocos datasets ya bajados. **Histórico.**
- `Tp Especial/` — **el trabajo que importa.** Enunciado en PDF, venv propio (`venvTPE/`),
  `requirements.txt` y la notebook del TPE. Ver la sección "TPE".

Los TP van a migrar de `TpN/` a `docs/Tps/` con su propio `docs/Tps/venv*` cuando se organicen;
hasta entonces los TP viejos quedan en `TpN/` y los nuevos también.

## Comandos

No hay build, test, lint, typecheck ni CI. Tampoco `package.json`. No inventar comandos de ese tipo
ni dejar de ejecutarlos "por costumbre".

La verificación es **ejecutar**, en el venv que corresponda:

```bash
# TPE (lo que importa)
source "Tp Especial/venvTPE/bin/activate"
cd "Tp Especial" && jupyter lab
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

## TPE — Práctico Especial (lo prioritario)

Enunciado: `Tp Especial/Enunciado TPE Ciencia de Datos 2026 - EPA Fuel Economy.pdf` (3 páginas).
Dataset: **EPA Fuel Economy — Model Year 2025**. Ayuda asignada: **Santiago Vitale**.
Grupo de máx. 3, registrado por Moodle.

### Qué pide el enunciado

1. **EDA**, *investigando con recursos online el (posible) origen de los datos*, caracterizando
   atributos, distribuciones, outliers y nulos.
2. **Limpieza** "si fuera necesario", detallando y **justificando** cada acción correctiva.
3. **3 hipótesis** justificadas con conocimiento del dominio: una univariada, una bivariada, una
   multivariada.
4. **Validación** de esas 3 **más las 3 que impone la cátedra**:
   - a) la mayoría de las configuraciones de combustión alcanzan ≥25 MPG urbano
   - b) en combustión, la eficiencia difiere según el sistema de tracción
   - c) en combustión, peso/potencia/cilindrada/cilindros/transmisión/tracción se asocian
     **conjuntamente** con la eficiencia urbana

### Entregables

Una **única** notebook Jupyter por secciones + informe + `requirements.txt` + `README.md` con
instrucciones de ejecución + **el archivo de datos en el repo**.

Lo que la cátedra deja explícito y conviene no discutir con ella:

- *"El código debe ser 100% ejecutable"* → la notebook tiene que correr sola, sin pasos manuales.
- *"Esas secciones deben referenciarse explícitamente en el informe, dado que se utilizarán como
  guía para realizar preguntas específicas sobre el código durante la evaluación oral"* → la
  **defensa oral es por secciones de la notebook**, no un "explicad qué hicieron". Con 2 o 3
  personas, cada sección tiene que poder defenderse de forma independiente.
- *"No entregar notebooks con experimentos descartados ni pruebas no realizadas... limpia, sin
  comentarios o borradores"* → contradice el dicho de la clase sobre que con notebooks "es un
  bardo con Git". Para el TPE manda el enunciado. Decidir con el grupo si se versiona con outputs.
- Nota **individual** en la defensa grupal → cada uno tiene que poder responder por todo.

### Fechas (cursada 2026)

| Hito | Fecha |
|---|---|
| Entrega | **martes 10 de noviembre, 23:59 hs** |
| Devolución inicial | martes 17 de noviembre |
| Defensa oral | semana del 23 al 27 de noviembre, a coordinar |
| Consulta | todas las clases prácticas + **jueves 3 de noviembre** (exclusiva parcial y TPE) |

Cronograma de la cátedra: 1 EDA + hipótesis uni/bi; 2 apertura y limpieza; 3 primeras cuatro
pruebas; 4 informe + probar GitHub; 5 hipótesis multivariada; 6 informe final.

### Sin resolver

- **El link del dataset.** El enunciado **no lo incluye**. El estudiante tiene uno; hasta
  confirmarlo, todo lo de la sección "Datasets" sobre el TPE es sobre el archivo oficial de la
  EPA y puede no coincidir.
- **El template del informe** está en el Moodle y no se pudo bajar. La estructura del informe
  depende de eso.

## Entrega: notas de la clase práctica

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

- Cada trabajo tiene su **venv propio y local**: `Tp Especial/venvTPE`.
- `.gitignore` tiene `Tp2/venvTp2` y `Tp Especial/venvTPE`. **Un venv con otro nombre aparece en
  `git status` como un untracked gigante** → agregarlo al `.gitignore` al crearlo.
- Los `.ipynb` guardan `kernelspec.display_name` con `name: "python3"`. El binding es por `name`,
  así que un kernel distinto puede ejecutarse en silencio sin que se note. Si se cambia el venv,
  actualizar el `kernelspec` del notebook. Para el TPE el kernel registrado es `venvTPE (Python 3.12)`.

### Trampa del sistema (ya resuelta, no volver a tropezar)

El `python3` del sistema es el 3.12.3 de Ubuntu **sin `pip` ni `ensurepip`** (falta el paquete
`python3-venv`), y `sudo` pide contraseña. Crear un venv normal falla. La receta que funciona:

```bash
python3 -m venv --without-pip "Tp Especial/venvTPE"
curl -sS -o /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py
./venvTPE/bin/python /tmp/get-pip.py     # instala pip DENTRO del venv, sin tocar el sistema
```

### Estado real de `Tp Especial/venvTPE` (creado el 15/10/2026)

pandas 3.0.6 · numpy 2.5.4 · scipy 1.18.1 · scikit-learn 1.9.1 · statsmodels 0.15.0 ·
matplotlib 3.11.2 · seaborn 0.13.2 · openpyxl 3.1.5 · jupyterlab 4.6.4 · ipykernel 7.4.0 · wget 3.2

`Tp2/venvTp2` **no existe** en esta máquina (esta sección antes afirmaba lo contrario).

- `openpyxl` es obligatorio para el TPE: el dataset de la EPA es `.xlsx` y sin eso `read_excel`
  falla.
- **pandas 3.0** es más nuevo que los Colab de clase. Cambió el comportamiento por defecto:
  Copy-on-Write (la asignación encadenada falla en silencio en vez de avisar) y dtype `str` en vez
  de `object` para texto (29 de 67 columnas del dataset EPA). El código de los notebooks de clase
  funciona, pero no copiarlo a ciegas.

## Datasets — trampas reales

### TPE: EPA Fuel Economy Model Year 2025

Analizado el archivo oficial (`25-testcar-2026-01-21.xlsx`, EPA). **4287 filas × 67 columnas**,
`Model Year` = 2025 en todas. Columnas clave: `RND_ADJ_FE` (MPG), `Test Category`,
`Test Fuel Type Description`, `Drive System Description`, `Equivalent Test Weight (lbs.)`,
`Rated Horsepower`, `Test Veh Displacement (L)`, `# of Cylinders and Rotors`,
`Tested Transmission Type`, `Test Vehicle ID`.

**Link del dataset RESUELTO (15/10/2026)**: el estudiante pasó
`https://drive.google.com/file/d/1SrWg-tvyGMxnR0KNi46dlA2KIq6kku6F/view`. El archivo de Drive es
**byte a byte idéntico** (MD5 `19f02966b1ce2d95227a815af61366cf`) al `25-testcar-2026-01-21.xlsx`
oficial de la EPA. Descargado a `Tp Especial/25-testcar-2026-01-21.xlsx`. Se conserva el nombre
original a propósito: el inciso 1 pide *investigar el origen de los datos*, y el nombre del archivo
de la EPA es parte de la evidencia de ese origen.

**Cómo descargarlo de Drive** (el endpoint clásico `drive.google.com/uc?export=download` devuelve
HTTP 500 con archivos grandes; el que funciona es `drive.usercontent.google.com`):

```bash
curl -L "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t" -o salida.xlsx
```

Cinco trampas confirmadas, en orden de gravedad:

1. **Las filas NO son independientes.** 4287 filas pero solo **953 `Test Vehicle ID` únicos**
   (2, 4, 6… hasta 45 filas por vehículo): son configuraciones y ciclos de prueba del mismo auto.
   En combustión+`FTP` son 1547 filas contra **732 vehículos** (≈2,1 filas/vehículo). Correr un
   t-test como si fueran observaciones independientes infla la significación. **La unidad de
   análisis hay que declararla y justificarla.**
2. **`RND_ADJ_FE` tiene centinelas que NO son nulos.** Valores `10000.0` y `4595.3` en 6 filas de
   combustión+`FTP`; el marcador de la EPA es **999**, visible explícito en `FE Bag 1/2/3` del
   Toyota RC F. `dropna()` no los toca. Efecto al limpiarlos: el desvío pasa de **532,30** a
   **10,66** (50×) y la media de 60,65 a 28,96. Mejor ejemplo posible para el punto 2 del
   enunciado ("justificar por qué cada acción correctiva").
3. **Los eléctricos declaran `FE_UNIT = 'MPG'`** en las 4287 filas, sin excepción, pero es MPGe.
   Además su FE va de 0 a 999. Filtrar por `Test Fuel Type Description` es obligatorio: 664 filas
   no son de combustión (654 `Electricity` + 10 `Hydrogen 5`).
4. **`Test Category` tiene 5 valores, no 2**: `FTP` (1577, urbano), `HWY` (1340, carretera), `CD`,
   `US06` y `SC03` (ciclos agresivos). "Urbano" = `FTP`; descartar los otros tres hay que
   justificarlo.
5. **Nulos reales**: `RND_ADJ_FE` 221 vacíos, `# of Cylinders and Rotors` 670 (664 son los
   eléctricos, quedan 6 en combustión). Peso, potencia y cilindrada no tienen ninguno.
   `Averaging Group ID` y `Averaging Weighting Factor` están casi vacíos (4212/4287): no usarlos.

Dato de referencia para la hipótesis (a): en combustión+`FTP` ya limpios, **902 de 1541 = 58,5 %**
llegan a ≥25 MPG. La hipótesis de la cátedra se confirma, pero falta el test y falta resolver la
unidad de análisis.

### TP 2–7 (históricos)

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

## Estado del repo (al 15/10/2026)

Casi nada está commiteado. Solo hay 2 commits:

- tracked: `Tp1/Ejercicio1..5.py` y `Tp2/Ejercicio1.py` (**borrado** en el working tree, reemplazo
  por `Tp2/Ejercicio1.ipynb` — la eliminación sigue sin commitear).
- untracked: todo `docs/` (~30 MB, PDFs y Colabs de clase), los `.ipynb`, los datasets,
  `.gitignore`, `Tp Especial/` y este `AGENTS.md`.

No commitear salvo pedido explícito, y no agregar los PDFs de `docs/` al repo sin confirmarlo antes.

**El TPE va a su propio repositorio de GitHub público**, no a este. Cuando estén, decidir con el
grupo si `Tp Especial/` se independiza (`git init` propio) o si se saca de acá.

## Datos de la materia

- Cátedra: Prof. Dra. Daniela Godoy (responsable). Práctica a cargo del JTP Dr. J. Ignacio Orlando.
  El TPE tiene un ayudante asignado aparte: **Santiago Vitale**.
- Cursada: martes 14–17 hs (2 h teoría + 1 h Práctica Especial) y jueves 14–17 hs (práctica).
- Aprobación: **Examen parcial (con dos recuperatorios) + Trabajo Práctico Especial (TPE)**;
  se necesitan ambos. Promoción con **7 o más** en el parcial/recuperatorio de primera instancia
  **y** en el TPE.
- Aula Moodle: `https://moodle.exa.unicen.edu.ar/course/view.php?id=1134&section=0`
  (no se puede acceder desde acá). Las consignas de los TP **sí** están en `docs/Tps/`; las del
  TPE están en `Tp Especial/`. Lo que no está accesible es el **template del informe** ni el
  link del dataset del TPE.