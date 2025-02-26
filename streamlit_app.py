import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder


st.title("📂 CSV File Reader in Streamlit")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📊 **Preview of the CSV File:**")
    st.dataframe(df)

    st.write("📝 **Basic File Information:**")
    st.write(df.describe(include="all"))  # Summary statistics
    st.write(f"**Rows:** {df.shape[0]}, **Columns:** {df.shape[1]}")
    st.write(f"what is the next step?");
    
    # Normalize features
    scaler = StandardScaler()
    df[df.columns] = scaler.fit_transform(df)
    st.dataframe(df)

