import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# ------------------------------
# App Title
# ------------------------------
st.set_page_config(page_title="BootsGalore Analytics Dashboard", layout="wide")
st.title(" BootsGalore Analytics Cloud Dashboard")

# ------------------------------
# Required CSV files
# ------------------------------
csv_files = {
    "Sizes": "df_Number_of_Selected_Sizes.csv",
    "Stud Types": "df_Number_of_Stud_Type_Selected.csv",
    "Brand Preferences": "df_Number_of_Brand_Preference_Selected.csv"
}

# ------------------------------
# Check CSV files exist
# ------------------------------
missing_files = [f for f in csv_files.values() if not os.path.exists(f)]
if missing_files:
    st.error(f"The following required CSV files are missing: {missing_files}")
    st.stop()

# ------------------------------
# Load CSVs
# ------------------------------
def load_csv(file_path, rename_cols):
    df = pd.read_csv(file_path)
    df.columns = rename_cols
    return df

df_sizes = load_csv(csv_files["Sizes"], ['Size', 'Total'])
df_stud_type = load_csv(csv_files["Stud Types"], ['Stud_Type', 'Total'])
df_brand = load_csv(csv_files["Brand Preferences"], ['Brand', 'Total'])

# ------------------------------
# Helper function: Plot bar chart
# ------------------------------
def plot_bar_chart(df, x_col, y_col, title, xlabel, ylabel):
    df_sorted = df.sort_values(by=y_col, ascending=False)  # descending order
    fig, ax = plt.subplots()
    bars = ax.bar(df_sorted[x_col], df_sorted[y_col], color="grey")
    
    # Add labels on bars
    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height(),
            str(int(bar.get_height())),
            ha='center', va='bottom'
        )
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

# ------------------------------
# Sidebar Navigation
# ------------------------------
st.sidebar.title(" Dashboard Navigation")
option = st.sidebar.radio(
    "Select a view:",
    (
        "Size Preferences",
        "Stud Type Preferences",
        "Brand Preferences"
    )
)

# ------------------------------
# Visualizations
# ------------------------------
if option == "Size Preferences":
    st.subheader("Size Preferences")
    plot_bar_chart(df_sizes, 'Size', 'Total', 'Size Preferences', 'Size', 'Total Selected')

elif option == "Stud Type Preferences":
    st.subheader("Stud Type Preferences")
    plot_bar_chart(df_stud_type, 'Stud_Type', 'Total', 'Stud Type Preferences', 'Stud Type', 'Total Selected')

elif option == "Brand Preferences":
    st.subheader("Brand Preferences")
    plot_bar_chart(df_brand, 'Brand', 'Total', 'Brand Preferences', 'Brand', 'Total Selected')

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown("Developed & Powered by Luyanda Hele")
















