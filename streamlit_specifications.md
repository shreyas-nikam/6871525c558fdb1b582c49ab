
# Streamlit Application Requirements Specification: Operational Risk Assessment Simulator

This document outlines the requirements for developing a Streamlit application based on the provided Jupyter Notebook content and user specifications. It details the application's purpose, user interface components, interactive features, and integrates relevant code snippets for a clear development blueprint.

## 1. Application Overview

The **Operational Risk Assessment Simulator** is an interactive Streamlit application designed to provide a hands-on experience in understanding the core concepts of operational risk management. It allows users to simulate various risk scenarios and observe the interplay between inherent risk, control effectiveness, and residual risk.

**Purpose and Objectives:**
*   To enable users to understand and manage operational risk by simulating different risk scenarios.
*   To provide an interactive environment for exploring the relationship between inherent risk, control effectiveness, and residual risk.
*   To facilitate learning about the practical application of operational risk concepts outlined in the PRMIA handbook.

**Learning Outcomes:**
*   Understand the key insights contained in the uploaded document and supporting data.
*   Understand the steps and interactions within the operational risk assessment lifecycle [3].
*   Learn how inherent risk and control effectiveness contribute to residual risk [8].
*   Explore different approaches for defining risk assessment units (functional, process-based, blended) [4].
*   Analyze the impact of various control attributes (preventative vs. detective, key vs. non-key) on risk mitigation [6].

**Features:**
*   **Synthetic Data Generation**: Generates a dataset representing various risk assessment units with attributes like `Inherent_Risk_Rating`, `Control_Effectiveness_Rating`, and other operational metrics.
*   **Interactive Residual Risk Calculation**: Allows users to apply different weighting schemes or scenarios for calculating residual risk (e.g., 'Basic' or 'Weighted'). The basic formula concept is often perceived as:
    $$
    \text{Residual Risk} = f(\text{Inherent Risk}, \text{Control Effectiveness})
    $$
    where $f$ is an additive or weighted function.
*   **Dynamic Visualizations**: Includes interactive plots for:
    *   **Aggregated Comparison**: A heatmap showing `Inherent_Risk_Rating` vs. `Control_Effectiveness_Rating` and the resulting `Residual_Risk_Rating`.
    *   **Relationship Plot**: A scatter plot illustrating the correlation between `Process_Complexity` and `Residual_Risk_Rating`.
    *   **Trend Plot**: A line chart showing the trend of average `Residual_Risk_Rating` over simulated assessment cycles.

**How It Explains the Concept:**
This application demystifies abstract operational risk assessment concepts by providing an interactive environment to manipulate key variables. Users can directly observe how changes in inherent risk or control effectiveness lead to different residual risk profiles, understanding the nuances of residual risk calculation beyond simple subtraction [8]. The various approaches to defining risk assessment units [4] will also be explored through user-selectable configurations.

## 2. User Interface Requirements

The Streamlit application will adopt a clean, intuitive layout to facilitate user interaction and data exploration.

**Layout and Navigation Structure:**
*   A sidebar will house input widgets and controls, allowing users to configure simulation parameters.
*   The main content area will display generated data summaries, data validation results, and interactive visualizations.
*   Sections will be clearly delineated with headings and subheadings, consistent with the notebook's structure.

**Input Widgets and Controls:**
*   **Data Generation Parameters:**
    *   `Number of Risk Assessment Units`: `st.slider` or `st.number_input` (e.g., range 10-500, default 100).
    *   `Include Time Series Data`: `st.checkbox` (default True).
*   **Residual Risk Calculation Method:**
    *   `Calculation Method`: `st.radio` or `st.selectbox` with options 'Basic' and 'Weighted' (default 'Basic').
*   **Dynamic Plotting Options**: (If applicable for advanced filtering/aggregation)
    *   `Filter by Risk Unit Type`: `st.multiselect` for `Risk_Assessment_Unit_Type`.
    *   `Select Assessment Cycle (for Trend Plot)`: `st.multiselect` for `Assessment_Cycle`.

