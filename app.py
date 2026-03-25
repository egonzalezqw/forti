import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Cybersecurity Quick Assessment", layout="wide")

# ---- Título ----
st.title("🔒 Cybersecurity Quick Assessment")
st.markdown("""
Obtén un diagnóstico rápido del estado de tu seguridad de red.
Identifica riesgos, conoce tu score y recibe recomendaciones prácticas.
""")

# ---- Inputs: Estado actual ----
st.header("1️⃣ Información básica")
firewall_status = st.selectbox("Estado del firewall", ["No implementado", "Parcial", "Completo"])
vpn_usage = st.selectbox("Uso de VPN", ["No usado", "Uso parcial", "Uso completo"])
internet_exposure = st.slider("Exposición a internet (% de servicios expuestos)", 0, 100, 20)
network_segmentation = st.selectbox("Segmentación de red", ["No segmentada", "Parcial", "Completa"])

# ---- Score y riesgos ----
st.header("2️⃣ Resultado rápido")

# Generar score simple basado en inputs (solo ejemplo)
score = 100
if firewall_status == "No implementado":
    score -= 30
elif firewall_status == "Parcial":
    score -= 10

if vpn_usage == "No usado":
    score -= 20
elif vpn_usage == "Uso parcial":
    score -= 5

score -= int(internet_exposure * 0.2)

if network_segmentation == "No segmentada":
    score -= 20
elif network_segmentation == "Parcial":
    score -= 10

score = max(score, 0)

st.subheader(f"🔹 Security Score: {score}/100")

# Riesgos detectados
risks = []
if firewall_status != "Completo":
    risks.append("Firewall insuficiente")
if vpn_usage != "Uso completo":
    risks.append("VPN no aplicada correctamente")
if internet_exposure > 50:
    risks.append("Alta exposición a internet")
if network_segmentation != "Completa":
    risks.append("Segmentación de red insuficiente")

st.subheader("⚠️ Riesgos detectados")
if risks:
    for r in risks:
        st.write(f"- {r}")
else:
    st.write("✅ Sin riesgos críticos detectados")

# ---- Roadmap de mejoras ----
st.header("3️⃣ Roadmap recomendado")
roadmap = {
    "Firewall": "Actualizar o implementar reglas completas",
    "VPN": "Asegurar uso completo en todos los accesos remotos",
    "Segmentación": "Segregar la red por departamentos y servicios",
    "Exposición a Internet": "Revisar y limitar servicios expuestos"
}

for k, v in roadmap.items():
    st.write(f"**{k}:** {v}")

# ---- Visualización simple ----
st.header("📊 Visualización")
chart_data = pd.DataFrame({
    'Área': ['Firewall', 'VPN', 'Exposición Internet', 'Segmentación'],
    'Score': [
        100 if firewall_status == "Completo" else 50 if firewall_status == "Parcial" else 0,
        100 if vpn_usage == "Uso completo" else 50 if vpn_usage == "Uso parcial" else 0,
        max(0, 100 - internet_exposure),
        100 if network_segmentation == "Completa" else 50 if network_segmentation == "Parcial" else 0
    ]
})
st.bar_chart(chart_data.set_index('Área'))
