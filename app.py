  import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Motor de Tubos y Derivación",
    layout="centered"
)

# ---------- LOGO (mismo estilo que el anterior) ----------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", width=220)

st.markdown("## Motor de Tubos y Derivación")
st.caption(
    "Herramienta explicativa para desarrolladores: "
    "define tubo y lugar de proceso según Hospital + Examen."
)

st.divider()

# ---------- CATÁLOGOS ----------
HOSPITALES = ["Villarrica", "Loncoche", "Temuco"]

EXAMENES = [
    "Glucosa",
    "GGT",
    "Troponina",
    "Progesterona",
    "LH",
]

# ---------- MATRIZ DE REGLAS ----------
# IMPORTANTE:
# - 'gel 1 / gel 2 / gel 3' es parte del NOMBRE del tubo
# - NO representa cantidad
RULES = {
    "Villarrica": {
        "Glucosa": {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
        "GGT": {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
        "Troponina": {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
        "Progesterona": {"tubo": "tubo amarillo gel 2", "proceso": "NO DEFINIDO"},
        "LH": {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
    },
    "Loncoche": {
        "Glucosa": {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
        "GGT": {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
        "Troponina": {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
        "Progesterona": {"tubo": "tubo amarillo gel 2", "proceso": "NO DEFINIDO"},
        "LH": {"tubo": "tubo amarillo gel 3", "proceso": "DERIVA A VILLARRICA"},
    },
    "Temuco": {
        "Glucosa": {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
        "GGT": {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
        "Troponina": {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
        "Progesterona": {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
        "LH": {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
    },
}

# ---------- INPUTS ----------
examenes_sel = st.multiselect("Selecciona examen(es)", EXAMENES)
hospital = st.selectbox("Selecciona hospital", HOSPITALES)

st.divider()

# ---------- MOTOR ----------
if not examenes_sel:
    st.info("Selecciona al menos un examen para calcular tubos y lugar de proceso.")
else:
    detalle = []
    tubos_unicos = set()

    for ex in examenes_sel:
        info = RULES[hospital].get(
            ex,
            {"tubo": "NO DEFINIDO", "proceso": "NO DEFINIDO"}
        )

        tubos_unicos.add(info["tubo"])

        detalle.append({
            "Examen": ex,
            "Tubo": info["tubo"],
            "Lugar de proceso": info["proceso"],
        })

    # ---------- SALIDA ----------
    st.markdown("### Tubos a tomar (únicos)")
    for t in sorted(tubos_unicos):
        st.write(f"- {t}")

    st.divider()

    st.markdown("### Detalle por examen")
    df = pd.DataFrame(detalle)
    st.dataframe(df, use_container_width=True, hide_index=True)

    with st.expander("Reglas implementadas (para desarrolladores)"):
        st.write(
            "- El usuario selecciona Hospital y Exámenes.\n"
            "- El sistema consulta la matriz Hospital + Examen.\n"
            "- Se listan tubos únicos (sin duplicar).\n"
            "- El lugar de proceso está asociado a Hospital + Examen.\n"
            "- 'gel 1/2/3' es solo nombre del tubo, NO cantidad."
        )

st.divider()
st.caption("Elaborado por TM. Camilo Muñoz, Enero 2026")
