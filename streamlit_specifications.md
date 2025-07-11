
# Streamlit Application Requirements Specification

## 1. Application Overview

The Operational Risk Assessment Simulator Streamlit application aims to provide an interactive platform for users to understand and explore the fundamental concepts of operational risk assessment. It simulates the relationship between inherent risk, control effectiveness, and the resulting residual risk within a hypothetical organizational context. This application serves as an educational tool for risk managers, students, and professionals, offering a hands-on approach to managing operational risk, which is vital for maintaining financial stability, ensuring regulatory compliance, and enhancing overall organizational resilience.

**Key Objectives:**
*   **Understand Operational Risk Lifecycle**: Illustrate the iterative process of identifying, assessing, and monitoring operational risk as outlined in PRMIA guidelines [3].
*   **Explore Risk Components**: Demonstrate how inherent risk and control effectiveness interact to determine residual risk [8].
*   **Simulate Scenarios**: Allow users to apply different weighting schemes for residual risk calculation and observe the impact.
*   **Visualize Insights**: Provide dynamic visualizations to highlight trends, relationships, and aggregated comparisons in risk data [8].

## 2. User Interface Requirements

### 2.1 Layout and Navigation Structure
The application will feature a clear, intuitive layout.
*   **Sidebar**: Will house all input widgets and controls for data generation, validation, and risk calculation.
*   **Main Content Area**: Dedicated to displaying narrative descriptions, data tables, and interactive visualizations.
*   **Sections**: The main content area will be organized into logical sections corresponding to data generation, validation, risk calculation, and visualization, with clear headings.

### 2.2 Input Widgets and Controls
The sidebar will contain interactive widgets to allow users to manipulate simulation parameters and analysis settings:
*   **Data Generation Controls**:
    *   **Number of Risk Units**: A slider or numeric input (`st.slider` or `st.number_input`) to specify `num_units` for synthetic data generation.
        *   *Help Text*: "Adjust the number of hypothetical risk assessment units to simulate."
    *   **Include Time Series Data**: A checkbox (`st.checkbox`) to toggle `has_time_series` for enabling or disabling the generation of time-series data.
        *   *Help Text*: "Check to include 'Assessment_Cycle' data, enabling the trend plot."
*   **Residual Risk Calculation Controls**:
    *   **Calculation Method**: A radio button or selectbox (`st.radio` or `st.selectbox`) allowing selection between `'Basic'` and `'Weighted'` methods for residual risk calculation.
        *   *Help Text*: "Choose the formula for calculating Residual Risk: 'Basic' (Inherent - Control) or 'Weighted' (Inherent / Control)."
*   **Data Upload (Optional but Recommended)**: A file uploader (`st.file_uploader`) to allow users to upload their own CSV data for analysis.
    *   *Help Text*: "Upload your own CSV file for operational risk analysis. (Optional)"

### 2.3 Visualization Components
The main content area will display the following visual components:
*   **Data Tables**:
    *   Initial synthetic data display.
    *   Dataframe with calculated `Residual_Risk_Score` and `Residual_Risk_Rating`.
*   **Core Visuals**:
    *   **Relationship Plot (Scatter Plot)**: Visualizing `Process_Complexity` vs. `Residual_Risk_Rating`.
    *   **Trend Plot (Line Chart)**: Showing the trend of average `Residual_Risk_Rating` over `Assessment_Cycle` (only if time series data is enabled).
    *   **Aggregated Comparison (Heatmap)**: A heatmap illustrating the relationship between `Inherent_Risk_Rating`, `Control_Effectiveness_Rating`, and the resulting `Residual_Risk_Rating` (as described in the "Features" section of the notebook overview, requiring custom implementation).

### 2.4 Interactive Elements and Feedback Mechanisms
*   **Dynamic Updates**: All charts and tables will automatically update as users change input parameters in the sidebar.
*   **Validation Feedback**: Clear messages (e.g., `st.success`, `st.error`) will inform users about data validation outcomes, including any errors (missing columns, duplicate IDs, missing values, incorrect data types).
*   **Tooltips/Inline Help**: Inline help text or tooltips will be provided for all interactive controls to guide users.
*   **Styling**: All visualizations will adhere to the "Style & usability" requirements from the user requirements: color-blind-friendly palette, font size $\ge 12$ pt, clear titles, labeled axes, and legends.

## 3. Additional Requirements

### 3.1 Real-time Updates and Responsiveness
The Streamlit application will be designed for immediate responsiveness. Changes to input widgets will trigger re-execution of relevant code sections and update visualizations in near real-time, providing an interactive and fluid user experience.

