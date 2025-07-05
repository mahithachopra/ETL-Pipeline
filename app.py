import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from io import BytesIO

# === ETL Function ===
def etl_pipeline(df):
    # Drop empty rows or columns
    df = df.dropna(how='all').dropna(axis=1, how='all')

    # Separate features and optional target
    target_column = st.selectbox("Select target column (optional):", ["None"] + list(df.columns))
    y = None

    if target_column != "None":
        y = df[target_column]
        X = df.drop(columns=[target_column])
    else:
        X = df.copy()

    # Identify types
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()

    # Pipelines
    numeric_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    categorical_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combine
    preprocessor = ColumnTransformer([
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

    # Fit and transform
    X_transformed = preprocessor.fit_transform(X)

    # Get feature names
    cat_cols = preprocessor.named_transformers_['cat']['encoder'].get_feature_names_out(categorical_features)
    all_columns = numeric_features + list(cat_cols)

    # DataFrame
    X_df = pd.DataFrame(X_transformed.toarray() if hasattr(X_transformed, 'toarray') else X_transformed,
                        columns=all_columns)

    if y is not None:
        X_df[target_column] = y.reset_index(drop=True)

    return X_df

# === Streamlit UI ===
st.set_page_config(page_title="ETL Pipeline Tool", layout="wide")
st.title("🔄 General ETL Pipeline for Any Dataset")
st.write("Upload your dataset (CSV), and this tool will clean, transform, and let you download the processed file.")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Preview of Uploaded Data")
    st.dataframe(df.head())

    with st.spinner("🔧 Processing..."):
        cleaned_df = etl_pipeline(df)

    st.subheader("✅ Transformed Data")
    st.dataframe(cleaned_df.head())

    # Download button
    def convert_df(df):
        buffer = BytesIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)
        return buffer

    st.download_button(
        label="📥 Download Cleaned CSV",
        data=convert_df(cleaned_df),
        file_name="transformed_dataset.csv",
        mime="text/csv"
    )
