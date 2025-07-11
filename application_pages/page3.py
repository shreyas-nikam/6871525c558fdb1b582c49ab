
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_relationship_scatter(df):
    """Generates a scatter plot of Process Complexity vs Residual Risk."""
    if df.empty or 'Process_Complexity' not in df.columns or 'Residual_Risk_Rating' not in df.columns:
        st.warning("Cannot generate scatter plot: missing required data or columns.")
        return None

    risk_mapping = {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4} # Include Very High
    df_plot = df.copy()
    df_plot['Residual_Risk_Rating_Numerical'] = df_plot['Residual_Risk_Rating'].map(risk_mapping)

    if df_plot['Residual_Risk_Rating_Numerical'].isnull().any():
        st.warning("Skipping scatter plot: Residual_Risk_Rating contains values outside expected 'Low', 'Medium', 'High', 'Very High'.")
        return None

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df_plot['Process_Complexity'], df_plot['Residual_Risk_Rating_Numerical'], alpha=0.7)
    ax.set_title('Process Complexity vs Residual Risk Rating', fontsize=14)
    ax.set_xlabel('Process Complexity', fontsize=12)
    ax.set_ylabel('Residual Risk Rating (Numerical)', fontsize=12)
    ax.set_yticks([1, 2, 3, 4]) # Include Very High
    ax.set_yticklabels(['Low', 'Medium', 'High', 'Very High']) # Include Very High
    ax.grid(True)
    plt.tight_layout()
    return fig

def plot_trend_line(df):
    """Generates a line chart showing the trend of average Residual Risk Rating over Assessment Cycles."""
    if df.empty or 'Assessment_Cycle' not in df.columns or 'Residual_Risk_Rating' not in df.columns:
        st.warning("Cannot generate trend plot: missing required data or 'Assessment_Cycle' column.")
        return None

    risk_mapping = {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4} # Include Very High
    df_plot = df.copy()
    df_plot['Residual_Risk_Rating_Numerical'] = df_plot['Residual_Risk_Rating'].map(risk_mapping)

    if df_plot['Residual_Risk_Rating_Numerical'].isnull().any():
        st.warning("Skipping trend plot: Residual_Risk_Rating contains values outside expected 'Low', 'Medium', 'High', 'Very High'.")
        return None

    avg_risk = df_plot.groupby('Assessment_Cycle')['Residual_Risk_Rating_Numerical'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(avg_risk['Assessment_Cycle'], avg_risk['Residual_Risk_Rating_Numerical'], marker='o', linestyle='-', color='skyblue')
    ax.set_title('Trend of Average Residual Risk Rating Over Assessment Cycles', fontsize=14)
    ax.set_xlabel('Assessment Cycle', fontsize=12)
    ax.set_ylabel('Average Residual Risk Rating', fontsize=12)
    ax.grid(True, linestyle='--')
    ax.set_xticks(avg_risk['Assessment_Cycle'])
    ax.set_ylim(0.5, 4.5) # Update y axis limit
    ax.set_yticks([1, 2, 3, 4]) # Update y axis ticks
    ax.set_yticklabels(['Low', 'Medium', 'High', 'Very High']) # Update y axis ticklabels
    plt.tight_layout()
    return fig

def plot_risk_heatmap(df):
    """Generates a heatmap of Inherent Risk vs Control Effectiveness showing Residual Risk."""
    if df.empty or 'Inherent_Risk_Rating' not in df.columns or 'Control_Effectiveness_Rating' not in df.columns or 'Residual_Risk_Rating' not in df.columns:
        st.warning("Cannot generate heatmap: missing required data or columns.")
        return None

    risk_rating_order = ['Low', 'Medium', 'High', 'Very High']
    control_effectiveness_order = ['Low', 'Medium', 'High', 'Very High']

    risk_mapping_numerical = {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4}
    df_plot = df.copy()
    df_plot['Residual_Risk_Rating_Numerical'] = df_plot['Residual_Risk_Rating'].map(risk_mapping_numerical)

    if df_plot['Residual_Risk_Rating_Numerical'].isnull().any():
        st.warning("Skipping heatmap: Residual_Risk_Rating contains values outside expected 'Low', 'Medium', 'High', 'Very High'.")
        return None

    heatmap_data = df_plot.groupby(['Inherent_Risk_Rating', 'Control_Effectiveness_Rating'])['Residual_Risk_Rating_Numerical'].mean().unstack()
    heatmap_data = heatmap_data.reindex(index=[r for r in risk_rating_order if r in heatmap_data.index],
                                        columns=[c for c in control_effectiveness_order if c in heatmap_data.columns])

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(heatmap_data, annot=True, cmap='viridis_r', fmt=".1f", linewidths=.5, ax=ax,
                cbar_kws={'label': 'Average Residual Risk (Numerical)'})

    ax.set_title('Inherent Risk vs Control Effectiveness (Average Residual Risk)', fontsize=14)
    ax.set_xlabel('Control Effectiveness Rating', fontsize=12)
    ax.set_ylabel('Inherent Risk Rating', fontsize=12)
    plt.tight_layout()
    return fig

def run_page3():
    st.header("Visualizations")
    st.markdown("""
    Explore the relationships between different risk factors through interactive visualizations.
    """)

    if 'synthetic_df' not in st.session_state:
        st.warning("Please generate data and calculate residual risk on the previous pages first.")
        return

    synthetic_df = st.session_state['synthetic_df'].copy()

    if synthetic_df is None or synthetic_df.empty:
        st.warning("No data to visualize. Please generate data and calculate residual risk first.")
        return

    st.subheader("Relationship Plot: Process Complexity vs Residual Risk")
    relationship_fig = plot_relationship_scatter(synthetic_df)
    if relationship_fig:
        st.pyplot(relationship_fig)

    if 'Assessment_Cycle' in synthetic_df.columns:
        st.subheader("Trend Plot: Average Residual Risk Rating Over Assessment Cycles")
        trend_fig = plot_trend_line(synthetic_df)
        if trend_fig:
            st.pyplot(trend_fig)

    st.subheader("Aggregated Comparison: Heatmap")
    heatmap_fig = plot_risk_heatmap(synthetic_df)
    if heatmap_fig:
        st.pyplot(heatmap_fig)

if __name__ == "__main__":
    run_page3()
