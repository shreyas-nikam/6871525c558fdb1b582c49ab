
import streamlit as st
import pandas as pd
import numpy as np

def calculate_residual_risk(df, calculation_method):
    """Calculates the residual risk rating based on the specified calculation method."""
    if calculation_method not in ['Basic', 'Weighted']:
        raise ValueError("Invalid calculation_method. Choose 'Basic' or 'Weighted'.")

    # Map the four Inherent_Risk_Rating levels to numerical scores 1-4 for calculation
    # And map Control_Effectiveness_Rating (which is 'Low', 'Medium', 'High' in synthetic data) to 1-3.
    # This addresses the discrepancy between synthetic data 'Control_Effectiveness_Rating' and the function's expected 'Ineffective', etc.
    inherent_risk_score_map = {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4}
    control_effectiveness_score_map = {'Low': 1, 'Medium': 2, 'High': 3} # Assuming 'Low' means less effective, 'High' means more.

    df_copy = df.copy() # Work on a copy to avoid SettingWithCopyWarning

    # Validate and map Inherent Risk Ratings
    df_copy['Inherent_Risk_Score'] = df_copy['Inherent_Risk_Rating'].map(inherent_risk_score_map)
    if df_copy['Inherent_Risk_Score'].isnull().any():
        invalid_ratings = df_copy[df_copy['Inherent_Risk_Score'].isnull()]['Inherent_Risk_Rating'].unique()
        raise ValueError(f"Invalid Inherent_Risk_Rating values: {invalid_ratings}. Allowed values are: {list(inherent_risk_score_map.keys())}")

    # Validate and map Control Effectiveness Ratings
    # This is a crucial adjustment: The synthetic data generates 'Low', 'Medium', 'High' for Control_Effectiveness_Rating.
    # The original calculate_residual_risk function expects 'Ineffective', 'Partially Effective', 'Effective'.
    # We must either change synthetic data or change the mapping here. For this spec, changing mapping here.
    df_copy['Control_Effectiveness_Score'] = df_copy['Control_Effectiveness_Rating'].map(control_effectiveness_score_map)
    if df_copy['Control_Effectiveness_Score'].isnull().any():
        invalid_ratings = df_copy[df_copy['Control_Effectiveness_Score'].isnull()]['Control_Effectiveness_Rating'].unique()
        raise ValueError(f"Invalid Control_Effectiveness_Rating values: {invalid_ratings}. Allowed values are: {list(control_effectiveness_score_map.keys())}")


    if calculation_method == 'Basic':
        # Inherent_Risk_Score - Control_Effectiveness_Score
        # Higher score = higher risk
        df_copy['Residual_Risk_Score'] = df_copy['Inherent_Risk_Score'] - df_copy['Control_Effectiveness_Score']
        # Map scores to ratings: Lower score means lower residual risk
        # This mapping is conceptual and needs refinement based on desired range and granularity.
        # For simplicity, let's define thresholds for -2, -1, 0, 1, 2, 3 scores.
        # Inherent scores (1-4), Control scores (1-3).
        # Basic min score: 1-3 = -2 (Low Inherent, High Control)
        # Basic max score: 4-1 = 3 (Very High Inherent, Low Control)
        def map_basic_residual(score):
            if score <= 0: # e.g., Low-Effective (1-3=-2), Medium-Effective (2-3=-1), High-High (3-3=0)
                return 'Low'
            elif score == 1: # e.g., Medium-Low (2-1=1), High-Medium (3-2=1)
                return 'Medium'
            else: # score >= 2 e.g., High-Low (3-1=2), Very High-Low (4-1=3), Very High-Medium (4-2=2)
                return 'High'
        df_copy['Residual_Risk_Rating'] = df_copy['Residual_Risk_Score'].apply(map_basic_residual)

    elif calculation_method == 'Weighted':
        # Inherent_Risk_Score / Control_Effectiveness_Score
        # Higher ratio = higher risk
        df_copy['Residual_Risk_Score'] = df_copy['Inherent_Risk_Score'] / df_copy['Control_Effectiveness_Score']
        # Map scores to ratings: Lower score means lower residual risk
        # Weighted min score: 1/3 = 0.33 (Low Inherent, High Control)
        # Weighted max score: 4/1 = 4.0 (Very High Inherent, Low Control)
        def map_weighted_residual(score):
            if score <= 1.0: # e.g., 1/3, 1/2, 1/1, 2/2, 3/3
                return 'Low'
            elif score <= 2.0: # e.g., 2/1, 3/2, 4/2
                return 'Medium'
            else: # score > 2.0 e.g., 3/1, 4/1
                return 'High'
        df_copy['Residual_Risk_Rating'] = df_copy['Residual_Risk_Score'].apply(map_weighted_residual)

    return df_copy.drop(columns=['Inherent_Risk_Score', 'Control_Effectiveness_Score'])

def run_page2():
    st.header("Residual Risk Calculation")

    if 'synthetic_df' not in st.session_state:
        st.warning("Please generate data on the 'Data Generation and Validation' page first.")
        return

    synthetic_df = st.session_state['synthetic_df']

    calculation_method = st.radio("Select Residual Risk Calculation Method", ('Basic', 'Weighted'))

    try:
        synthetic_df_calculated = calculate_residual_risk(synthetic_df, calculation_method)
        st.subheader(f"Data with Residual Risk ({calculation_method} Method)")
        st.dataframe(synthetic_df_calculated.head())
        
        # Store the calculated data in session state for page3
        st.session_state['synthetic_df_calculated'] = synthetic_df_calculated
    except ValueError as e:
        st.error(f"Error calculating residual risk: {e}")