**Visualization Components:**
*   **Data Tables**:
    *   Display `synthetic_df.head()` and `synthetic_df.info()` using `st.dataframe` and `st.write` (for info printout).
*   **Charts and Graphs**:
    *   **Relationship Plot (Scatter)**: Will visualize `Process_Complexity` vs. `Residual_Risk_Rating`.
        *   X-axis: 'Process Complexity', Y-axis: 'Residual Risk Rating (Numerical)'.
        *   Title: 'Process Complexity vs Residual Risk Rating'.
        *   Interactive (zoom, pan, tooltips) using `Altair`. Color-blind friendly palette will be used.
    *   **Trend Plot (Line)**: Will visualize average `Residual_Risk_Rating` over `Assessment_Cycle`.
        *   X-axis: 'Assessment Cycle', Y-axis: 'Average Residual Risk Rating'.
        *   Title: 'Trend of Average Residual Risk Rating Over Assessment Cycles'.
        *   Interactive using `Altair`.
    *   **Aggregated Comparison (Heatmap)**: Will show the aggregated `Residual_Risk_Rating` distribution across `Inherent_Risk_Rating` and `Control_Effectiveness_Rating`.
        *   X-axis: 'Inherent Risk Rating', Y-axis: 'Control Effectiveness Rating'.
        *   Color encoding for `Residual_Risk_Rating` (e.g., numerical average or count of "High" risks).
        *   Title: 'Aggregated Residual Risk Rating Heatmap'.
        *   Interactive using `Altair`.

**Interactive Elements and Feedback Mechanisms:**
*   All plots will be interactive, enabling zooming, panning, and detailed tooltips on hover.
*   Error messages from data validation (`KeyError`, `ValueError`, `TypeError`) will be displayed prominently using `st.error`.
*   Success messages will be displayed using `st.success` or `st.info`.
*   Help text or tooltips (`st.help` or `help` parameter in widgets) will be provided for each control/input to describe its function.

## 3. Additional Requirements

**Real-time Updates and Responsiveness:**
*   The application will re-run calculations and update visualizations dynamically as users adjust input parameters in the sidebar. This leverages Streamlit's built-in re-execution model.
*   The application must execute end-to-end within a reasonable timeframe (target under 5 minutes on mid-spec laptop).

**Annotation and Tooltip Specifications:**
*   Each input widget (sliders, dropdowns, checkboxes) will include descriptive help text or tooltips to guide the user on its purpose and impact on the simulation.
*   Visualizations will feature interactive tooltips on data points to display specific values (e.g., `Inherent_Risk_Rating`, `Control_Effectiveness_Rating`, `Residual_Risk_Rating`, `Process_Complexity`, `Assessment_Cycle`).
*   Clear titles, labeled axes, and legends will be provided for all charts, with a color-blind-friendly palette.

## 4. Notebook Content and Code Requirements

This section details how the core logic and functions from the Jupyter Notebook will be integrated into the Streamlit application.

### 4.1. Application Setup and Dependencies

The Streamlit application will require the following libraries:
```python
# In a requirements.txt file or at the top of the Streamlit app
# pandas
# numpy
# matplotlib
# altair
# streamlit

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt # For interactive and color-blind friendly plots
```

### 4.2. Data Generation

**Business Value:** Synthetic data generation is critical for model development, scenario analysis, and training in operational risk management without exposing sensitive real-world data. It mimics statistical properties of actual data, enabling safe experimentation.

**Technical Implementation:** The `generate_synthetic_data` function creates a `pandas.DataFrame` with various operational risk attributes.
**Streamlit Integration:**
*   Users will control `num_units` and `has_time_series` via sidebar widgets.
*   The generated DataFrame and its metadata (`.head()`, `.info()`) will be displayed.

**Formula:**
The synthetic data generation process is summarized by:
$$
\text{Synthetic Data} = \{ \text{randomly sampled attributes for each unit} \}
$$
where each attribute is independently generated based on predefined distributions or lists of possible values.

