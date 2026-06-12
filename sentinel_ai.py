import streamlit as st

st.title("Sentinel AI")

st.subheader("Fraud Detection Dashboard")

st.metric("Total Records", "9082")
st.metric("Fraud Cases", "81")

st.write("Model Accuracy: 99.61%")
st.write("Precision: 100%")
st.write("Recall: 67%")

st.success("High Risk Accounts Detected")

st.table({
    "Account": ["Mule_A", "Mule_B"],
    "Risk Score": [86.18, 80.73]
})