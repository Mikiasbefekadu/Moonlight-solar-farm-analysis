import numpy as np
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Set the title of the app
st.title("Exploratory Data Analysis Dashboard")

# Sidebar for Navigation
st.sidebar.title("Navigation")
country = st.sidebar.selectbox("Select a Country", ["Togo", "Sierra Leone", "Benin"])
uploaded_file = st.sidebar.file_uploader("Upload a new dataset", type=["csv"])

# Checkboxes for different analyses
show_statistics = st.sidebar.checkbox("Show Key Statistics", value=True)
show_univariate_analysis = st.sidebar.checkbox("Univariate Analysis", value=False)
show_correlation_matrix = st.sidebar.checkbox("Correlation Matrix", value=False)
show_data_cleaning = st.sidebar.checkbox("Data Cleaning Analysis", value=False)

# Function to load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Preloaded data path (adjust this path as needed)
data_path = "D:/Desktop/Data_folder/data/benin-malanville.csv"

# Load the dataset
df = load_data(data_path)

# Display Static Data for Selected Country
if country:
    st.header(f"{country} Insights")
    
    # Display available columns
    st.subheader("Available Columns in Dataset:")
    # st.write(df.columns.tolist())
    
    # Key Statistics
    if show_statistics:
        st.subheader("Key Statistics")
        st.write(df.describe())

    # Univariate Analysis
    if show_univariate_analysis:
        st.subheader("Univariate Analysis")
        column_to_plot = st.selectbox("Select a column for Univariate Analysis", df.columns.tolist())
        if column_to_plot:
            if pd.api.types.is_numeric_dtype(df[column_to_plot]):
                fig, ax = plt.subplots()
                sns.histplot(data=df, x=column_to_plot, kde=True, ax=ax)
                st.pyplot(fig)
            else:
                st.error("Selected column is not numeric. Please select a numeric column.")

    # Correlation Matrix
if show_correlation_matrix:
    st.subheader("Correlation Matrix")
    
    # Clean the DataFrame to include only numeric columns
    df_cleaned = df.select_dtypes(include=[np.number])
    
    if not df_cleaned.empty:
        correlation_matrix = df_cleaned.corr()
        
        # Create a larger figure
        plt.figure(figsize=(12, 8))
        
        # Create a heatmap with adjustments
        sns.heatmap(
            correlation_matrix, 
            annot=True, 
            fmt=".2f", 
            cmap="coolwarm", 
            linewidths=.5, 
            linecolor='black', 
            annot_kws={"size": 10}  # Adjust the font size of annotations
        )
        
        st.pyplot(plt)
    else:
        st.error("No numeric columns available for correlation.")

    # Data Cleaning Analysis
    if show_data_cleaning:
        st.subheader("Data Cleaning Analysis")
        st.write("### Missing Values")
        st.write(df.isnull().sum())
        st.write("### Duplicates")
        st.write(df.duplicated().sum())

# Custom Data Analysis
if uploaded_file is not None:
    st.subheader("Custom Data Analysis")
    custom_df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data")
    st.write(custom_df.head())
    
    # Summary statistics for the uploaded data
    st.write("### Summary Statistics")
    st.write(custom_df.describe())
    
    # Univariate Analysis for uploaded data
    if show_univariate_analysis:
        column_to_plot_custom = st.selectbox("Select a column for Univariate Analysis from uploaded data", custom_df.columns.tolist())
        if column_to_plot_custom:
            if pd.api.types.is_numeric_dtype(custom_df[column_to_plot_custom]):
                fig_custom = px.histogram(custom_df, x=column_to_plot_custom, title='Histogram of Uploaded Data')
                st.plotly_chart(fig_custom)
            else:
                st.error("Selected column is not numeric. Please select a numeric column.")

    # Correlation Matrix for uploaded data
    if show_correlation_matrix:
        st.subheader("Correlation Matrix for Uploaded Data")
        
        # Clean the custom DataFrame
        custom_df_cleaned = custom_df.select_dtypes(include=[np.number])
        
        if not custom_df_cleaned.empty:
            correlation_matrix_custom = custom_df_cleaned.corr()
            fig_custom, ax_custom = plt.subplots()
            sns.heatmap(correlation_matrix_custom, annot=True, fmt=".2f", cmap="coolwarm", ax=ax_custom)
            st.pyplot(fig_custom)
        else:
            st.error("No numeric columns available for correlation.")

    # Data Cleaning Analysis for uploaded data
    if show_data_cleaning:
        st.subheader("Data Cleaning Analysis for Uploaded Data")
        st.write("### Missing Values")
        st.write(custom_df.isnull().sum())
        st.write("### Duplicates")
        st.write(custom_df.duplicated().sum())

# Data Download
if uploaded_file is not None:
    st.download_button("Download Processed Data", custom_df.to_csv(index=False).encode('utf-8'), "processed_data.csv", "text/csv")

# Additional Features
st.sidebar.title("Additional Features")
if st.sidebar.button("Export Report"):
    st.sidebar.success("Report exported successfully!")

# Theme toggle
theme = st.sidebar.selectbox("Select Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""
        <style>
        .css-1d391kg { background-color: #2C2C2C; color: white; }
        </style>
    """, unsafe_allow_html=True)