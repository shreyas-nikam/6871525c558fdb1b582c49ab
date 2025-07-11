
import streamlit as st
import pandas as pd
import numpy as np

def calculate_residual_risk(df, calculation_method):
    """Calculates the residual risk rating based on the specified calculation method."""
    if df.empty:
        df['Residual_Risk_Score'] = []
        df['Residual_Risk_Rating'] = []
        return df

    if calculation_method not in ['Basic', 'Weighted']:
        raise ValueError("Invalid calculation_method. Choose 'Basic' or 'Weighted'.")

    risk_ratings_to_numeric = {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4}
    control_ratings_to_score = {'Low': 3, 'Medium': 2, 'High': 1, 'Very High': 0.5}

    df['Inherent_Risk_Numeric'] = df['Inherent_Risk_Rating'].map(risk_ratings_to_numeric)
    if df['Inherent_Risk_Numeric'].isnull().any():
        invalid_ir = df[df['Inherent_Risk_Numeric'].isnull()]['Inherent_Risk_Rating'].unique()
        raise ValueError(f"Invalid Inherent_Risk_Rating value(s): {invalid_ir}. Allowed values are: Low, Medium, High, Very High")

    df['Control_Effectiveness_Score'] = df['Control_Effectiveness_Rating'].map(control_ratings_to_score)
    if df['Control_Effectiveness_Score'].isnull().any():
        invalid_ce = df[df['Control_Effectiveness_Score'].isnull()]['Control_Effectiveness_Rating'].unique()
        raise ValueError(f"Invalid Control_Effectiveness_Rating value(s): {invalid_ce}. Allowed values are: Low, Medium, High, Very High (interpreted as Effective to Ineffective)")

    if calculation_method == 'Basic':
        df['Residual_Risk_Score'] = df['Inherent_Risk_Numeric'] - df['Control_Effectiveness_Score']
    elif calculation_method == 'Weighted':
        df['Residual_Risk_Score'] = df['Inherent_Risk_Numeric'] / df['Control_Effectiveness_Score'].replace(0, 0.001)

    min_score = df['Residual_Risk_Score'].min()
    max_score = df['Residual_Risk_Score'].max()
    score_range = max_score - min_score

    if score_range > 0:
        low_threshold = min_score + 0.33 * score_range
        medium_threshold = min_score + 0.66 * score_range
    else:
        low_threshold = min_score
        medium_threshold = min_score

    def map_score_to_rating(score):
        if score <= low_threshold:
            return 'Low'
        elif score <= medium_threshold:
            return 'Medium'
        else:
            return 'High'

    df['Residual_Risk_Rating'] = df['Residual_Risk_Score'].apply(map_score_to_rating)
    df = df.drop(columns=['Inherent_Risk_Numeric', 'Control_Effectiveness_Score'])

    return df

def run_page2():
    st.header("Risk Calculation")
    st.markdown("""
    Calculate the residual risk based on the inherent risk and control effectiveness. Choose the calculation method to see the impact on the residual risk scores and ratings.
    The basic formula for residual risk calculation is:
    $$\text{Residual Risk} = f(\text{Inherent Risk}, \text{Control Effectiveness})$$
    where $f$ can be either an additive function (Basic method) or a multiplicative/weighted function (Weighted method). The choice of method should reflect the organization's specific approach to risk assessment and the relative importance of controls in mitigating inherent risks.
    """)

    calculation_method = st.sidebar.radio("Calculation Method", options=['Basic', 'Weighted'], help="Choose the formula for calculating Residual Risk: 'Basic' (Inherent - Control) or 'Weighted' (Inherent / Control).")

    # Use a session state to store the dataframe from page 1
    if 'synthetic_df' not in st.session_state:
        st.warning("Please generate data on the 'Data Generation and Validation' page first.")
        return

    synthetic_df = st.session_state['synthetic_df'].copy()

    if synthetic_df is None or synthetic_df.empty:
        st.warning("No data to calculate residual risk. Please generate data first.")
        return

    try:
        residual_risk_df = calculate_residual_risk(synthetic_df, calculation_method)
        st.subheader("Residual Risk Results")
        st.dataframe(residual_risk_df)
        # Store the updated dataframe with residual risk in session state for other pages
        st.session_state['synthetic_df'] = residual_risk_df
    except Exception as e:
        st.error(f"Risk calculation failed: {e}")

if __name__ == "__main__":
    run_page2()
