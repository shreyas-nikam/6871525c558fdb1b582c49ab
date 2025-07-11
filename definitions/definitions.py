import pandas as pd
import numpy as np

def generate_synthetic_data(num_units, has_time_series):
    """Generates a pandas.DataFrame with synthetic operational risk data."""

    if not isinstance(has_time_series, bool):
      raise TypeError("has_time_series must be a boolean")

    # Define possible values for categorical columns
    risk_unit_types = ['Business Unit', 'Department', 'Team']
    risk_ratings = ['Low', 'Medium', 'High', 'Very High']
    control_types = ['Preventative', 'Detective', 'Corrective']

    # Create an empty dictionary to store the data
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

    # Create a pandas DataFrame from the dictionary
    df = pd.DataFrame(data)

    # Add time-series data if requested
    if has_time_series:
        df['Assessment_Cycle'] = np.random.randint(2020, 2024, num_units)

    return df

import pandas as pd

def validate_data(df):
    """Validates DataFrame for expected columns, data types, PK uniqueness, and missing values."""

    expected_columns = ['Risk_Assessment_Unit_ID', 'Risk_Assessment_Unit_Type', 'Inherent_Risk_Rating',
                        'Control_Effectiveness_Rating', 'Control_Type', 'Control_Key_Status',
                        'Process_Complexity', 'Operational_Metric_1', 'Operational_Metric_2']

    # Check for missing columns
    for col in expected_columns:
        if col not in df.columns:
            raise KeyError(f"Missing column: {col}")

    # Check for duplicate Risk_Assessment_Unit_ID values
    if df['Risk_Assessment_Unit_ID'].duplicated().any():
        raise ValueError("Duplicate Risk_Assessment_Unit_ID values found.")

    # Check for missing values
    if df.isnull().any().any():
        raise ValueError("Missing values found in DataFrame.")

    # Check for invalid data types
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
    if not pd.api.types.is_string_dtype(df['Control_Key_Status']):
        raise TypeError("Control_Key_Status should be string.")
    if not pd.api.types.is_numeric_dtype(df['Process_Complexity']):
        raise TypeError("Process_Complexity should be numeric.")
    if not pd.api.types.is_numeric_dtype(df['Operational_Metric_1']):
        raise TypeError("Operational_Metric_1 should be numeric.")
    if not pd.api.types.is_numeric_dtype(df['Operational_Metric_2']):
        raise TypeError("Operational_Metric_2 should be numeric.")

import pandas as pd

def calculate_residual_risk(df, calculation_method):
    """Calculates the residual risk rating based on the specified calculation method."""

    if calculation_method not in ['Basic', 'Weighted']:
        raise ValueError("Invalid calculation_method. Choose 'Basic' or 'Weighted'.")

    if not df.empty:
        # Define risk rating mappings
        risk_ratings = {'Low': 1, 'Medium': 2, 'High': 3}
        control_ratings = {'Ineffective': 1, 'Partially Effective': 2, 'Effective': 3}

        # Validate Inherent Risk Ratings
        for rating in df['Inherent_Risk_Rating'].unique():
            if rating not in risk_ratings:
                raise ValueError(f"Invalid Inherent_Risk_Rating value: {rating}. Allowed values are: Low, Medium, High")

        # Validate Control Effectiveness Ratings
        for rating in df['Control_Effectiveness_Rating'].unique():
            if rating not in control_ratings:
                raise ValueError(f"Invalid Control_Effectiveness_Rating value: {rating}. Allowed values are: Ineffective, Partially Effective, Effective")

        # Calculate Residual Risk Score
        if calculation_method == 'Basic':
            df['Residual_Risk_Score'] = df.apply(
                lambda row: risk_ratings[row['Inherent_Risk_Rating']] - control_ratings[row['Control_Effectiveness_Rating']], axis=1
            )
        elif calculation_method == 'Weighted':
            df['Residual_Risk_Score'] = df.apply(
                lambda row: risk_ratings[row['Inherent_Risk_Rating']] / control_ratings[row['Control_Effectiveness_Rating']], axis=1
            )

        # Define Residual Risk Rating Mapping
        residual_risk_mapping = {
            (3, 'Effective'): 'Low',
            (3, 'Partially Effective'): 'Medium',
            (3, 'Ineffective'): 'High',
            (2, 'Effective'): 'Low',
            (2, 'Partially Effective'): 'Medium',
            (2, 'Ineffective'): 'Medium',
            (1, 'Effective'): 'Low',
            (1, 'Partially Effective'): 'Low',
            (1, 'Ineffective'): 'Medium'
        }
        if calculation_method == 'Basic':
            df['Residual_Risk_Rating'] = df.apply(lambda row:
                                                    'Low' if row['Inherent_Risk_Rating'] == 'Low' and row['Control_Effectiveness_Rating'] == 'Effective' else (
                'Low' if row['Inherent_Risk_Rating'] == 'Medium' and row['Control_Effectiveness_Rating'] == 'Effective' else (
                    'Low' if row['Inherent_Risk_Rating'] == 'Low' and row['Control_Effectiveness_Rating'] == 'Partially Effective' else (
                        'Low' if row['Inherent_Risk_Rating'] == 'Low' and row['Control_Effectiveness_Rating'] == 'Ineffective' else (
                            'Medium' if row['Inherent_Risk_Rating'] == 'Medium' and row['Control_Effectiveness_Rating'] == 'Ineffective' else (
                                'Medium' if row['Inherent_Risk_Rating'] == 'Medium' and row['Control_Effectiveness_Rating'] == 'Partially Effective' else (
                                    'High' if row['Inherent_Risk_Rating'] == 'High' and row['Control_Effectiveness_Rating'] == 'Ineffective' else (
                                        'Medium' if row['Inherent_Risk_Rating'] == 'High' and row['Control_Effectiveness_Rating'] == 'Partially Effective' else 'Low'))))))), axis=1)
        elif calculation_method == 'Weighted':
            df['Residual_Risk_Rating'] = df.apply(lambda row:
                                                    'Low' if row['Inherent_Risk_Rating'] == 'Low' and row['Control_Effectiveness_Rating'] == 'Effective' else (
                'Low' if row['Inherent_Risk_Rating'] == 'Medium' and row['Control_Effectiveness_Rating'] == 'Effective' else (
                    'Low' if row['Inherent_Risk_Rating'] == 'Low' and row['Control_Effectiveness_Rating'] == 'Partially Effective' else (
                        'High' if row['Inherent_Risk_Rating'] == 'High' and row['Control_Effectiveness_Rating'] == 'Ineffective' else (
                            'High' if row['Inherent_Risk_Rating'] == 'Medium' and row['Control_Effectiveness_Rating'] == 'Ineffective' else (
                                'Medium' if row['Inherent_Risk_Rating'] == 'Medium' and row['Control_Effectiveness_Rating'] == 'Partially Effective' else (
                                    'Low' if row['Inherent_Risk_Rating'] == 'High' and row['Control_Effectiveness_Rating'] == 'Effective' else 'Medium')))))), axis=1)


    else:
        df['Residual_Risk_Rating'] = []
        df['Residual_Risk_Score'] = []

    return df

