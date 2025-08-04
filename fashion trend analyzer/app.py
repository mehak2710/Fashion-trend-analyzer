import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fashion Trend Analyzer", layout="centered")
st.title("👗 Fashion Trend Analyzer")
st.markdown("Visualize example fashion trend data with no external files or APIs.")

# 📊 Hardcoded sample trend data
data = {
    "Month": pd.date_range(start="2022-01-01", periods=12, freq='M'),
    "Crop Top":     [25, 28, 30, 40, 45, 50, 48, 55, 60, 58, 55, 50],
    "Denim Jacket": [40, 38, 35, 33, 32, 34, 37, 39, 38, 40, 42, 45],
    "Boho Dress":   [30, 33, 35, 40, 42, 45, 47, 50, 52, 51, 49, 47],
    "Sneakers":     [35, 36, 38, 42, 45, 47, 50, 53, 56, 54, 52, 51],
    "Bucket Hat":   [20, 22, 25, 30, 35, 40, 38, 42, 44, 43, 40, 38]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Sidebar selection
options = list(df.columns[1:])
selected_items = st.multiselect("Choose fashion items to display:", options, default=["Crop Top", "Denim Jacket"])

# Plot
if selected_items:
    st.subheader("📈 Monthly Trend Overview")
    fig, ax = plt.subplots(figsize=(10, 5))
    for item in selected_items:
        ax.plot(df["Month"], df[item], label=item)
    ax.set_xlabel("Month")
    ax.set_ylabel("Trend Score")
    ax.set_title("Fashion Trend Comparison")
    ax.legend()
    st.pyplot(fig)
else:
    st.info("Please select at least one fashion item.")
