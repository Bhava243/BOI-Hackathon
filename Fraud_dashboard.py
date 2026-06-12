import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Fraud Detection AI",
    layout="wide"
)

st.title("Fraud Detection AI")
st.subheader(
    "Graph-Based Mule Account Detection"
)

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Transactions",
        "9082"
    )

with col2:
    st.metric(
        "Fraud Cases",
        "81"
    )

with col3:
    st.metric(
        "Accuracy",
        "99.61%"
    )

with col4:
    st.metric(
        "High Risk Accounts",
        "12"
    )

st.divider()

# Model Results

st.subheader(
    "Model Performance"
)

model_df = pd.DataFrame({
    "Metric":[
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ],
    "Value":[
        "99.61%",
        "100%",
        "67%",
        "80%"
    ]
})

st.dataframe(
    model_df,
    use_container_width=True
)

st.divider()

# Risk Accounts

st.subheader(
    "High Risk Accounts"
)

risk_df = pd.DataFrame({

    "Account":[
        "Mule_A",
        "Mule_B",
        "Mule_D"
    ],

    "Risk Score":[
        92,
        85,
        88
    ],

    "Risk Level":[
        "High",
        "High",
        "High"
    ]
})

st.dataframe(
    risk_df,
    use_container_width=True
)

st.divider()

# Alerts

st.subheader(
    "Real-Time Alerts"
)

st.error(
    " Mule_A detected (Risk Score 92)"
)

st.error(
    " Mule_B detected (Risk Score 85)"
)

st.error(
    " Mule_D detected (Risk Score 88)"
)

st.divider()

# Mule Network

st.subheader(
    "Mule Account Network"
)

G = nx.DiGraph()

G.add_edge("Victim","Mule_A")
G.add_edge("Mule_A","Mule_B")
G.add_edge("Mule_A","Mule_C")
G.add_edge("Mule_A","Mule_D")
G.add_edge("Mule_B","Cash_Out")
G.add_edge("Mule_C","Cash_Out")
G.add_edge("Mule_D","Crypto")

fig, ax = plt.subplots(
    figsize=(10,6)
)

pos = nx.spring_layout(
    G,
    seed=42
)

colors = []

for node in G.nodes():

    if node == "Victim":
        colors.append("skyblue")

    elif "Mule" in node:
        colors.append("red")

    else:
        colors.append("green")

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=colors,
    node_size=3500,
    ax=ax
)

st.pyplot(fig)

st.divider()

# External Sources

st.subheader(
    "External Intelligence Sources"
)

st.success(
    " RBI Regulatory Alerts"
)

st.success(
    " NCRP Cyber Fraud Complaints"
)

st.success(
    " Fraud Monitoring Alerts"
)

st.success(
    " Transaction Monitoring System Alerts"
)

st.divider()

st.info(
    "Fraud Detection combines machine learning and graph analytics to detect suspicious mule account networks."
)