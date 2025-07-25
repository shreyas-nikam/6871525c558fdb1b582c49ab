id: 6871525c558fdb1b582c49ab_documentation
summary: Second Lab of Module 3 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Operational Risk Assessment with Streamlit: A QuLab Guide

## Step 1: Introduction to Operational Risk and the QuLab Application
Duration: 00:05:00

Welcome to the QuLab Operational Risk Assessment Codelab! In this guide, you will learn how to set up, understand, and extend a Streamlit application designed for hands-on exploration of operational risk assessment using synthetic data.

Operational risk is defined as the risk of loss resulting from inadequate or failed internal processes, people and systems, or from external events. Managing operational risk is crucial for any organization, especially in finance, as it directly impacts financial stability, regulatory compliance, and overall organizational resilience. This application provides a practical environment to simulate and analyze operational risk scenarios.

<aside class="positive">
  Understanding operational risk is not just about compliance; it's about <b>proactive risk management</b> to safeguard an organization's assets and reputation.
</aside>

The QuLab application focuses on three core concepts:

1.  **Synthetic Data Generation**: Creating realistic, yet artificial, datasets for risk analysis without relying on sensitive real-world data. This allows for safe experimentation and development.
    $$\text{Synthetic Data} = \{ \text{randomly sampled attributes for each unit} \}$$

2.  **Data Validation**: Ensuring the quality and integrity of the generated data. This is a critical step in any data-driven process to prevent errors and ensure reliable analysis.
    $$\text{Data Validation} = \{ \text{Column Presence} \} \cap \{ \text{Data Type Correctness} \} \cap \{ \text{PK Uniqueness} \} \cap \{ \text{No Missing Values} \}$$

3.  **Residual Risk Calculation**: Determining the risk that remains after controls have been put in place. This is a key metric in operational risk management.
    $$\text{Residual Risk} = f(\text{Inherent Risk}, \text{Control Effectiveness})$$
    Here, $f$ represents a function that combines inherent risk (the raw risk before controls) and control effectiveness (how well the controls mitigate the risk).

### Application Architecture Overview

The QuLab application is built with Streamlit and is modularized into several Python files for better organization and maintainability.

-   **`app.py`**: The main entry point of the Streamlit application. It handles the overall layout, displays introductory information, and manages navigation between different functional pages using Streamlit's sidebar.
-   **`application_pages/page1.py`**: Dedicated to data generation and initial validation. This module allows users to configure and create synthetic operational risk data.
-   **`application_pages/page2.py`**: Focuses on calculating residual risk based on the generated data. It implements different methodologies for risk computation.
-   **`application_pages/page3.py`**: Provides various visualizations to help users understand the relationships and trends within the risk data.

Data flow between these pages is managed using Streamlit's `st.session_state`, which allows a DataFrame generated on one page to be accessed and modified on subsequent pages.

**Flowchart Representation:**

```mermaid
graph TD
    A[Start Application: app.py] --> B{Navigation Selection};
    B -- "Data Generation and Validation" --> C[Page 1: generate_synthetic_data & validate_data];
    C -- "Store DF in session_state" --> D[session_state];
    B -- "Risk Calculation" --> E[Page 2: calculate_residual_risk];
    E -- "Read DF from session_state" --> D;
    D -- "Update DF in session_state" --> E;
    B -- "Visualizations" --> F[Page 3: plot_visualizations];
    F -- "Read DF from session_state" --> D;
```
*(Note: The mermaid diagram above is a conceptual representation. Markdown codelab format does not natively render mermaid, but it illustrates the logical flow.)*

Now, let's get started by setting up your environment and running the application.

## Step 2: Setting Up the Environment and Running the Application
Duration: 00:05:00

Before running the QuLab application, you need to ensure you have Python installed and the necessary libraries are in your environment.

### Prerequisites

You will need:
-   Python 3.8+
-   `streamlit`
-   `pandas`
-   `numpy`
-   `matplotlib`
-   `seaborn`

### Project Structure

Create a directory structure like this:

```
quLab_app/
├── app.py
└── application_pages/
    ├── __init__.py
    ├── page1.py
    ├── page2.py
    └── page3.py
```

### Installation

1.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

2.  **Activate the virtual environment:**
    -   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    -   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Install the required libraries:**
    ```bash
    pip install streamlit pandas numpy matplotlib seaborn
    ```

### Copying the Code

Place the provided code into the respective files:

**`app.py`**
```python
import streamlit as st

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, we explore operational risk assessment using synthetic data. This application allows you to generate risk assessment data, validate it, calculate residual risk based on different methods, and visualize the results. The purpose is to create hands-on experience for managing operational risk, which is vital for maintaining financial stability, ensuring regulatory compliance, and enhancing overall organizational resilience.

$\text{Synthetic Data} = \{ \text{randomly sampled attributes for each unit} \}$

$\text{Data Validation} = \{ \text{Column Presence} \} \cap \{ \text{Data Type Correctness} \} \cap \{ \text{PK Uniqueness} \} \cap \{ \text{No Missing Values} \}$

$\text{Residual Risk} = f(\text{Inherent Risk}, \text{Control Effectiveness})$
""")

page = st.sidebar.selectbox(label="Navigation", options=["Data Generation and Validation", "Risk Calculation", "Visualizations"])

if page == "Data Generation and Validation":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Risk Calculation":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Visualizations":
    from application_pages.page3 import run_page3
    run_page3() # Corrected: Added run_page3() call
```

**`application_pages/page1.py`**
```python
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
    st.markdown("""
    Here, you can generate synthetic operational risk data and validate its integrity. Adjust the parameters to create different datasets and ensure data quality.

    The synthetic data generation process is summarized by:
    $$\text{Synthetic Data} = \{ \text{randomly sampled attributes for each unit} \}$$
    where each attribute is independently generated based on predefined distributions or lists of possible values.

    The validation process can be summarized as follows:
    $$\text{Data Validation} = \{ \text{Column Presence} \} \cap \{ \text{Data Type Correctness} \} \cap \{ \text{PK Uniqueness} \} \cap \{ \text{No Missing Values} \}$$
    """)

    num_units = st.sidebar.slider("Number of Risk Units", min_value=10, max_value=100, value=50, help="Adjust the number of hypothetical risk assessment units to simulate.")
    has_time_series = st.sidebar.checkbox("Include Time Series Data", value=True, help="Check to include 'Assessment_Cycle' data, enabling the trend plot.")

    synthetic_df = generate_synthetic_data(num_units, has_time_series)

    st.subheader("Generated Data")
    st.dataframe(synthetic_df)

    st.subheader("Data Validation")
    try:
        validate_data(synthetic_df)
        st.success("Data validation successful!")
        # Store the generated and validated dataframe in session state for other pages
        st.session_state['synthetic_df'] = synthetic_df
    except Exception as e:
        st.error(f"Data validation failed: {e}")
        # Clear the session state if validation fails, to prevent using invalid data
        if 'synthetic_df' in st.session_state:
            del st.session_state['synthetic_df']


if __name__ == "__main__":
    run_page1()
```

**`application_pages/page2.py`**
```python
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
```

**`application_pages/page3.py`**
```python
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
```
*(Note: An `__init__.py` file (even empty) is required in the `application_pages` directory for Python to treat it as a package and allow imports like `from application_pages.page1 import run_page1`.)*

### Running the Application

1.  Open your terminal or command prompt.
2.  Navigate to the `quLab_app` directory (where `app.py` is located).
3.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

This command will open a new tab in your web browser displaying the QuLab application.

## Step 3: Data Generation and Validation
Duration: 00:10:00

The first core functionality of the QuLab application is generating synthetic operational risk data and validating its integrity. This is handled by `application_pages/page1.py`.

### Synthetic Data Generation

The `generate_synthetic_data` function creates a pandas DataFrame filled with various attributes relevant to operational risk assessment. These attributes are randomly sampled from predefined lists or distributions.

**Key attributes generated:**

-   `Risk_Assessment_Unit_ID`: Unique identifier for each unit.
-   `Risk_Assessment_Unit_Type`: Categories like 'Business Unit', 'Department', 'Team'.
-   `Inherent_Risk_Rating`: 'Low', 'Medium', 'High', 'Very High'.
-   `Control_Effectiveness_Rating`: 'Low', 'Medium', 'High', 'Very High' (representing different levels of control strength).
-   `Control_Type`: 'Preventative', 'Detective', 'Corrective'.
-   `Control_Key_Status`: Boolean (True/False).
-   `Process_Complexity`: Integer from 1 to 10.
-   `Operational_Metric_1`, `Operational_Metric_2`: Normally distributed numerical metrics.
-   `Assessment_Cycle` (Optional): An integer representing the year, included if `has_time_series` is True.