### 3.2 Annotation and Tooltip Specifications
As specified in the user requirements, every input control (sliders, checkboxes, radio buttons, etc.) will be accompanied by concise inline help text or tooltips to explain its purpose and impact on the analysis. This will enhance the learning experience by providing contextual information directly within the UI.

### 3.3 Performance
The application will optimize data generation, validation, and visualization processes to ensure it runs efficiently on a mid-spec laptop (8 GB RAM) and completes end-to-end execution in fewer than 5 minutes. This will involve using efficient Pandas operations and limiting the complexity of synthetic data generation for demonstration purposes.

## 4. Notebook Content and Code Requirements

This section details the functions extracted from the Jupyter Notebook and how they will be integrated into the Streamlit application.

### 4.1 Required Libraries
The application will utilize the following Python libraries:
```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # Recommended for heatmap and better visual styling
```

### 4.2 Data Generation
**Description**: This component generates a synthetic dataset to simulate various operational risk assessment units.
**Business Value**: Provides a realistic, yet artificial, dataset for model development, scenario analysis, and training without relying on sensitive real-world data. The synthetic data generation process is summarized by:
$$
\text{Synthetic Data} = \{ \text{randomly sampled attributes for each unit} \}
$$
where each attribute is independently generated based on predefined distributions or lists of possible values.

**Extracted Code**:
```python
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
```
**Streamlit Integration**:
*   Place `num_units` as `st.slider` and `has_time_series` as `st.checkbox` in the sidebar.
*   Call `generate_synthetic_data` using these inputs.
*   Display the generated `synthetic_df` using `st.dataframe` or `st.table`.
*   Include the narrative and business value markdown in the main content area using `st.markdown`.

### 4.3 Data Validation
**Description**: This component performs a series of checks on the generated (or uploaded) DataFrame to ensure data quality and integrity.
**Business Value**: Ensures that data used for analysis is accurate, consistent, and reliable, minimizing errors and supporting informed decision-making. The validation process can be summarized as follows:
$$
\text{Data Validation} = \{ \text{Column Presence} \} \cap \{ \text{Data Type Correctness} \} \cap \{ \text{PK Uniqueness} \} \cap \{ \text{No Missing Values} \}
$$
The function raises an exception if any of these conditions are not met.

**Extracted Code**:
```python
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

    # Modified to accept boolean for 'Control_Key_Status' as generated data uses boolean
    # And to map "Very High" to a numerical value in Inherent/Control Risk Ratings if needed later
    if not pd.api.types.is_numeric_dtype(df['Risk_Assessment_Unit_ID']):
        raise TypeError("Risk_Assessment_Unit_ID should be numeric.")
    if not pd.api.types.is_string_dtype(df['Risk_Assessment_Unit_Type']):
        raise TypeError("Risk_Assessment_Unit_Type should be string.")
    # Assuming 'Inherent_Risk_Rating' and 'Control_Effectiveness_Rating' are strings like 'Low', 'Medium', 'High', 'Very High'
    if not pd.api.types.is_string_dtype(df['Inherent_Risk_Rating']):
        raise TypeError("Inherent_Risk_Rating should be string.")
    if not pd.api.types.is_string_dtype(df['Control_Effectiveness_Rating']):
        raise TypeError("Control_Effectiveness_Rating should be string.")
    if not pd.api.types.is_string_dtype(df['Control_Type']):
        raise TypeError("Control_Type should be string.")
    if not pd.api.types.is_bool_dtype(df['Control_Key_Status']): # Changed from is_string_dtype
        raise TypeError("Control_Key_Status should be boolean.")
    if not pd.api.types.is_numeric_dtype(df['Process_Complexity']):
        raise TypeError("Process_Complexity should be numeric.")
    if not pd.api.types.is_numeric_dtype(df['Operational_Metric_1']):
        raise TypeError("Operational_Metric_1 should be numeric.")
    if not pd.api.types.is_numeric_dtype(df['Operational_Metric_2']):
        raise TypeError("Operational_Metric_2 should be numeric.")

```
**Streamlit Integration**:
*   Call `validate_data` on the generated `synthetic_df` within a `try-except` block.
*   Display success/error messages using `st.success` or `st.error`.
*   Include the narrative and business value markdown in the main content area.

### 4.4 Residual Risk Calculation
**Description**: This component calculates the residual risk rating based on inherent risk and control effectiveness, using either a 'Basic' (subtractive) or 'Weighted' (ratio) method.
**Business Value**: Quantifies remaining risk exposure after controls, enabling prioritization of mitigation efforts and evaluation of control effectiveness. The basic formula for residual risk calculation is:
$$
\text{Residual Risk} = f(\text{Inherent Risk}, \text{Control Effectiveness})
$$
where $f$ can be either an additive function (Basic method) or a multiplicative/weighted function (Weighted method). The choice of method should reflect the organization's specific approach to risk assessment and the relative importance of controls in mitigating inherent risks.

