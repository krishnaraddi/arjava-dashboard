# Aarjava Dashboard 🌿

**Flow with Integrity. Operate with Intelligence.**  
Aarjava Dashboard is a Streamlit-based web application designed to visualize agent coordination and ESG metrics for industrial operations—starting with cement manufacturing. It integrates Gen AI agents, synthetic ESG simulations, and real-time Pub/Sub messaging to support intelligent, self-optimizing plant behavior.

---

## 🚀 Features

- 📊 **ESG Metrics Visualization**  
  Real-time charts for energy usage, CO₂ emissions, fault recovery, and sustainability KPIs.

- 🤖 **Agent Coordination Panel**  
  Displays status and decisions from deployed Gen AI agents (e.g. KilnAgent, CoolerAgent).

- 🔁 **Synthetic Data Generator**  
  Simulates ESG performance trends for testing and prototyping.

- ☁️ **Cloud-Native Deployment**  
  Built for Google Cloud Run with CI/CD via GitHub Actions.

---

## 🧱 Tech Stack

- **Frontend**: Streamlit + Plotly  
- **Backend**: Python (FastAPI-ready)  
- **Cloud**: Google Cloud Run, Pub/Sub, Monitoring  
- **CI/CD**: GitHub Actions  
- **AI Agents**: Modular Gen AI architecture (external integration)

---

## 📦 Folder Structure
arjava-dashboard/ ├── dashboard.py               # Main Streamlit app ├── utils/ │   ├── pubsub_reader.py       # Agent status via Pub/Sub │   └── monitoring.py          # ESG metrics generator ├── assets/ │   └── aarjava_logo.png       # Branded logo ├── requirements.txt ├── Dockerfile ├── .github/ │   └── workflows/deploy.yaml # CI/CD pipeline


---

## 🔧 Deployment

To deploy on Google Cloud Run:

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT/arjava-dashboard
gcloud run deploy arjava-dashboard \
  --image gcr.io/YOUR_PROJECT/arjava-dashboard \
  --platform=managed \
  --region=asia-south1 \
  --allow-unauthenticated
  📄 License
This project is licensed under the MIT License.
Feel free to fork, extend, and deploy responsibly.

Built by 
[Krishnaraddi V K](https://www.linkedin.com/in/krishnaraddi/)
Founder, Aarjava Intelligence
Mechanical Engineer with 15+ years in IT
Specializing in Gen AI, Agentic AI, and ESG-aligned industrial transformation


 


