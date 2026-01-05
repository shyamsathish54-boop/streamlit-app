import streamlit as st
import pandas as pd
import numpy as np

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Streamlit Data Explorer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Streamlit Data Explorer")
st.write("Upload a CSV or Excel file to explore the data.")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.header("App Controls")
show_raw_data = st.sidebar.checkbox("Show raw data", value=True)
show_summary = st.sidebar.checkbox("Show summary statistics", value=True)

# --------------------------------------------------
# FILE UPLOADER (CSV + EXCEL)
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

# --------------------------------------------------
# MAIN LOGIC
# --------------------------------------------------
if uploaded_file is not None:
    try:
        # Detect file type
        file_name = uploaded_file.name

        if file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        elif file_name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)

        else:
            st.error("Unsupported file format")
            st.stop()

        st.success("File uploaded successfully ✅")

        if show_raw_data:
            st.subheader("📄 Raw Data")
            st.dataframe(df)

        if show_summary:
            st.subheader("📈 Summary Statistics")
            st.write(df.describe(include="all"))

        st.subheader("🔍 Column Analysis")
        column = st.selectbox("Select a column", df.columns)

        if pd.api.types.is_numeric_dtype(df[column]):
            st.metric("Mean", round(df[column].mean(), 2))
            st.metric("Median", round(df[column].median(), 2))
            st.line_chart(df[column])
        else:
            st.write(df[column].value_counts())

    except Exception as e:
        st.error("Error while processing file")
        st.exception(e)

else:
    st.info("👆 Please upload a CSV or Excel file")

st.markdown("---")
st.caption("Built with Streamlit")