**Extracted Code**:
*Note*: The original `calculate_residual_risk` function has `risk_ratings` as `{'Low': 1, 'Medium': 2, 'High': 3}` but `generate_synthetic_data` includes `'Very High'`. The `calculate_residual_risk` function also has a complex nested ternary operator for `Residual_Risk_Rating` mapping which is prone to errors. It should be refactored for clarity and correctness, especially to handle the 'Very High' category. For consistency and simplicity in the Streamlit app, the `risk_ratings` dictionary should be expanded to include 'Very High' with an appropriate numerical mapping (e.g., 4).

```python
def calculate_residual_risk(df, calculation_method):
    """Calculates the residual risk rating based on the specified calculation method."""
    if df.empty:
        df['Residual_Risk_Score'] = []
        df['Residual_Risk_Rating'] = []
        return df

    if calculation_method not in ['Basic', 'Weighted']:
        raise ValueError("Invalid calculation_method. Choose 'Basic' or 'Weighted'.")

    # Define risk rating mappings, expanded to include 'Very High'
    risk_ratings_to_numeric = {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4}
    # Control effectiveness ratings from notebook are Ineffective, Partially Effective, Effective.
    # The synthetic data generator uses 'Low', 'Medium', 'High', 'Very High' for Control_Effectiveness_Rating.
    # This is a discrepancy that needs to be resolved for the function to work correctly with generated data.
    # For this specification, we assume a mapping that aligns with generated data's 'Low', 'Medium', 'High', 'Very High'
    # Or, the data generation should be modified to produce 'Ineffective', 'Partially Effective', 'Effective'.
    # For the purpose of the spec, let's assume the ratings are consistent and the mapping needs to reflect that.
    # Given the original notebook's use of 'Low', 'Medium', 'High' for CE in the context of the tables,
    # let's adjust the generated data's 'Control_Effectiveness_Rating' to fit the expected categories for calculation.
    # Alternatively, the function's internal mapping for control effectiveness should match the data generator's output.
    # Let's align it with 'Low', 'Medium', 'High', 'Very High' for consistency in input data, then map to 'control_scores'
    # that reflect their 'effectiveness'.
    control_ratings_to_score = {'Low': 3, 'Medium': 2, 'High': 1, 'Very High': 0.5} # Assuming Low means 'Effective', High means 'Ineffective'

    # Validate Inherent Risk Ratings and map to numeric scores
    df['Inherent_Risk_Numeric'] = df['Inherent_Risk_Rating'].map(risk_ratings_to_numeric)
    if df['Inherent_Risk_Numeric'].isnull().any():
        invalid_ir = df[df['Inherent_Risk_Numeric'].isnull()]['Inherent_Risk_Rating'].unique()
        raise ValueError(f"Invalid Inherent_Risk_Rating value(s): {invalid_ir}. Allowed values are: Low, Medium, High, Very High")

    # Validate Control Effectiveness Ratings and map to scores
    df['Control_Effectiveness_Score'] = df['Control_Effectiveness_Rating'].map(control_ratings_to_score)
    if df['Control_Effectiveness_Score'].isnull().any():
        invalid_ce = df[df['Control_Effectiveness_Score'].isnull()]['Control_Effectiveness_Rating'].unique()
        raise ValueError(f"Invalid Control_Effectiveness_Rating value(s): {invalid_ce}. Allowed values are: Low, Medium, High, Very High (interpreted as Effective to Ineffective)")

    # Calculate Residual Risk Score
    if calculation_method == 'Basic':
        df['Residual_Risk_Score'] = df['Inherent_Risk_Numeric'] - df['Control_Effectiveness_Score']
    elif calculation_method == 'Weighted':
        # Ensure no division by zero if Control_Effectiveness_Score can be 0.
        # Adding a small epsilon or handling cases where score is 0.5
        df['Residual_Risk_Score'] = df['Inherent_Risk_Numeric'] / df['Control_Effectiveness_Score'].replace(0, 0.001) # Avoid division by zero

    # Define a more robust Residual Risk Rating Mapping
    # This logic needs careful re-evaluation based on how scores should map to Low/Medium/High
    # A simplified, threshold-based mapping is more practical than the nested if-else from the notebook.
    # Example:
    min_score = df['Residual_Risk_Score'].min()
    max_score = df['Residual_Risk_Score'].max()
    score_range = max_score - min_score

    if score_range > 0:
        low_threshold = min_score + 0.33 * score_range
        medium_threshold = min_score + 0.66 * score_range
    else: # Handle case where all scores are the same
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

    # Drop temporary numeric columns
    df = df.drop(columns=['Inherent_Risk_Numeric', 'Control_Effectiveness_Score'])

    return df
```
**Streamlit Integration**:
*   Place `calculation_method` as `st.radio` or `st.selectbox` in the sidebar.
*   Call `calculate_residual_risk` on the validated `synthetic_df`.
*   Display the updated `synthetic_df` with new `Residual_Risk_Score` and `Residual_Risk_Rating` columns using `st.dataframe`.
*   Include the narrative and business value markdown in the main content area.

