import streamlit as st
import base64
from utils.pubsub_reader import get_pubsub_data
from utils.monitoring import get_esg_metrics
import streamlit as st
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Aarjava dashboard is healthy"}


st.set_page_config(page_title="Aarjava Dashboard", layout="wide")

# ─── Custom CSS ───────────────────────────────────────────────
   
def inject_css():
    st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
        font-family: 'Segoe UI', sans-serif;
        color: #000000;  /* Default text color: black */
    }

    .logo {
        width: 180px;
        margin-bottom: 10px;
    }

    .header {
        font-size: 32px;
        font-weight: bold;
        color: #ffffff !important;  /* Header text: white */
        margin-bottom: 20px;
    }

    .kpi-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        color: #000000;  /* KPI card text: black */
    }

    .agent-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.1);
        color: #000000 !important;  /* Agent labels: black */
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)
inject_css()

# ─── Logo and Header ──────────────────────────────────────────
with open("assets/aarjava_logo.png", "rb") as f:
    logo_data = base64.b64encode(f.read()).decode()
st.markdown(f"<img src='data:image/png;base64,{logo_data}' class='logo'>", unsafe_allow_html=True)
st.markdown("<div class='header'>Aarjava Agentic Dashboard</div>", unsafe_allow_html=True)

# ─── Agent Coordination ───────────────────────────────────────
st.subheader("Agent Coordination")
agent_data = get_pubsub_data()

cols = st.columns(len(agent_data))
for i, (agent, status) in enumerate(agent_data.items()):
    with cols[i]:
        st.markdown(f"<div class='kpi-card'><h4>{agent}</h4><p>Status: {status['status']}</p><p>Last Msg: {status['last_message']}</p></div>", unsafe_allow_html=True)

# ─── ESG Metrics ──────────────────────────────────────────────
st.subheader("ESG Performance")
esg = get_esg_metrics()

kpi_cols = st.columns(3)
kpi_cols[0].metric("Energy Saved", f"{esg['energy_saved']}%", "-12%")
kpi_cols[1].metric("CO₂ Reduction", f"{esg['co2_reduction']} kg/ton", "-0.8")
kpi_cols[2].metric("Fault Recovery", f"{esg['fault_recovery']} min", "-40%")

st.line_chart(esg["trend_data"])