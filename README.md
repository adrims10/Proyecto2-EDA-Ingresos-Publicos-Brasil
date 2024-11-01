Proyecto: Análisis de la Ejecución de Ingresos Públicos en Brasil

Bienvenidos!

Es un placer recibirlos

En qué consiste:
¡Bienvenidos a un nuevo proyecto! Esta vez, vamos a realizar un análisis de la ejecución de ingresos públicos en Brasil, examinando los datos históricos entre 2013 y 2021. Nuestro objetivo es identificar patrones, detectar áreas problemáticas y proponer recomendaciones para mejorar la precisión de las previsiones y la eficiencia de la recaudación.

Objetivos del Proyecto:
Limpieza de datos: Resolver problemas comunes como valores nulos, formatos inconsistentes y duplicados.

Unión de conjuntos de datos: Combinar todos los archivos en un solo dataframe para un análisis global.

Análisis Exploratorio de Datos (EDA): Examinar la relación entre diferentes variables clave y explorar categorías relevantes para identificar patrones o discrepancias significativas.

Visualización de datos: Generar gráficos que permitan identificar tendencias y patrones relevantes en los datos analizados.

Estructura del Proyecto:
Hemos creado un entorno llamado AnalisisIngresosPublicos para el siguiente proyecto.

├── notebooks/           # Notebooks de Jupyter para limpieza de datos y visualización
├── src/                 # Scripts de procesamiento y modelado
├── Datos/               # Datos, donde estarán los archivos CSV obtenidos
├── README.md            # Descripción del proyecto
├── README_English.md    # Descripción del proyecto en inglés
Instalación y Requisitos
Este proyecto usa Python 3.12.6.

Se ha importado la librería BeautifulSoup

Se ha importado la librería requests

Se ha importado la librería pandas

Se ha importado la librería numpy

Se ha importado la librería webdriver

Se ha importado la librería ChromeDriverManager

Se ha importado la librería Keys

Se ha importado la librería Select

Se ha importado la librería WebDriverWait

Se ha importado la librería expected_conditions as EC

Se ha importado la librería NoSuchElementException

Se ha importado la librería re

Se ha importado la librería sys

Se ha importado la librería os

Instrucciones Detalladas
Fase 1: Unión de Conjuntos de Datos
Lectura y Exploración Inicial:
Cargar los diferentes archivos CSV en dataframes individuales.

Explorar la estructura de cada archivo para asegurarse de que las columnas sean consistentes y tengan un formato homogéneo.

Estandarización y Limpieza:
Estandarizar nombres de columnas si es necesario.

Asegurar que los tipos de datos (fechas, valores monetarios) sean consistentes en todos los archivos.

Tratar los valores nulos y eliminar filas o columnas irrelevantes.

Unión de los Dataframes:
Unir los dataframes de todos los archivos para crear un solo dataframe consolidado.

Verificar la existencia de duplicados y corregir cualquier inconsistencia en los datos.

Fase 2: Limpieza de Datos
Tratamiento de Valores Nulos:
Identificar y manejar los valores nulos: decidir si se deben rellenar, eliminar o imputar según el contexto.

Corrección de Formatos:
Convertir valores monetarios a formato numérico, eliminando símbolos y asegurando que todas las cifras sean comparables.

Asegurarse de que las fechas estén en un formato uniforme y puedan ser fácilmente manipuladas para análisis temporal.

Detección y Corrección de Errores en Categorizaciones:
Revisar posibles inconsistencias en las categorías económicas (errores tipográficos, variaciones en los nombres) y unificarlas.

Resultados y Conclusiones
Observamos que las desviaciones entre lo previsto y lo recaudado son más pronunciadas en ciertas categorías económicas.

La recaudación ha mostrado patrones temporales específicos, con mayores discrepancias en ciertos meses del año.

Los órganos y unidades gestoras muestran variaciones en términos de eficiencia en alcanzar las metas de recaudación.

Próximos Pasos
Implementar paralelización y asincronía en la recolección de datos para mejorar la eficiencia.

Añadir funciones de soporte para la visualización de gráficos, no estando estas directamente en el Notebook.

Limpiar y analizar los datos de marca-volumen para un análisis más detallado por formato de producto.