### 4.5 Dynamic Visualizations

All visualization functions should be adapted to return `matplotlib.Figure` objects or directly use `st.pyplot(fig)` to display the plots within Streamlit.

#### 4.5.1 Relationship Plot: Process Complexity vs. Residual Risk
**Description**: A scatter plot to visualize the correlation between `Process_Complexity` and `Residual_Risk_Rating`.
**Business Value**: Helps identify if more complex processes lead to higher residual risks, guiding control efforts or process simplification.
The scatter plot visualizes the relationship as:
$$
\text{Scatter Plot} = \text{Points}(\text{Process Complexity}, \text{Residual Risk Rating (Numerical)})
$$
where each point represents a risk assessment unit.

**Extracted Code**:
```python
def plot_relationship_scatter(df):
    """Generates a scatter plot of Process Complexity vs Residual Risk."""
    if df.empty or 'Process_Complexity' not in df.columns or 'Residual_Risk_Rating' not in df.columns:
        st.warning("Cannot generate scatter plot: missing required data or columns.")
        return None

    # Convert Residual_Risk_Rating to numerical values for plotting
    risk_mapping = {'Low': 1, 'Medium': 2, 'High': 3} # Assuming 3 levels for plot
    df_plot = df.copy() # Work on a copy to avoid SettingWithCopyWarning
    df_plot['Residual_Risk_Rating_Numerical'] = df_plot['Residual_Risk_Rating'].map(risk_mapping)

    if df_plot['Residual_Risk_Rating_Numerical'].isnull().any():
        st.warning("Skipping scatter plot: Residual_Risk_Rating contains values outside expected 'Low', 'Medium', 'High'.")
        return None

    fig, ax = plt.subplots(figsize=(8, 6)) # Use subplots for explicit figure and axes
    ax.scatter(df_plot['Process_Complexity'], df_plot['Residual_Risk_Rating_Numerical'], alpha=0.7)
    ax.set_title('Process Complexity vs Residual Risk Rating', fontsize=14)
    ax.set_xlabel('Process Complexity', fontsize=12)
    ax.set_ylabel('Residual Risk Rating (Numerical)', fontsize=12)
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(['Low', 'Medium', 'High'])
    ax.grid(True)
    plt.tight_layout() # Adjust layout
    return fig
```
**Streamlit Integration**:
*   Call `plot_relationship_scatter(synthetic_df)`.
*   Display the plot using `st.pyplot(fig)`.
*   Include the narrative and business value markdown.

#### 4.5.2 Trend Plot: Average Residual Risk Rating Over Assessment Cycles
**Description**: A line chart to visualize the trend of average `Residual_Risk_Rating` over `Assessment_Cycle`.
**Business Value**: Essential for proactive risk management by identifying emerging risks and assessing long-term control effectiveness.
The line chart visualizes the trend as:
$$
\text{Line Chart} = \text{Line}(\text{Assessment Cycle}, \text{Average Residual Risk Rating})
$$
where the line connects the average residual risk rating for each assessment cycle.

