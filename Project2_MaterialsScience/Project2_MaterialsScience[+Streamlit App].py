import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Materials Science Explorer", layout="wide")

st.title("Materials Science Plot Viewer")

#load data
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

#CSV path
DEFAULT_PATH = #your own path to the CSV

#load automatically — no sidebar, no file uploader
if os.path.exists(DEFAULT_PATH):
    df = load_data(DEFAULT_PATH)
else:
    st.error("CSV file not found at the given path.")
    st.stop()

#identify numeric + all cols
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
all_cols = df.columns.tolist()

#dropdown centered at top
plot_type = st.selectbox(
    "Select a Plot Type",
    ["Histogram", "Scatter Plot", "Correlation Heatmap"]
)

#histogram
if plot_type == "Histogram":
    col = st.selectbox("Select Column", numeric_cols)
    bins = st.slider("Bins", 10, 100, 30)

    fig, ax = plt.subplots()
    sns.histplot(df[col], bins=bins, kde=True, ax=ax)
    ax.set_title(f"Distribution of {col}")

    st.pyplot(fig)

#scatter plot
elif plot_type == "Scatter Plot":
    x = st.selectbox("X Axis", numeric_cols)
    y = st.selectbox("Y Axis", numeric_cols)

    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=x, y=y, ax=ax)
    ax.set_title(f"{x} vs {y}")

    st.pyplot(fig)

#correlation heatmap
elif plot_type == "Correlation Heatmap":
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Matrix")

    st.pyplot(fig)
