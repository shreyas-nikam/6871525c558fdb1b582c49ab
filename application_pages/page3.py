
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def plot_relationship_scatter_altair(df):
    """Generates an interactive scatter plot of Process Complexity vs Residual Risk using Altair."""
    if df.empty:
        st.warning("No data to plot for Process Complexity vs Residual Risk.")
        return None

    if 'Process_Complexity' not in df.columns or 'Residual_Risk_Rating' not in df.columns:
        st.error("DataFrame must contain 'Process_Complexity' and 'Residual_Risk_Rating' columns for scatter plot.")
        return None

    risk_mapping = {'Low': 1, 'Medium': 2, 'High': 3}
    df['Residual_Risk_Rating_Numerical'] = df['Residual_Risk_Rating'].map(risk_mapping)

    if df['Residual_Risk_Rating_Numerical'].isnull().any():
        st.error("Residual_Risk_Rating must be categorical with levels 'Low', 'Medium', or 'High'.")
        return None

    chart = alt.Chart(df).mark_circle(size=60).encode(
        x=alt.X('Process_Complexity', axis=alt.Axis(title='Process Complexity')),
        y=alt.Y('Residual_Risk_Rating_Numerical', axis=alt.Axis(title='Residual Risk Rating (Numerical)',
                                                                 values=[1, 2, 3],
                                                                 labelExpr="datum.value == 1 ? 'Low' : datum.value == 2 ? 'Medium' : 'High'")),
        tooltip=[
            alt.Tooltip('Risk_Assessment_Unit_ID'),
            alt.Tooltip('Inherent_Risk_Rating'),
            alt.Tooltip('Control_Effectiveness_Rating'),
            alt.Tooltip('Residual_Risk_Rating'),
            alt.Tooltip('Process_Complexity')
        ],
        color=alt.Color('Residual_Risk_Rating', scale=alt.Scale(domain=['Low', 'Medium', 'High'], range=['#1f77b4', '#ff7f0e', '#d62728']), legend=alt.Legend(title="Residual Risk"))
    ).properties(
        title='Process Complexity vs Residual Risk Rating'
    ).interactive()

    return chart

def plot_trend_line_altair(df):
    """Generates an interactive line chart showing the trend of average Residual Risk Rating over Assessment Cycles using Altair."""
    if df.empty:
        st.warning("No data to plot for Residual Risk Trend.")
        return None

    if 'Assessment_Cycle' not in df.columns or 'Residual_Risk_Rating' not in df.columns:
        st.info("Time-series data (Assessment_Cycle) is required for the Trend Plot. Please enable 'Include Time Series Data'.")
        return None

    risk_mapping = {'Low': 1, 'Medium': 2, 'High': 3}
    df['Residual_Risk_Rating_Numerical'] = df['Residual_Risk_Rating'].map(risk_mapping)

    if df['Residual_Risk_Rating_Numerical'].isnull().any():
        st.error("Residual_Risk_Rating must be categorical with levels 'Low', 'Medium', or 'High'.")
        return None

    # Calculate the average Residual Risk Rating for each Assessment Cycle
    avg_risk = df.groupby('Assessment_Cycle')['Residual_Risk_Rating_Numerical'].mean().reset_index()

    chart = alt.Chart(avg_risk).mark_line(point=True).encode(
        x=alt.X('Assessment_Cycle:O', axis=alt.Axis(title='Assessment Cycle', format="d")), # :O for ordinal to show all years
        y=alt.Y('Residual_Risk_Rating_Numerical', axis=alt.Axis(title='Average Residual Risk Rating (Numerical)',
                                                                 values=[1, 2, 3],
                                                                 labelExpr="datum.value == 1 ? 'Low' : datum.value == 2 ? 'Medium' : 'High'")),
        tooltip=[alt.Tooltip('Assessment_Cycle', title='Cycle'), alt.Tooltip('Residual_Risk_Rating_Numerical', title='Avg Risk', format=".2f")]
    ).properties(
        title='Trend of Average Residual Risk Rating Over Assessment Cycles'
    ).interactive()

    return chart

