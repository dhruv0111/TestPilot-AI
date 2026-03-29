import streamlit as st
import requests

# ------------------- PAGE CONFIG -------------------
st.set_page_config(page_title="Engineering Intelligence AI", layout="wide")

st.title("Engineering Intelligence AI")
st.subheader("LLM + RAG + ML System for Bug Analysis")

# ------------------- BACKEND STATUS -------------------
try:
    requests.get("https://backend-ai-x6r7.onrender.com/health")
    st.success("🟢 Backend Connected")
except:
    st.error("🔴 Backend Not Running")

# ------------------- SESSION STATE (HISTORY) -------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ------------------- INPUT -------------------
query = st.text_input("Ask your engineering question")

# ------------------- BUTTON ACTION -------------------
if st.button("Analyze"):

    if query.strip() == "":
        st.warning("Please enter a query")
    else:
        with st.spinner("Analyzing..."):

            try:
                res = requests.post(
                    "https://backend-ai-x6r7.onrender.com/query",
                    json={"query": query}
                )

                data = res.json()

                if "error" in data:
                    st.error(data["error"])

                else:
                    st.success("Analysis Complete")

                    # ------------------- SAVE HISTORY -------------------
                    st.session_state.history.append((query, data["answer"]))

                    # ------------------- ANSWER -------------------
                    st.markdown("## Answer")
                    st.markdown(data["answer"])

                    # ------------------- RISK ANALYSIS -------------------
                    st.markdown("## Risk Analysis")

                    risk_score = data["risk_score"]

                    if risk_score > 0.7:
                        st.error(f"🔴 High Risk ({round(risk_score, 2)})")
                    elif risk_score > 0.4:
                        st.warning(f"🟡 Medium Risk ({round(risk_score, 2)})")
                    else:
                        st.success(f"🟢 Low Risk ({round(risk_score, 2)})")

                    st.write(f"Predicted Risk (0=Low,1=High): {data['predicted_risk']}")

                    # ------------------- METRICS -------------------
                    st.markdown("## System Metrics")

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric(
                            "Latency (sec)",
                            round(data["metrics"]["latency_sec"], 2)
                        )

                    with col2:
                        st.metric(
                            "Retrieval Score",
                            round(data["metrics"]["retrieval_score"], 2)
                        )

                    with col3:
                        st.metric(
                            "Response Quality",
                            round(data["metrics"]["response_quality"], 2)
                        )

            except Exception as e:
                st.error(f"Frontend Error: {str(e)}")

# ------------------- HISTORY DISPLAY -------------------
st.markdown("## Previous Queries")

if len(st.session_state.history) == 0:
    st.info("No queries yet")
else:
    for q, a in reversed(st.session_state.history[-5:]):
        st.write(f"**Q:** {q}")
        st.write(f"**A:** {a}")
        st.markdown("---")