# Roadmap — Análisis del TPE (EPA Fuel Economy 2025)

Guía de trabajo por etapas. Cada etapa tiene un objetivo, qué mirar y qué descartar.

---

## Cómo se reparten las acciones según el enunciado

El enunciado separa **describir** de **arreglar**, y esa separación hay que respetarla:

| Inciso | Qué pide | Qué hacés |
|---|---|---|
| **1** | "...describiendo su comportamiento, distribución de variables, **presencia de outliers, valores nulos** y demás particularidades" | **Diagnosticás.** Mostrás los problemas con evidencia |
| **2** | "**operaciones de limpieza**..., detallando las acciones correctivas y **justificando el por qué de cada una**" | **Arreglás.** Filtrás, quitás centinelas |

**Consecuencia práctica:** en el inciso 1 **no filtrás nada**. Mostrás la base
cruda, con los `10000` a la vista. Esa tabla fea **es la evidencia** que
justifica el filtrado del inciso 2. Si limpiás en el inciso 1, el inciso 2 se
queda sin nada que justificar y la defensa se cae.

El inciso 2 va a citar explícitamente los hallazgos del inciso 1:
*"Como se observó en la sección 1.6, hay 24 valores centinela..."*

---

## Fase 0 — Carga y diagnóstico (sin tocar nada)

En el inciso 1 se carga la base **cruda** y se mira. No se aplica ninguna
corrección todavía.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_excel('25-testcar-2026-01-21.xlsx')

df.shape          # 4287 filas x 67 columnas
df.info()
df.describe()
```

### Qué hay que documentar en el inciso 1

Estas son las **evidencias** que después justifican cada acción del inciso 2:

| Evidencia | Lo que muestra | Corrección que después se justifica |
|---|---|---|
| `df.groupby('Test Fuel Type Description')['RND_ADJ_FE'].mean()` | `10000.0`, `178.9` | quitar centinelas |
| `df['FE_UNIT'].unique()` | `'MPG'` en las 4287 filas | filtrar por combustible |
| `df['Test Fuel Type Description'].value_counts()` | 654 `Electricity` + 10 `Hydrogen 5` | filtrar por combustible |
| `df['Test Category'].value_counts()` | 5 ciclos, no 2 | filtrar por `FTP` |
| `df['Test Veh Displacement (L)'].max()` | `99.999` | quitar centinelas técnicos |
| `df.groupby('Test Vehicle ID').size()` | 953 vehículos para 4287 filas | declarar la unidad de análisis |
| `df.isna().sum()` | nulos desiguales por columna | decidir qué hacer con cada uno |

**Nada de esto se corrige acá.** Se reporta.

> Cuando analices en el inciso 3 y 4, ahí sí trabajás sobre la base ya
> limpia del inciso 2. El filtrado ocurre una vez, en el inciso 2.

### Lo que hay que borrar de la notebook

- La celda de `wget`: descarga 83 KB de HTML porque el link de Drive es la página
  de navegación, no el archivo. El dataset ya está en el repo.
- Tener **una sola** notebook (el enunciado pide una única).

---

## Fase 1 — El censo de variables (NO es opcional)

Antes de decidir qué analizar, hacé un inventario. **Una celda** y te cubre
todas las preguntas de "¿por qué no miraste X?".

Armá una tabla con: variable, tipo, % nulos, nº de valores distintos, decisión
y motivo.

```python
inventario = pd.DataFrame({
    'tipo'     : df.dtypes.astype(str),
    'nulos_%'  : (100 * df.isna().mean()).round(1),
    'distintos': df.nunique(),
})
inventario
```

---

## Fase 2 — Decidir qué descartar, y por qué

### 2.1 Descartar por ser constantes (1 solo valor)

| Variable | Por qué |
|---|---|
| `Model Year` | siempre 2025 |
| `FE_UNIT` | siempre `'MPG'` (y además miente para los eléctricos) |

### 2.2 Descartar por estar casi vacías

| Variable | % nulos | Por qué |
|---|---|---|
| `Averaging Group ID` | 98,4 % | inservible |
| `Averaging Weighting Factor` | 98,4 % | inservible |
| `ADFE Test Number` | 95,1 % | aplica solo a casos derivados |
| `ADFE Total Road Load HP` | 95,1 % | ídem |
| `ADFE Equiv. Test Weight (lbs.)` | 95,1 % | ídem |
| `ADFE N/V Ratio` | 95,1 % | ídem |
| `PM (g/mi)` | 90,9 % | casi siempre vacío **y** con centinelas |
| `FE Bag 4` | 90,9 % | presente solo en FTP |

### 2.3 Descartar por ser identificadores (no son variables de análisis)

Tienen cientos de valores, uno por auto. Sirven para leer nombres, no para agrupar.

`Test Vehicle ID` · `Test Number` · `Represented Test Veh Model` ·
`Represented Test Veh Make` · `Vehicle Manufacturer Name` · `Veh Mfr Code` ·
`Engine Code` · `Actual Tested Testgroup` · `ADFE Test Number`

### 2.4 Descartar por redundantes con `RND_ADJ_FE`

`FE Bag 1`, `FE Bag 2`, `FE Bag 3` tienen correlación **0,90 / 0,91 / 0,91** con
`RND_ADJ_FE`: son la misma medición. Describilas una vez como respaldo y listo.

### 2.5 Describir pero NO analizar: parámetros del dinamómetro

| Grupo | Variables |
|---|---|
| Coeficientes de resistencia | `Target Coef A/B/C`, `Set Coef A/B/C` |
| Ratings de traza | `DT-Inertia Work Ratio Rating`, `DT-Absolute Speed Change Ratg`, `DT-Energy Economy Rating` |

Describen **cómo se simuló el auto en el banco**, no el auto. Además tienen
centinelas (`Set Coef A = 99,999`).

### 2.6 Eje opcional: emisiones

`THC`, `CO`, `CO2`, `NOx`, `CH4`, `N2O` — son del ensayo de emisiones, no del
consumo. Solo si querés abrir un segundo eje de análisis.

---

## Fase 3 — Analizar lo que queda, por grupo

> **Cuándo se hace:** los incisos 3 y 4, sobre la base **ya limpia** del inciso 2.
> En el inciso 1 esta misma caracterización se hace sobre la base cruda, para
> *detectar* los problemas; acá se repite sobre la base corregida para *analizar*.

### Grupo: Características del vehículo y motor ⭐ (el corazón)

Estas son las que pide la hipótesis **4.c**.

| Variable | Cómo analizarla |
|---|---|
| `Equivalent Test Weight (lbs.)` | histograma + `corr` + boxplot por tramo |
| `Rated Horsepower` | histograma + `corr` |
| `Test Veh Displacement (L)` | histograma + `corr` |
| `# of Cylinders and Rotors` | `value_counts` (son 7 valores) |