<aside class="positive">
  Using synthetic data is a great way to develop and test risk models without relying on sensitive real-world data, ensuring privacy and compliance during development.
</aside>

**Code Snippet (`generate_synthetic_data` function from `application_pages/page1.py`):**
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

### Data Validation

The `validate_data` function ensures the quality and correctness of the generated DataFrame. It performs several checks:

1.  **Column Presence**: Verifies that all expected columns exist.
2.  **Primary Key Uniqueness**: Checks for duplicate `Risk_Assessment_Unit_ID` values.
3.  **Missing Values**: Ensures there are no null values in the DataFrame.
4.  **Data Type Correctness**: Confirms that each column has the expected data type (e.g., numeric for IDs, string for ratings, boolean for status).

**Code Snippet (`validate_data` function from `application_pages/page1.py`):**
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
```

### Streamlit Interface

On the "Data Generation and Validation" page in the Streamlit app:
-   You will find a slider in the sidebar to control the **"Number of Risk Units"** (from 10 to 100).
-   A checkbox allows you to **"Include Time Series Data"**, which adds the `Assessment_Cycle` column, crucial for trend analysis in visualizations.
-   The generated data is displayed in a `st.dataframe` widget.
-   After generation, the `validate_data` function is called, and a success or error message is shown based on the validation outcome.
-   Crucially, the validated DataFrame is stored in Streamlit's `st.session_state` as `'synthetic_df'`. This allows the data to persist and be accessed by other pages (`page2` and `page3`) without re-generation. If validation fails, the `session_state` is cleared to prevent downstream issues.

<aside class="negative">
  If data validation fails, the application will display an error, and subsequent pages that rely on this data (Risk Calculation, Visualizations) will not function correctly until valid data is generated. Always ensure data quality!
</aside>

Experiment with different settings and observe the generated data and validation results.

## Step 4: Residual Risk Calculation
Duration: 00:15:00

Once the synthetic data is generated and validated, the next step is to calculate the residual risk. This process is handled by `application_pages/page2.py`. Residual risk represents the level of risk remaining after considering the effectiveness of existing controls.

### The `calculate_residual_risk` Function

This function takes the DataFrame and a `calculation_method` as input and computes a `Residual_Risk_Score` and `Residual_Risk_Rating` for each risk unit.

1.  **Mapping Ratings to Numeric Scores**:
    -   `Inherent_Risk_Rating` (Low, Medium, High, Very High) are mapped to numerical values (1, 2, 3, 4 respectively).
    -   `Control_Effectiveness_Rating` (Low, Medium, High, Very High) are mapped to scores (3, 2, 1, 0.5 respectively). Note that 'Low' control effectiveness leads to a higher control score (meaning controls are weak, hence more risk), and 'Very High' control effectiveness leads to a lower score (meaning controls are very strong, mitigating risk significantly).

2.  **Residual Risk Calculation Methods**:
    The application provides two common methods:

    -   **Basic Method**: This is an additive or subtractive model.
        $$\text{Residual Risk Score} = \text{Inherent Risk Numeric} - \text{Control Effectiveness Score}$$
        A higher inherent risk score and a lower control effectiveness score (meaning controls are less effective) will result in a higher residual risk score.

    -   **Weighted Method**: This is a multiplicative or ratio-based model.
        $$\text{Residual Risk Score} = \frac{\text{Inherent Risk Numeric}}{\text{Control Effectiveness Score}}$$
        For this method, `Control_Effectiveness_Score` is replaced with `0.001` if it is zero to avoid division by zero errors. This method implies that control effectiveness proportionally reduces inherent risk.

3.  **Mapping Score to Rating**:
    The calculated `Residual_Risk_Score` is then mapped back to categorical ratings ('Low', 'Medium', 'High'). This mapping is dynamic, based on the range of scores in the current dataset:
    -   Scores are divided into three equal bins based on the `min_score` and `max_score` observed:
        -   Scores $\le \text{min\_score} + 0.33 \times \text{score\_range}$ are mapped to 'Low'.
        -   Scores $\le \text{min\_score} + 0.66 \times \text{score\_range}$ are mapped to 'Medium'.
        -   All other scores are mapped to 'High'.

**Code Snippet (`calculate_residual_risk` function from `application_pages/page2.py`):**
```python
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
```

### Streamlit Interface

On the "Risk Calculation" page in the Streamlit app:
-   A radio button in the sidebar allows you to select the **"Calculation Method"** (Basic or Weighted).
-   The page retrieves the `synthetic_df` from `st.session_state` (which was populated and validated on Page 1).
-   The `calculate_residual_risk` function is called, and the resulting DataFrame, now including `Residual_Risk_Score` and `Residual_Risk_Rating` columns, is displayed.
-   The updated DataFrame is then stored back into `st.session_state` to make it available for the visualization page.

<aside class="positive">
  Experiment with both 'Basic' and 'Weighted' calculation methods to observe how different approaches to combining inherent risk and control effectiveness can impact the final residual risk ratings. This highlights the importance of choosing an appropriate risk model.
</aside>

## Step 5: Visualizing Operational Risk
Duration: 00:15:00

Visualizations are essential for understanding complex data, identifying trends, and communicating insights. The `application_pages/page3.py` module provides several plots to help analyze the operational risk data.

### Plotting Functions

The page implements three distinct visualizations using `matplotlib` and `seaborn`:

1.  **Relationship Plot: Process Complexity vs Residual Risk (Scatter Plot)**
    -   **Function**: `plot_relationship_scatter(df)`
    -   **Purpose**: To visualize if there's any correlation or pattern between the complexity of a process and its resulting residual risk. More complex processes might intuitively lead to higher residual risk.
    -   This plot maps `Residual_Risk_Rating` to numerical values for plotting purposes.

2.  **Trend Plot: Average Residual Risk Rating Over Assessment Cycles (Line Plot)**
    -   **Function**: `plot_trend_line(df)`
    -   **Purpose**: If 'Assessment_Cycle' data is included (from Page 1), this plot shows how the average residual risk has evolved over different assessment periods. This is critical for identifying improvements or deteriorations in overall risk posture over time.
    -   It aggregates the average numerical residual risk rating per `Assessment_Cycle`.

3.  **Aggregated Comparison: Heatmap of Inherent Risk vs Control Effectiveness**
    -   **Function**: `plot_risk_heatmap(df)`
    -   **Purpose**: This heatmap provides an aggregated view of average residual risk based on combinations of `Inherent_Risk_Rating` and `Control_Effectiveness_Rating`. It's an excellent way to see which combinations typically result in higher or lower residual risk. For example, high inherent risk with low control effectiveness should clearly show high residual risk.

**Code Snippets (functions from `application_pages/page3.py`):**

**`plot_relationship_scatter`**
```python
def plot_relationship_scatter(df):
    """Generates a scatter plot of Process Complexity vs Residual Risk."""
    if df.empty or 'Process_Complexity' not in df.columns or 'Residual_Risk_Rating' not in df.columns:
        st.warning("Cannot generate scatter plot: missing required data or columns.")
        return None

    risk_mapping = {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4}
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
    ax.set_yticks([1, 2, 3, 4])
    ax.set_yticklabels(['Low', 'Medium', 'High', 'Very High'])
    ax.grid(True)
    plt.tight_layout()
    return fig
