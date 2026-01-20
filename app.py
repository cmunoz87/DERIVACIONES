    import streamlit as st
    import pandas as pd

    st.set_page_config(page_title="Motor de Tubos y Derivación", layout="centered")

    # ---------- LOGO (mismo estilo que el anterior: centrado y pequeño) ----------
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.png", width=220)

    st.markdown("## Motor de Tubos y Derivación")
    st.caption("Herramienta explicativa para desarrolladores: define tubo y lugar de proceso según Hospital + Examen.")

    st.divider()

    # ---------- Catálogos ----------
    HOSPITALES = ["Villarrica", "Loncoche", "Temuco"]

    EXAMENES = [
        "Glucosa",
        "GGT",
        "Troponina",
        "Progesterona",
        "LH",
    ]

    # ---------- Matriz de reglas (EDITABLE) ----------
    # Nota: "gel 1/2/3" es parte del NOMBRE del tubo y NO representa cantidad.
    # Si algún valor no está definido en la tabla original, déjalo como "NO DEFINIDO" y luego se ajusta.
    RULES = {
        "Villarrica": {
            "Glucosa":      {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
            "GGT":          {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
            "Troponina":    {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
            "Progesterona": {"tubo": "tubo amarillo gel 2", "proceso": "NO DEFINIDO"},
            "LH":           {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
        },
        "Loncoche": {
            "Glucosa":      {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
            "GGT":          {"tubo": "tubo amarillo gel 1", "proceso": "PROCESA LOCAL"},
            "Troponina":    {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
            "Progesterona": {"tubo": "tubo amarillo gel 2", "proceso": "NO DEFINIDO"},
            "LH":           {"tubo": "tubo amarillo gel 3", "proceso": "DERIVA A VILLARRICA"},
        },
        "Temuco": {
            "Glucosa":      {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
            "GGT":          {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
            "Troponina":    {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
            "Progesterona": {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
            "LH":           {"tubo": "tubo amarillo gel 1", "proceso": "NO DEFINIDO"},
        },
    }

    # ---------- Inputs ----------
    examenes_sel = st.multiselect("Selecciona examen(es)", EXAMENES)
    hospital = st.selectbox("Selecciona hospital", HOSPITALES)

    st.divider()

    # ---------- Motor ----------
    if not examenes_sel:
        st.info("Selecciona al menos un examen para calcular tubos y lugar de proceso.")
    else:
        detalle = []
        tubos_unicos = set()

        for ex in examenes_sel:
            info = RULES.get(hospital, {}).get(ex, {"tubo": "NO DEFINIDO", "proceso": "NO DEFINIDO"})
            tubo = info.get("tubo", "NO DEFINIDO")
            proceso = info.get("proceso", "NO DEFINIDO")

            tubos_unicos.add(tubo)
            detalle.append({"Examen": ex, "Tubo": tubo, "Lugar de proceso": proceso})

        # Salida A: tubos únicos
        st.markdown("### Tubos a tomar (únicos)")
        for t in sorted(tubos_unicos):
            st.write(f"- {t}")

        st.divider()

        # Salida B: detalle por examen
        st.markdown("### Detalle por examen")
        df = pd.DataFrame(detalle)
        st.dataframe(df, use_container_width=True, hide_index=True)

        # Ayuda para devs
        with st.expander("Reglas implementadas (para desarrolladores)"):
            st.write(
                "- El usuario selecciona Hospital y Exámenes.
"
                "- Para cada combinación Hospital + Examen, la app consulta una matriz (RULES).
"
                "- La app entrega: (1) Tubos únicos sin duplicar, (2) Detalle por examen con Lugar de proceso.
"
                "- 'gel 1/2/3' es parte del nombre del tubo y NO representa cantidad.
"
                "- Los valores 'NO DEFINIDO' indican campos pendientes de completar según la tabla oficial."
            )

    st.divider()
    st.caption("Elaborado por TM. Camilo Muñoz, Enero 2025")
