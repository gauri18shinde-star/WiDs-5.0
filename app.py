import streamlit as st
import json
import matplotlib.pyplot as plt

st.title("Federated Learning Results")

METRICS_PATH = "models/training_history.json"

with open(METRICS_PATH, "r") as f:
    history = json.load(f)

rounds = [h["round"] for h in history]
accuracies = [h["accuracy"] for h in history]

st.subheader("Accuracy vs Rounds")

fig, ax = plt.subplots()
ax.plot(rounds, accuracies, marker="o")
ax.set_xlabel("Round")
ax.set_ylabel("Accuracy")
ax.set_ylim(0, 1)
ax.grid(True)

st.pyplot(fig)

st.subheader("Final Summary")

st.write(f"""
- **Total Rounds:** {len(rounds)}
- **Final Round:** {rounds[-1]}
- **Final Accuracy:** {accuracies[-1]:.4f}
""")