def plot_residual_risk_heatmap_altair(df):
    """Generates an interactive heatmap of Inherent Risk vs Control Effectiveness showing Residual Risk."""
    if df.empty:
        st.warning("No data to plot for Residual Risk Heatmap.")
        return None

    required_cols = ['Inherent_Risk_Rating', 'Control_Effectiveness_Rating', 'Residual_Risk_Rating']
    for col in required_cols:
        if col not in df.columns:
            st.error(f"Missing column: {col} for Residual Risk Heatmap.")
            return None

    # Define the order for categorical axes for better readability
    inherent_order = ['Low', 'Medium', 'High', 'Very High']
    control_order = ['Low', 'Medium', 'High'] # Assuming 'Low' control effectiveness is bad, 'High' is good

    # Create a numerical mapping for Residual_Risk_Rating for color encoding
    residual_risk_numerical_map = {'Low': 1, 'Medium': 2, 'High': 3}
    df['Residual_Risk_Rating_Numerical'] = df['Residual_Risk_Rating'].map(residual_risk_numerical_map)

    # Aggregate data for the heatmap
    # We can show count of units, or average residual risk numerical score
    heatmap_data = df.groupby(['Inherent_Risk_Rating', 'Control_Effectiveness_Rating']).agg(
        unit_count=('Risk_Assessment_Unit_ID', 'count'),
        avg_residual_score=('Residual_Risk_Rating_Numerical', 'mean')
    ).reset_index()

    # Define color scale for average residual risk (e.g., green for low, red for high)
    # Using a sequential multi-hue scale suitable for color-blindness (e.g., 'viridis')
    color_scale = alt.Scale(domain=[1, 3], range='viridis', type='linear') # Viridis for sequential data

    chart = alt.Chart(heatmap_data).mark_rect().encode(
        x=alt.X('Inherent_Risk_Rating:O', sort=inherent_order, axis=alt.Axis(title='Inherent Risk Rating')),
        y=alt.Y('Control_Effectiveness_Rating:O', sort=control_order, axis=alt.Axis(title='Control Effectiveness Rating')),
        color=alt.Color('avg_residual_score:Q', scale=color_scale, legend=alt.Legend(title="Avg. Residual Risk Score")),
        tooltip=[
            alt.Tooltip('Inherent_Risk_Rating'),
            alt.Tooltip('Control_Effectiveness_Rating'),
            alt.Tooltip('unit_count', title='Number of Units'),
            alt.Tooltip('avg_residual_score', title='Avg. Residual Score', format=".2f")
        ]
    ).properties(
        title='Aggregated Residual Risk by Inherent Risk & Control Effectiveness'
    )

    # Add text labels for unit count
    text = chart.mark_text().encode(
        x=alt.X('Inherent_Risk_Rating:O', sort=inherent_order),
        y=alt.Y('Control_Effectiveness_Rating:O', sort=control_order),
        text=alt.Text('unit_count', format='.0f'),
        color=alt.value('black') # Make text black for readability
    )

    return (chart + text).interactive()

def run_page3():
    st.header("Visualizations")

    if 'synthetic_df' not in st.session_state:
        st.warning("Please generate and validate data on the 'Data Generation and Validation' page first.")
        return

    synthetic_df = st.session_state['synthetic_df']
    
    synthetic_df_calculated = synthetic_df.copy()
    if 'Residual_Risk_Rating' not in synthetic_df_calculated.columns:
        st.warning("Please calculate Residual Risk first on the 'Residual Risk Calculation' page.")
        return
    
    has_time_series = st.session_state.get('has_time_series', False) # Use get to provide a default value

    st.subheader("Process Complexity vs Residual Risk")
    scatter_chart = plot_relationship_scatter_altair(synthetic_df_calculated)
    if scatter_chart:
        st.altair_chart(scatter_chart, use_container_width=True)

    if has_time_series:
        st.subheader("Trend of Average Residual Risk Rating")
        trend_chart = plot_trend_line_altair(synthetic_df_calculated)
        if trend_chart:
            st.altair_chart(trend_chart, use_container_width=True)

    st.subheader("Aggregated Residual Risk Heatmap")
    heatmap_chart = plot_residual_risk_heatmap_altair(synthetic_df_calculated)
    if heatmap_chart:
        st.altair_chart(heatmap_chart, use_container_width=True)
