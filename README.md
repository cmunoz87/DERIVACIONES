# Motor de Tubos y Derivación

App en Streamlit para explicar la lógica de **tubo** y **lugar de proceso** según:
- Hospital (Villarrica / Loncoche / Temuco)
- Examen(es)

## Regla clave
El texto **"gel 1 / gel 2 / gel 3"** es parte del **nombre** del tubo y **NO representa cantidad**.

## Entradas
- Hospital
- Exámenes (multiselección)

## Salidas
- Tubos a tomar (únicos, sin duplicar)
- Tabla detalle por examen: Examen | Tubo | Lugar de proceso

## Configuración de reglas
La matriz está en `app.py` en el diccionario `RULES`.
Valores `NO DEFINIDO` deben reemplazarse por lo indicado en la tabla oficial.

## Ejecutar
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Autor
TM. Camilo Muñoz — Enero 2025