**Extracted Code**:
```python
def plot_trend_line(df):
    """Generates a line chart showing the trend of average Residual Risk Rating over Assessment Cycles."""
    if df.empty or 'Assessment_Cycle' not in df.columns or 'Residual_Risk_Rating' not in df.columns:
        st.warning("Cannot generate trend plot: missing required data or 'Assessment_Cycle' column.")
        return None

    risk_mapping = {'Low': 1, 'Medium': 2, 'High': 3} # Assuming 3 levels for plot
    df_plot = df.copy() # Work on a copy
    df_plot['Residual_Risk_Rating_Numerical'] = df_plot['Residual_Risk_Rating'].map(risk_mapping)

    if df_plot['Residual_Risk_Rating_Numerical'].isnull().any():
        st.warning("Skipping trend plot: Residual_Risk_Rating contains values outside expected 'Low', 'Medium', 'High'.")
        return None

    avg_risk = df_plot.groupby('Assessment_Cycle')['Residual_Risk_Rating_Numerical'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(avg_risk['Assessment_Cycle'], avg_risk['Residual_Risk_Rating_Numerical'], marker='o', linestyle='-', color='skyblue')
    ax.set_title('Trend of Average Residual Risk Rating Over Assessment Cycles', fontsize=14)
    ax.set_xlabel('Assessment Cycle', fontsize=12)
    ax.set_ylabel('Average Residual Risk Rating', fontsize=12)
    ax.grid(True, linestyle='--')
    ax.set_xticks(avg_risk['Assessment_Cycle']) # Ensure all assessment cycles are displayed on x-axis
    ax.set_ylim(0.5, 3.5) # Set fixed y-axis limits for consistency across updates
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(['Low', 'Medium', 'High'])
    plt.tight_layout()
    return fig
```
**Streamlit Integration**:
*   Display this plot only if `has_time_series` is `True`.
*   Call `plot_trend_line(synthetic_df)`.
*   Display the plot using `st.pyplot(fig)`.
*   Include the narrative and business value markdown.

#### 4.5.3 Aggregated Comparison: Heatmap (Implementation Required)
**Description**: A heatmap showing `Inherent_Risk_Rating` vs. `Control_Effectiveness_Rating` and the resulting `Residual_Risk_Rating` for different units, similar to sample residual risk charts [8].
**Business Value**: Provides a quick visual summary of how different combinations of inherent risk and control effectiveness map to residual risk, highlighting high-risk areas.

**Required Implementation Details**:
This function is mentioned in the notebook's "Features" but no corresponding Python code is provided. A new function `plot_risk_heatmap` will need to be implemented.

```python
def plot_risk_heatmap(df):
    """Generates a heatmap of Inherent Risk vs Control Effectiveness showing Residual Risk."""
    if df.empty or 'Inherent_Risk_Rating' not in df.columns or 'Control_Effectiveness_Rating' not in df.columns or 'Residual_Risk_Rating' not in df.columns:
        st.warning("Cannot generate heatmap: missing required data or columns.")
        return None

    # Define order for categorical axes for consistent plotting
    risk_rating_order = ['Low', 'Medium', 'High', 'Very High']
    # Adjust control effectiveness order if it uses Low, Medium, High from data generator,
    # mapping to 'Effective', 'Partially Effective', 'Ineffective'
    # Assuming for heatmap, we want to display the actual rating labels.
    control_effectiveness_order = ['Low', 'Medium', 'High', 'Very High'] # These are the values from synthetic data

    # Create a pivot table: group by Inherent_Risk_Rating and Control_Effectiveness_Rating
    # and compute the mean numerical Residual_Risk_Rating
    risk_mapping_numerical = {'Low': 1, 'Medium': 2, 'High': 3} # For averaging residual risk numerically
    df_plot = df.copy()
    df_plot['Residual_Risk_Rating_Numerical'] = df_plot['Residual_Risk_Rating'].map(risk_mapping_numerical)

    if df_plot['Residual_Risk_Rating_Numerical'].isnull().any():
        st.warning("Skipping heatmap: Residual_Risk_Rating contains values outside expected 'Low', 'Medium', 'High'.")
        return None

    # Calculate average residual risk score for each combination
    heatmap_data = df_plot.groupby(['Inherent_Risk_Rating', 'Control_Effectiveness_Rating'])['Residual_Risk_Rating_Numerical'].mean().unstack()

    # Reindex to ensure consistent order
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
```
**Streamlit Integration**:
*   Call `plot_risk_heatmap(synthetic_df)`.
*   Display the plot using `st.pyplot(fig)`.
*   Include the narrative and business value markdown.

### 4.6 General Streamlit Structure
The `app.py` or main Streamlit file will orchestrate the execution:
1.  Set up page configuration (`st.set_page_config`).
2.  Display application title and overview using `st.title` and `st.markdown`.
3.  Implement sidebar for inputs using `st.sidebar`.
4.  Generate data using `generate_synthetic_data` based on sidebar inputs.
5.  Perform data validation using `validate_data` and display results.
6.  Calculate residual risk using `calculate_residual_risk` based on sidebar input.
7.  Display dataframes (`st.dataframe`).
8.  Render visualizations (`st.pyplot`) in dedicated sections, conditionally displaying the trend plot.
9.  Ensure all narrative sections and business value explanations from the notebook are included using `st.markdown`.