**Ojo con la redundancia entre ellas:** cilindrada ↔ cilindros r = **0,92**;
potencia ↔ cilindros r = **0,84**. Si entran juntas en la regresión de la 4.c,
tenés multicolinealidad. Decidí y justificá: ¿dejás una y por qué?

### Grupo: Transmisión y tracción ⭐ (hipótesis 4.b)

| Variable | Cómo analizarla |
|---|---|
| `Drive System Description` | `groupby().mean()` + `sns.boxplot` + test |
| `Tested Transmission Type` | `value_counts` (7 tipos) |
| `# of Gears` | `value_counts` (7 valores) |
| `Transmission Overdrive Desc` | `value_counts` (2) |
| `Transmission Lockup?` | `value_counts` (2) |

### Grupo: Combustible (hipótesis 4.a)

| Variable | Cómo analizarla |
|---|---|
| `Test Fuel Type Description` | `value_counts` — define el filtro |

**Ojo:** después de filtrar quedan solo 5 combustibles con datos, y 2 con menos
de 15 filas. Un grupo de 5 autos no sostiene una comparación.

### Grupo: Identificación (solo para leer, no para agrupar)

`Represented Test Veh Make`, `Represented Test Veh Model` — útiles para leer
nombres en tablas, jamás para `groupby`.

### Grupo: Información del ensayo

| Variable | Cómo analizarla |
|---|---|
| `Test Category` | `value_counts` — justifica el filtro a FTP |
| `Test Originator` | `value_counts` — 448 filas ensayadas por la EPA, 3839 por fabricantes |
| `Vehicle Type` | `value_counts` (3 valores) |
| `Test Procedure Description` | `value_counts` |

---

## Fase 4 — La unidad de análisis (NO la saltees)

La clave oficial de la EPA es:

```
Veh Mfr Code + Test Vehicle ID + Test Veh Configuration #
```

Pero en combustión + `FTP` da **1087 combinaciones para 1541 filas**. Sigue
habiendo filas repetidas, que difieren solo en `Aftertreatment Device Desc`.

Tenés que **declarar y justificar** qué usás como observación independiente.
No es un detalle: la cátedra lo pide explícitamente.

---

## Fase 5 — Las hipótesis

| # | Qué | Con qué |
|---|---|---|
| 4.a | ¿la mayoría llega a 25 MPG? | contar + chi-cuadrado |
| 4.b | ¿cambia según tracción? | `groupby().mean()` + `sns.boxplot` + `levene` + `ttest_ind` o `mannwhitneyu` |
| 4.c | ¿todo junto? | regresión con `statsmodels` (ojo con multicolinealidad) |

---

## Checklist antes de seguir

**Inciso 1** (diagnóstico)

- [ ] ¿Analicé la base **cruda**, sin filtrar?
- [ ] ¿Documenté la presencia de centinelas con la evidencia concreta?
- [ ] ¿Documenté el problema de `FE_UNIT` y las 664 filas no--combustión?
- [ ] ¿Documenté que `Test Category` tiene 5 valores?
- [ ] ¿Documenté que las filas no son independientes (953 vehículos)?
- [ ] ¿Inventarié las 67 columnas con su disposición?
- [ ] ¿No apliqué ninguna corrección todavía?

**Inciso 2** (limpieza)

- [ ] ¿Cada acción correctiva **cita** el hallazgo del inciso 1 que la justifica?
- [ ] ¿Expliqué por qué filtrar y no imputar/transformar?
- [ ] ¿Declaré qué pierdo con cada decisión?
- [ ] ¿Mostré el antes y el después?

**Transversal**

- [ ] ¿Declaré la unidad de análisis?
- [ ] ¿Justifiqué cada variable que descarté?
- [ ] ¿Usé solo funciones de la cátedra?
- [ ] ¿La notebook corre entera sin intervention manual?