**Code:**
```python
# Function from Jupyter Notebook
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

# Streamlit usage (example)
# num_units = st.sidebar.slider("Number of Risk Units", 10, 500, 100)
# has_time_series = st.sidebar.checkbox("Include Time Series Data", True)
# synthetic_df = generate_synthetic_data(num_units, has_time_series)
# st.subheader("Generated Synthetic Data")
# st.dataframe(synthetic_df.head())
# st.text("DataFrame Info:")
# st.text(synthetic_df.info()) # This prints to console, need to capture for display
```

### 4.3. Data Validation

**Business Value:** Data validation ensures accuracy, consistency, and reliability, minimizing errors, improving data quality, and aiding regulatory compliance for informed decision-making in risk management.

**Technical Implementation:** The `validate_data` function performs checks on expected columns, data types, primary key uniqueness, and missing values.
**Streamlit Integration:**
*   The validation will be executed after data generation.
*   Success or failure messages will be displayed using `st.success` or `st.error` blocks.

**Formula:**
The validation process can be summarized as follows:
$$
\text{Data Validation} = \{ \text{Column Presence} \} \cap \{ \text{Data Type Correctness} \} \cap \{ \text{PK Uniqueness} \} \cap \{ \text{No Missing Values} \}
$$
The function raises an exception if any of these conditions are not met.

**Code:**
```python
# Function from Jupyter Notebook
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

    # Note: 'Control_Key_Status' is boolean in original code but expected string in validation.
    # Adjusting validation to match synthetic data generation's actual output which is boolean.
    # This ensures consistency and prevents validation failure on valid synthetic data.
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
    if not pd.api.types.is_bool_dtype(df['Control_Key_Status']): # Adjusted from string to bool
        raise TypeError("Control_Key_Status should be boolean.")
    if not pd.api.types.is_numeric_dtype(df['Process_Complexity']):
        raise TypeError("Process_Complexity should be numeric.")
    if not pd.api.types.is_numeric_dtype(df['Operational_Metric_1']):
        raise TypeError("Operational_Metric_1 should be numeric.")
    if not pd.api.types.is_numeric_dtype(df['Operational_Metric_2']):
        raise TypeError("Operational_Metric_2 should be numeric.")

# Streamlit usage (example)
# try:
#     validate_data(synthetic_df.copy()) # Pass a copy to avoid SettingWithCopyWarning later
#     st.success("Data validation successful!")
# except (KeyError, ValueError, TypeError) as e:
#     st.error(f"Data validation failed: {e}")
```

### 4.4. Residual Risk Calculation

**Business Value:** Calculating residual risk provides a quantitative measure of remaining risk after controls, enabling prioritization of mitigation, evaluation of control effectiveness, informed decision-making, and regulatory compliance.

**Technical Implementation:** The `calculate_residual_risk` function computes residual risk based on 'Basic' (subtractive) or 'Weighted' (divisive) methods, mapping ratings to numerical scores and then back to categorical ratings.
**Streamlit Integration:**
*   Users will select the `calculation_method` from a sidebar widget.
*   The function will modify the DataFrame in place or return a new one with 'Residual_Risk_Score' and 'Residual_Risk_Rating' columns.
*   The updated DataFrame head will be displayed.

**Formula:**
The basic formula for residual risk calculation is:
$$
\text{Residual Risk} = f(\text{Inherent Risk}, \text{Control Effectiveness})
$$
where $f$ can be either an additive function (Basic method) or a multiplicative/weighted function (Weighted method).

**Code:**
```python
# Function from Jupyter Notebook (Modified for consistency in Control_Effectiveness_Rating, as 'Ineffective' etc. are not in synthetic data)
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

# Streamlit usage (example)
# calculation_method = st.sidebar.radio("Select Residual Risk Calculation Method", ('Basic', 'Weighted'))
# synthetic_df_calculated = calculate_residual_risk(synthetic_df, calculation_method)
# st.subheader(f"Data with Residual Risk ({calculation_method} Method)")
# st.dataframe(synthetic_df_calculated.head())
```