import pandas as pd
import matplotlib.pyplot as plt

def plot_relationship_scatter(df):
    """Generates a scatter plot of Process Complexity vs Residual Risk."""
    if df.empty:
        return

    if 'Process_Complexity' not in df.columns or 'Residual_Risk_Rating' not in df.columns:
        raise KeyError("DataFrame must contain 'Process_Complexity' and 'Residual_Risk_Rating' columns.")

    # Convert Residual_Risk_Rating to numerical values for plotting
    risk_mapping = {'Low': 1, 'Medium': 2, 'High': 3}
    df['Residual_Risk_Rating_Numerical'] = df['Residual_Risk_Rating'].map(risk_mapping)

    # Handle cases where risk levels are not in predefined mapping
    if df['Residual_Risk_Rating_Numerical'].isnull().any():
        raise ValueError("Residual_Risk_Rating must be categorical with levels 'Low', 'Medium', or 'High'.")

    try:
        plt.figure(figsize=(8, 6))
        plt.scatter(df['Process_Complexity'], df['Residual_Risk_Rating_Numerical'])
        plt.title('Process Complexity vs Residual Risk Rating')
        plt.xlabel('Process Complexity')
        plt.ylabel('Residual Risk Rating (Numerical)')
        plt.yticks([1, 2, 3], ['Low', 'Medium', 'High'])  # Map numerical values back to categories
        plt.grid(True)
        plt.show()
    except TypeError as e:
        raise TypeError(f"Ensure 'Process_Complexity' is numeric: {e}")
    except Exception as e:
        raise e

import pandas as pd
import matplotlib.pyplot as plt

def plot_trend_line(df):
    """Generates a line chart showing the trend of average Residual Risk Rating over Assessment Cycles."""

    if df.empty:
        raise Exception("DataFrame is empty")

    if 'Assessment_Cycle' not in df.columns or 'Residual_Risk_Rating' not in df.columns:
        raise KeyError("Required columns ('Assessment_Cycle', 'Residual_Risk_Rating') are missing.")

    if not pd.api.types.is_numeric_dtype(df['Residual_Risk_Rating']):
        raise TypeError("Residual_Risk_Rating must be numeric.")

    # Calculate the average Residual Risk Rating for each Assessment Cycle
    avg_risk = df.groupby('Assessment_Cycle')['Residual_Risk_Rating'].mean()

    # Create the line chart
    plt.figure(figsize=(10, 6))  # Adjust figure size for better visualization
    plt.plot(avg_risk.index, avg_risk.values, marker='o', linestyle='-')
    plt.title('Trend of Average Residual Risk Rating Over Assessment Cycles')
    plt.xlabel('Assessment Cycle')
    plt.ylabel('Average Residual Risk Rating')
    plt.grid(True)  # Add grid for better readability
    plt.xticks(avg_risk.index)  # Ensure all assessment cycles are displayed on x-axis
    plt.tight_layout()  # Adjust layout to prevent labels from overlapping
    plt.show()