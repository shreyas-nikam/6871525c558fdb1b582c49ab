
import streamlit as st
import pandas as pd
import numpy as np

def generate_synthetic_data(num_units, has_time_series):
    """Generates a pandas.DataFrame with synthetic operational risk data."""
    if not isinstance(has_time_series, bool):
        raise TypeError("has_time_series must be a boolean")

    risk_unit_types = ['Business Unit', 'Department', 'Team']
    risk_ratings = ['Low', 'Medium', 'High', 'Very High']
    control_types = ['Preventative', 'Detective', 'Corrective']

    data = {
        'Risk_Assessment_Unit_ID': range(1, num_units + 1),
        'Risk_Assessment_Unit_Type': np.random.choice(risk_unit_types, num_units),
        'Inherent_Risk_Rating': np.random.choice(risk_ratings, num_units),
        'Control_Effectiveness_Rating': np.random.choice(risk_ratings, num_units),
        'Control_Type': np.random.choice(control_types, num_units),
        'Control_Key_Status': np.random.choice([True, False], num_units),
        'Process_Complexity': np.random.randint(1, 11, num_units),
        'Operational_Metric_1': np.random.normal(50, 10, num_units),
        'Operational_Metric_2': np.random.normal(100, 20, num_units)
    }
    df = pd.DataFrame(data)

    if has_time_series:
        df['Assessment_Cycle'] = np.random.randint(2020, 2024, num_units)
    return df

def validate_data(df):
    """Validates DataFrame for expected columns, data types, PK uniqueness, and missing values."""
    expected_columns = ['Risk_Assessment_Unit_ID', 'Risk_Assessment_Unit_Type', 'Inherent_Risk_Rating',
                        'Control_Effectiveness_Rating', 'Control_Type', 'Control_Key_Status',
                        'Process_Complexity', 'Operational_Metric_1', 'Operational_Metric_2']

    for col in expected_columns:
        if col not in df.columns:
            raise KeyError(f"Missing column: {col}")

    if df['Risk_Assessment_Unit_ID'].duplicated().any():
        raise ValueError("Duplicate Risk_Assessment_Unit_ID values found.")

    if df.isnull().any().any():
        raise ValueError("Missing values found in DataFrame.")

    if not pd.api.types.is_numeric_dtype(df['Risk_Assessment_Unit_ID']):
        raise TypeError("Risk_Assessment_Unit_ID should be numeric.")
    if not pd.api.types.is_string_dtype(df['Risk_Assessment_Unit_Type']):
        raise TypeError("Risk_Assessment_Unit_Type should be string.")
    if not pd.api.types.is_string_dtype(df['Inherent_Risk_Rating']):
        raise TypeError("Inherent_Risk_Rating should be string.")
    if not pd.api.types.is_string_dtype(df['Control_Effectiveness_Rating']):
        raise TypeError("Control_Effectiveness_Rating should be string.")
    if not pd.api.types.is_string_dtype(df['Control_Type']):
        raise TypeError("Control_Type should be string.")
    if not pd.api.types.is_bool_dtype(df['Control_Key_Status']):
        raise TypeError("Control_Key_Status should be boolean.")
    if not pd.api.types.is_numeric_dtype(df['Process_Complexity']):
        raise TypeError("Process_Complexity should be numeric.")
    if not pd.api.types.is_numeric_dtype(df['Operational_Metric_1']):
        raise TypeError("Operational_Metric_1 should be numeric.")
    if not pd.api.types.is_numeric_dtype(df['Operational_Metric_2']):
        raise TypeError("Operational_Metric_2 should be numeric.")

def run_page1():
    st.header("Data Generation and Validation")
    num_units = st.slider("Number of Risk Units", 10, 500, 100)
    has_time_series = st.checkbox("Include Time Series Data", True)

    try:
        synthetic_df = generate_synthetic_data(num_units, has_time_series)
        st.subheader("Generated Synthetic Data")
        st.dataframe(synthetic_df.head())
        st.text("DataFrame Info:")
        st.text(str(synthetic_df.info()))

        try:
            validate_data(synthetic_df.copy())
            st.success("Data validation successful!")
        except (KeyError, ValueError, TypeError) as e:
            st.error(f"Data validation failed: {e}")

    except TypeError as e:
        st.error(f"Error generating data: {e}")