### 4.5. Dynamic Visualizations

**Business Value:** Visualizations translate complex data into actionable insights, enabling enhanced risk monitoring, improved communication, proactive decision-making, and better resource allocation.

**General Implementation Note:** The application will prioritize `Altair` for interactive plots due to its native Streamlit integration, interactivity, and color-blind friendly palettes. `Matplotlib` will be used as a static fallback if `Altair` is not suitable for a specific plot type or for comparison.

#### 4.5.1. Relationship Plot: Process Complexity vs. Residual Risk

**Technical Implementation:** The `plot_relationship_scatter` function (adapted for Altair) generates a scatter plot to visualize the relationship between 'Process_Complexity' and `Residual_Risk_Rating_Numerical`.
**Streamlit Integration:**
*   Display the scatter plot using `st.altair_chart`.
*   Tooltips will show `Process_Complexity`, `Inherent_Risk_Rating`, `Control_Effectiveness_Rating`, and `Residual_Risk_Rating`.

**Formula:**
The scatter plot visualizes the relationship as:
$$
\text{Scatter Plot} = \text{Points}(\text{Process Complexity}, \text{Residual Risk Rating (Numerical)})
$$
where each point represents a risk assessment unit.

**Code (Adapted for Altair):**
```python
# Function adapted for Altair for interactive plotting
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

# Streamlit usage (example)
# st.subheader("Process Complexity vs Residual Risk")
# scatter_chart = plot_relationship_scatter_altair(synthetic_df_calculated)
# if scatter_chart:
#     st.altair_chart(scatter_chart, use_container_width=True)
```

#### 4.5.2. Trend Plot: Average Residual Risk Rating Over Assessment Cycles

**Business Value:** Trend analysis provides insights into emerging risks, control effectiveness over time, improved risk forecasting, and supports continuous improvement in risk management practices.

**Technical Implementation:** The `plot_trend_line` function (adapted for Altair) computes the average `Residual_Risk_Rating` for each `Assessment_Cycle` and visualizes the trend.
**Streamlit Integration:**
*   Requires `has_time_series` to be True.
*   Display the line chart using `st.altair_chart`.
*   Tooltips will show `Assessment_Cycle` and `Average Residual Risk Rating`.

**Formula:**
The line chart visualizes the trend as:
$$
\text{Line Chart} = \text{Line}(\text{Assessment Cycle}, \text{Average Residual Risk Rating})
$$
where the line connects the average residual risk rating for each assessment cycle.

**Code (Adapted for Altair):**
```python
# Function adapted for Altair for interactive plotting
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

# Streamlit usage (example)
# if has_time_series:
#     st.subheader("Trend of Average Residual Risk Rating")
#     trend_chart = plot_trend_line_altair(synthetic_df_calculated)
#     if trend_chart:
#         st.altair_chart(trend_chart, use_container_width=True)
```

#### 4.5.3. Aggregated Comparison: Heatmap

**Technical Implementation:** This plot will aggregate the data to show the distribution of residual risk ratings based on combinations of inherent risk and control effectiveness. It will require a new function to prepare and visualize the data for a heatmap.
**Streamlit Integration:**
*   Display the heatmap using `st.altair_chart`.
*   Tooltips will show the count of units for each combination.

**Formula:**
The heatmap visualizes the aggregated relationship as:
$$
\text{Heatmap} = \text{Count}(\text{Inherent Risk Rating}, \text{Control Effectiveness Rating}, \text{Residual Risk Rating})
$$
where the color intensity represents the aggregation (e.g., count of units or average residual risk score) within each cell.

**Code (New Function for Heatmap using Altair):**
```python
import altair as alt

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

# Streamlit usage (example)
# st.subheader("Aggregated Residual Risk Heatmap")
# heatmap_chart = plot_residual_risk_heatmap_altair(synthetic_df_calculated)
# if heatmap_chart:
#     st.altair_chart(heatmap_chart, use_container_width=True)
```
