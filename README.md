# Dashboard de Datos Universitarios

**Data Mining — Actividad I: Visualización de Datos y Despliegue de Dashboard**  
Universidad de la Costa | Prof. José Escorcia-Gutierrez, Ph.D.

## Integrantes

- Nicolle Trujillo Albor
- David Calderón
- Lopez Dahl Mariela Catalina
- Juan Esteban Jiménez López
- Jorge Eliecer de la Hoz Epiayu

## Propósito

Dashboard interactivo desarrollado en Streamlit para explorar datos estudiantiles universitarios del 2015 al 2024.  
Cubre indicadores clave como tasa de retención, satisfacción estudiantil e inscripciones por departamento.

## Cómo ejecutar localmente

1. Clonar el repositorio y navegar a la carpeta
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar la app: `streamlit run app.py`

## Funcionalidades del dashboard

- **Filtro** por período académico (Spring / Fall)
- **KPI Cards**: retención promedio, satisfacción promedio, total de inscriptos
- **Gráficos de línea**: tendencias de retención y satisfacción a lo largo del tiempo
- **Gráfico de barras**: comparación de retención entre Spring y Fall
- **Gráfico de torta**: distribución de inscriptos por departamento

## Hallazgos principales

- La tasa de retención creció de **85% en 2015** a **90% en 2024**, reflejando una mejora sostenida.
- La satisfacción estudiantil aumentó de **78% a 88%** en el mismo período.
- **Ingeniería** es el departamento con mayor número de inscriptos; **Ciencias** muestra una leve caída en los últimos años.
- Los períodos Spring y Fall presentan valores casi idénticos en todas las métricas.

**Insight accionable:** La caída en inscripciones de Ciencias sugiere que la universidad debería revisar su oferta académica y las perspectivas laborales de ese departamento para atraer y retener más estudiantes.
