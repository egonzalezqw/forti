import streamlit as st
import pandas as pd

st.set_page_config(page_title="FortiGate Security Sizing Tool", layout="wide")

st.title("🛡️ FortiGate Security Sizing Tool")
st.markdown("""
Ingresa tus parámetros y recibe una recomendación instantánea del modelo, licencias y features sugeridos.
Ideal para clientes que buscan decisiones rápidas y confiables.
""")

# ---- Inputs ----
st.header("1️⃣ Datos de la organización")
num_users = st.number_input("Número de usuarios", min_value=1, step=1, value=50)
num_sites = st.number_input("Número de sedes", min_value=1, step=1, value=1)
estimated_traffic = st.number_input("Tráfico estimado (Mbps)", min_value=1, step=1, value=100)

# ---- Lógica de sizing ----
st.header("2️⃣ Resultado recomendado")

# Modelo FortiGate (ejemplo simplificado)
def recommend_model(users, traffic):
    if users <= 50 and traffic <= 200:
        return "FortiGate 60F"
    elif users <= 200 and traffic <= 1000:
        return "FortiGate 100F"
    elif users <= 500 and traffic <= 5000:
        return "FortiGate 300E"
    else:
        return "FortiGate 600C+"

model = recommend_model(num_users, estimated_traffic)

# Licencias sugeridas (simplificación)
def suggest_licenses(users, model):
    base = 1
    if "60F" in model:
        return f"{base} x FortiCare + 1 x UTM Bundle (IPS, AV, Web Filtering)"
    elif "100F" in model:
        return f"{base} x FortiCare + {users//50} x UTM Bundle"
    elif "300E" in model:
        return f"{base} x FortiCare + {users//100} x UTM Bundle"
    else:
        return f"{base} x FortiCare + {users//200} x UTM Bundle"

licenses = suggest_licenses(num_users, model)

# Features recomendadas
features = ["IPS", "Antivirus", "Web Filtering"]
if num_sites > 1:
    features.append("SD-WAN / VPN")

# ---- Output ----
st.subheader(f"✅ Modelo recomendado: {model}")
st.subheader("📄 Licencias sugeridas:")
st.write(licenses)
st.subheader("💡 Features sugeridos:")
st.write(", ".join(features))

# ---- Visualización rápida ----
st.header("📊 Resumen visual")
summary = pd.DataFrame({
    "Parámetro": ["Usuarios", "Sedes", "Tráfico (Mbps)"],
    "Valor": [num_users, num_sites, estimated_traffic]
})
st.table(summary)
