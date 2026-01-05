import streamlit as st
import pandas as pd
import numpy as np

# --------------------------------------------------
# PAGE CONFIG (must be at the top)
# --------------------------------------------------
st.set_page_config(
    page_title="Streamlit Demo App",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# TITLE & DESCRIPTION
# --------------------------------------------------
st.title("📊 Streamlit Data Explorer")
st.write(
    """
    This is a simple Streamlit app that allows you to upload a CSV file,
    explore the data, and view basic statistics.
    """
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.header("App Controls")

show_raw_data = st.sidebar.checkbox("Show raw data", value=True)
show_summary = st.sidebar.checkbox("Show summary statistics", value=True)

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

# --------------------------------------------------
# MAIN LOGIC
# --------------------------------------------------
if uploaded_file is not None:
    try:
        # Read CSV
        df = pd.read_csv(uploaded_file)

        st.success("File uploaded successfully ✅")

        # Show raw data
        if show_raw_data:
            st.subheader("📄 Raw Data")
            st.dataframe(df)

        # Show summary
        if show_summary:
            st.subheader("📈 Summary Statistics")
            st.write(df.describe(include="all"))

        # Column selection
        st.subheader("🔍 Column Analysis")
        column = st.selectbox(
            "Select a column to analyze",
            df.columns
        )

        if pd.api.types.is_numeric_dtype(df[column]):
            st.write("**Mean:**", round(df[column].mean(), 2))
            st.write("**Median:**", round(df[column].median(), 2))
            st.write("**Standard Deviation:**", round(df[column].std(), 2))

            st.line_chart(df[column])

        else:
            st.write("Value Counts:")
            st.write(df[column].value_counts())

    except Exception as e:
        st.error("Something went wrong while reading the file.")
        st.exception(e)

else:
    st.info("👆 Please upload a CSV file to get started.")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