```

**`plot_trend_line`**
```python
def plot_trend_line(df):
    """Generates a line chart showing the trend of average Residual Risk Rating over Assessment Cycles."""
    if df.empty or 'Assessment_Cycle' not in df.columns or 'Residual_Risk_Rating' not in df.columns:
        st.warning("Cannot generate trend plot: missing required data or 'Assessment_Cycle' column.")
        return None

    risk_mapping = {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4}
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
    ax.set_ylim(0.5, 4.5)
    ax.set_yticks([1, 2, 3, 4])
    ax.set_yticklabels(['Low', 'Medium', 'High', 'Very High'])
    plt.tight_layout()
    return fig
```

**`plot_risk_heatmap`**
```python
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
```

### Streamlit Interface

On the "Visualizations" page in the Streamlit app:
-   The page retrieves the processed `synthetic_df` from `st.session_state` (which now includes `Residual_Risk_Score` and `Residual_Risk_Rating`).
-   Each plotting function is called, and if a figure is returned (meaning data requirements are met), it is displayed using `st.pyplot()`.
-   The trend plot (`plot_trend_line`) will only appear if you selected "Include Time Series Data" on the "Data Generation and Validation" page.

<aside class="positive">
  Visualizations make it easy to spot trends, anomalies, and areas of high risk at a glance. For instance, the heatmap immediately highlights which combinations of inherent risk and control effectiveness lead to the highest average residual risk.
</aside>

Explore the visualizations and how they change as you adjust parameters on the previous pages (e.g., number of units, inclusion of time series data, or the residual risk calculation method).

## Step 6: Extending and Customizing the Application
Duration: 00:10:00

The QuLab application provides a solid foundation for operational risk assessment. Here are some ideas for how you can extend and customize it further:

1.  **More Sophisticated Data Generation**:
    -   Implement correlations between attributes in `generate_synthetic_data` (e.g., higher process complexity leading to higher inherent risk).
    -   Add more nuanced distributions for numerical metrics (e.g., skewed distributions).
    -   Allow users to upload their own data instead of relying solely on synthetic data.

2.  **Advanced Data Validation**:
    -   Add rules for valid ranges for numerical columns.
    -   Implement cross-column validation (e.g., `Control_Type` must be 'Preventative' if `Control_Key_Status` is True).
    -   Integrate a data quality framework or a more robust schema validation library.

3.  **New Risk Calculation Methods**:
    -   Introduce new formulas for residual risk, perhaps based on industry-specific standards (e.g., Basel II/III operational risk approaches).
    -   Incorporate qualitative factors or expert judgment into the risk score.
    -   Model operational loss events and integrate them into the risk assessment.

4.  **Interactive Visualizations**:
    -   Replace `matplotlib` plots with interactive libraries like `Plotly`, `Altair`, or `Bokeh` for dynamic filtering and zooming.
    -   Create interactive dashboards that allow users to slice and dice the data based on various risk attributes.
    -   Implement a risk matrix visualization (e.g., a 5x5 matrix for likelihood vs. impact).

5.  **Database Integration**:
    -   Instead of `st.session_state`, connect the application to a real database (e.g., SQLite, PostgreSQL) to store and retrieve data persistently. This would allow for historical analysis and multi-user scenarios.

6.  **User Authentication and Authorization**:
    -   Add a login system to restrict access to certain functionalities or data.

7.  **Machine Learning for Risk Prediction**:
    -   Train a machine learning model (e.g., a classifier) to predict `Residual_Risk_Rating` based on other attributes, or to identify high-risk units.

### Example: Adding a New Control Rating Category

Let's say you want to add a 'Critical' control effectiveness rating.

**Modify `application_pages/page1.py`:**
In `generate_synthetic_data`, update `control_types`:
```python
    # ... existing code ...
    risk_ratings = ['Low', 'Medium', 'High', 'Very High']
    control_types = ['Preventative', 'Detective', 'Corrective'] # No change needed here for new rating
    
    # ... in data dictionary for 'Control_Effectiveness_Rating'
    # This actually uses risk_ratings for control effectiveness, so update risk_ratings instead
    risk_ratings = ['Low', 'Medium', 'High', 'Very High', 'Critical'] # Add 'Critical'
    # ... and adjust probabilities if desired
    data = {
        # ...
        'Inherent_Risk_Rating': np.random.choice(risk_ratings, num_units),
        'Control_Effectiveness_Rating': np.random.choice(risk_ratings, num_units), # This uses the same list
        # ...
    }
```
In `validate_data`, ensure it can handle the new string:
```python
    # No direct change needed if it's still a string, but consider adding validation for allowed values.
    # The error handling in calculate_residual_risk already catches invalid values.
```

**Modify `application_pages/page2.py`:**
In `calculate_residual_risk`, update `risk_ratings_to_numeric` and `control_ratings_to_score` mappings:
```python
    risk_ratings_to_numeric = {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4, 'Critical': 5} # Add 'Critical'
    control_ratings_to_score = {'Low': 3, 'Medium': 2, 'High': 1, 'Very High': 0.5, 'Critical': 0.1} # Add 'Critical' with a very low score for very effective control
```
You might also need to adjust the `map_score_to_rating` function or thresholds if the new rating significantly changes the score range. Also, update `risk_rating_order` and `control_effectiveness_order` in `page3.py` for correct heatmap display.

<aside class="positive">
  Don't be afraid to experiment! The modular design of this Streamlit application makes it easy to add new features or modify existing ones without disrupting the entire codebase. Start with small, isolated changes and test frequently.
</aside>

This concludes the QuLab Operational Risk Assessment Codelab. We hope this comprehensive guide helps you understand the application's functionalities and inspires you to build upon it!
