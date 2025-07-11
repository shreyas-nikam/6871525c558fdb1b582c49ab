
# Technical Specification for Jupyter Notebook: Operational Risk Assessment Simulator

## 1. Notebook Overview

### 1.1. Learning Goals

This Jupyter Notebook is designed to provide an interactive simulation of an operational risk assessment program, allowing users to gain practical insights into the complex interplay between inherent risk, control effectiveness, and residual risk within a hypothetical organizational context. Upon completion, learners will be able to:

- Understand the steps and interactions within the operational risk assessment lifecycle, as outlined in the PRMIA handbook [3].
- Learn how inherent risk and control effectiveness contribute to residual risk calculations, exploring different approaches [8].
- Explore various methodologies for defining risk assessment units (functional, process-based, blended) and their implications [4].
- Analyze the impact of different control attributes (preventative vs. detective, key vs. non-key) on risk mitigation strategies [6].
- Understand the key insights contained in the uploaded document and supporting data.

### 1.2. Expected Outcomes

Users will:
- Interact with a synthetic dataset representing operational risk scenarios.
- Apply different calculation methodologies for residual risk based on PRMIA guidelines.
- Visualize the relationships between risk components and observe how changes in inputs affect the overall risk profile.
- Develop a deeper appreciation for the nuances of operational risk quantification beyond simplistic models.

### 1.3. Scope & Constraints

- The notebook must execute end-to-end on a mid-spec laptop (8 GB RAM) in fewer than 5 minutes.
- Only open-source Python libraries from PyPI may be used.
- All major steps need both code comments and brief narrative Markdown cells that describe **what** is happening and **why**.
- Deployment steps or platform-specific references (e.g., Streamlit) are explicitly excluded.

## 2. Mathematical and Theoretical Foundations

This section will explain the core concepts of operational risk assessment, focusing on the definitions and the functional relationship between Inherent Risk, Control Effectiveness, and Residual Risk, using LaTeX for all mathematical expressions.

### 2.1. Definition of Operational Risk

Operational risk is formally defined by the Basel Committee on Banking Supervision as:
$$
\text{The risk of loss resulting from inadequate or failed internal processes, people and systems, or from external events.}
$$
This definition includes legal risk but excludes strategic and reputational risk [1, Page 13].

### 2.2. The Operational Risk Assessment Lifecycle

The PRMIA handbook [3, Page 20] outlines an iterative process for identifying, assessing, and monitoring operational risk. Key components include:
- **Define Risk Assessment Units [4]:** The organizational units (functional, process-based, or blended) by which risks are categorized and assessed. This provides a consistent unit of measure for aggregation.
- **Top-down Workshops:** Senior management identifies and prioritizes high-level, firm-wide risks.
- **Identify Controls [6]:** Link identified risks to existing controls designed to mitigate them.
- **Process Reviews:** Detailed walk-throughs of processes to identify potential control gaps or breaks.
- **Control Substantiation [6]:** Evaluate controls for design effectiveness and quality of implementation. This includes assessing control attributes such as:
    - **Preventative vs. Detective Controls:** Preventative controls aim to prevent a risk event from occurring, while detective controls identify events either concurrently or after occurrence.
    - **Key vs. Non-key Controls:** Key controls are primary mitigants, whereas non-key controls supplement them.
- **Identify Issues & Design Action Plans:** Document control deficiencies and develop remediation plans.
- **Residual Risk Calculation [8]:** The focus of this simulation, it quantifies the risk remaining after controls have been applied.
- **Management Validation:** Senior management reviews and approves the overall risk profile.
- **Oversight & Monitoring:** Continuous tracking of the risk environment.

### 2.3. Residual Risk Calculation

The concept of residual risk is central to operational risk assessment. It represents the level of risk that remains after the application of controls. While intuitively one might consider it a simple subtraction of control effectiveness from inherent risk, the PRMIA handbook [8, Page 38] explicitly states it is "not a subtractive exercise." Instead, it is typically derived from a "ratings scale based on an additive approach" or a weighted function.

The simulation will implement two distinct approaches for calculating Residual Risk Rating, derived from the qualitative matrices provided in the PRMIA handbook [8, Page 38]. We will map qualitative ratings to numerical scores for consistent calculation.

**Scoring Convention:**
- **Inherent Risk (IR_score):** Low = 0, Medium = 1, High = 2
- **Control Effectiveness (CE_score):** Effective = 0, Partially Effective = 1, Ineffective = 2
    *Note: A higher CE_score implies lower effectiveness of controls.*
- **Residual Risk Rating (Output):** Low, Medium, High

#### 2.3.1. Approach 1: Basic Residual Risk Calculation ($f_1$)

This approach directly implements the logic from the "Residual risk chart" in the PRMIA handbook [8]. It represents a fundamental mapping of inherent risk and control effectiveness to the resulting residual risk.

The function $f_1(\text{IR\_score}, \text{CE\_score})$ is defined as:
$$
\text{Residual Risk Rating}_1 = \begin{cases}
\text{Low} & \text{if } \text{IR\_score} = 0 \text{ (Low)} \\
\text{Low} & \text{if } \text{IR\_score} = 1 \text{ (Medium) and } \text{CE\_score} = 0 \text{ (Effective)} \\
\text{Medium} & \text{if } \text{IR\_score} = 1 \text{ (Medium) and } (\text{CE\_score} = 1 \text{ (Partially Effective) or } \text{CE\_score} = 2 \text{ (Ineffective)}) \\
\text{Low} & \text{if } \text{IR\_score} = 2 \text{ (High) and } \text{CE\_score} = 0 \text{ (Effective)} \\
\text{Medium} & \text{if } \text{IR\_score} = 2 \text{ (High) and } \text{CE\_score} = 1 \text{ (Partially Effective)} \\
\text{High} & \text{if } \text{IR\_score} = 2 \text{ (High) and } \text{CE\_score} = 2 \text{ (Ineffective)}
\end{cases}
$$

#### 2.3.2. Approach 2: Residual Risk with Control Weighting ($f_2$)

This approach reflects the "control weighting" scenario, "recommended when the risk is high for violations of law" [8]. It demonstrates how inadequate controls in medium-inherent-risk scenarios can lead to a higher residual risk than in the basic approach.

The function $f_2(\text{IR\_score}, \text{CE\_score})$ is defined as:
$$
\text{Residual Risk Rating}_2 = \begin{cases}
\text{Low} & \text{if } \text{IR\_score} = 0 \text{ (Low)} \\
\text{Low} & \text{if } \text{IR\_score} = 1 \text{ (Medium) and } \text{CE\_score} = 0 \text{ (Effective)} \\
\text{Medium} & \text{if } \text{IR\_score} = 1 \text{ (Medium) and } \text{CE\_score} = 1 \text{ (Partially Effective)} \\
\text{High} & \text{if } \text{IR\_score} = 1 \text{ (Medium) and } \text{CE\_score} = 2 \text{ (Ineffective)} \\
\text{Low} & \text{if } \text{IR\_score} = 2 \text{ (High) and } \text{CE\_score} = 0 \text{ (Effective)} \\
\text{Medium} & \text{if } \text{IR\_score} = 2 \text{ (High) and } \text{CE\_score} = 1 \text{ (Partially Effective)} \\
\text{High} & \text{if } \text{IR\_score} = 2 \text{ (High) and } \text{CE\_score} = 2 \text{ (Ineffective)}
\end{cases}
$$
The key difference between $f_1$ and $f_2$ is in the scenario where Inherent Risk is Medium (IR_score = 1) and Control Effectiveness is Ineffective (CE_score = 2). In $f_1$, this results in Medium Residual Risk, whereas in $f_2$, it results in High Residual Risk, reflecting a heightened sensitivity to control failures for certain types of risks.

## 3. Code Requirements

This section outlines the structure, libraries, data handling, and visualization components of the Jupyter Notebook.

### 3.1. Expected Libraries

The following open-source Python libraries (from PyPI) will be used:
- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations, especially in synthetic data generation.
- `matplotlib.pyplot`: For static plotting.
- `seaborn`: For enhanced statistical data visualization.
- `ipywidgets`: For interactive user controls (sliders, dropdowns).

### 3.2. Logical Flow and Markdown Explanations

The notebook will follow a clear, logical flow, with each major step introduced by a Markdown cell explaining its purpose and followed by a code cell implementing the step. Code comments will further elaborate on the implementation details.

#### 3.2.1. Setup and Initialization

- **Markdown Cell:** Introduction to the notebook, a brief overview of operational risk, and the simulation's purpose.
- **Code Cell:**
    - Import necessary libraries (`pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`, `ipywidgets`).
    - Define global constants or configuration settings (e.g., color palettes, font sizes for plots).

#### 3.2.2. Synthetic Data Generation

- **Markdown Cell:** Explanation of synthetic data generation, its purpose in simulating diverse operational risk scenarios, and the attributes included.
- **Code Cell:**
    - **Function: `generate_synthetic_data(num_units, has_time_series=False)`**
        - Input: `num_units` (integer, number of risk assessment units), `has_time_series` (boolean, whether to include time-series data).
        - Generates a `pandas.DataFrame` with the following columns:
            - `Risk_Assessment_Unit_ID` (unique identifier)
            - `Risk_Assessment_Unit_Type` (categorical: 'Functional', 'Process-based', 'Blended' - simulating options for [4])
            - `Inherent_Risk_Rating` (categorical: 'Low', 'Medium', 'High')
            - `Control_Effectiveness_Rating` (categorical: 'Effective', 'Partially Effective', 'Ineffective')
            - `Control_Type` (categorical: 'Preventative', 'Detective' - simulating attributes from [6])
            - `Control_Key_Status` (categorical: 'Key', 'Non-Key' - simulating attributes from [6])
            - `Process_Complexity` (numeric: synthetic metric representing complexity)
            - `Operational_Metric_1` (numeric: general operational health indicator)
            - `Operational_Metric_2` (numeric: another general operational metric)
            - If `has_time_series` is True, include `Assessment_Cycle` (integer, e.g., 1 to 12 for monthly cycles).
        - Ensure realistic distribution (e.g., more 'Medium' than 'High' for inherent risk).
    - **Invocation:** Call `generate_synthetic_data` with user-defined parameters (via ipywidgets) to create the primary dataset.
    - **Optional Lightweight Sample:** Provide logic to load a pre-generated lightweight sample dataset (e.g., as a CSV file) if the user skips interactive data generation, ensuring the notebook can run without manual data input.

#### 3.2.3. Data Handling & Validation

- **Markdown Cell:** Describe the importance of data quality and the validation steps performed.
- **Code Cell:**
    - **Function: `validate_data(df)`**
        - Input: `df` (DataFrame).
        - Checks:
            - Confirm expected column names (`Inherent_Risk_Rating`, `Control_Effectiveness_Rating`, etc.).
            - Validate data types for critical fields.
            - Assert primary-key uniqueness (`Risk_Assessment_Unit_ID`).
            - Assert no missing values in critical fields (`Inherent_Risk_Rating`, `Control_Effectiveness_Rating`, `Process_Complexity`).
            - Log summary statistics for numeric columns (`.describe()`).
            - Log value counts for categorical columns.
        - Output: Prints validation messages and statistics.
    - **Invocation:** Call `validate_data` on the generated dataset.

#### 3.2.4. Interactive Residual Risk Calculation

- **Markdown Cell:** Explain the theoretical foundation of residual risk calculation and introduce the two approaches ($f_1$ and $f_2$) derived from the PRMIA handbook. Explain the `ipywidgets` for user interaction.
- **Code Cell:**
    - **Function: `calculate_residual_risk(df, calculation_method)`**
        - Input: `df` (DataFrame), `calculation_method` (string: 'Basic' for $f_1$, 'Weighted' for $f_2$).
        - Internal Mapping: Convert categorical risk ratings ('Low', 'Medium', 'High', 'Effective', 'Partially Effective', 'Ineffective') to numerical scores (0, 1, 2) as defined in Section 2.3 for internal calculation.
        - Apply the logic of $f_1$ or $f_2$ based on `calculation_method` to derive `Residual_Risk_Rating`.
        - Add `Residual_Risk_Rating` (categorical: 'Low', 'Medium', 'High') and a corresponding numerical `Residual_Risk_Score` to the DataFrame.
        - Return the updated DataFrame.
    - **IPyWidgets Integration:**
        - Create a dropdown widget for `calculation_method` selection ('Basic', 'Weighted').
        - Create parameters (sliders/text inputs) for potential scenario adjustments, such as:
            - `impact_of_key_controls_multiplier`: A slider (e.g., 0.8 to 1.2) that can slightly adjust the effective control rating for 'Key' controls, simulating their enhanced mitigation.
            - `regulatory_emphasis_factor`: A slider (e.g., 1.0 to 1.5) that can increase the numerical score of 'Ineffective' controls for 'High' inherent risks, simulating the "control weighting" scenario's emphasis on legal/regulatory impact.
        - Use `@interact` or `interactive` to link these widgets to the `calculate_residual_risk` function, allowing dynamic recalculation.
        - Include inline help text or tooltips for each control using `description` and `tooltip` parameters where applicable.
    - **Output:** Display a sample of the DataFrame with the newly calculated `Residual_Risk_Rating`.

#### 3.2.5. Dynamic Visualizations

- **Markdown Cell:** Introduce the visualization section, explaining what each plot illustrates regarding operational risk insights. Emphasize color-blind friendly design and interactivity.
- **Code Cell:**
    - **Function: `plot_risk_heatmap(df)`**
        - Input: `df` (DataFrame with `Inherent_Risk_Rating`, `Control_Effectiveness_Rating`, `Residual_Risk_Rating`).
        - Aggregated Comparison: Generate a heatmap showing the `Inherent_Risk_Rating` vs. `Control_Effectiveness_Rating` and the resulting `Residual_Risk_Rating`. This will likely require grouping the data and showing the *most frequent* or *average* residual risk for each combination.
        - Style: `seaborn.heatmap`. Adopt a color-blind-friendly palette. Set font size >= 12 pt. Clear title and labeled axes.
        - Interactivity: Consider using `plotly.express` or `altair` if budget/time allows for true interactivity, otherwise, ensure static fallback (saved PNG).
        - Fallback: Save the plot as a PNG image using `plt.savefig()` after display.
    - **Function: `plot_relationship_scatter(df)`**
        - Input: `df` (DataFrame with `Process_Complexity`, `Residual_Risk_Rating`).
        - Relationship Plot: Generate a scatter plot illustrating the correlation between `Process_Complexity` and `Residual_Risk_Rating`.
        - Style: `seaborn.scatterplot`. Color-blind friendly palette. Font size >= 12 pt. Clear title, labeled axes, and legend.
        - Interactivity/Fallback: As above.
    - **Function: `plot_trend_line(df)`**
        - Input: `df` (DataFrame with `Assessment_Cycle`, `Residual_Risk_Rating`). Requires `has_time_series=True` in data generation.
        - Trend Plot: Generate a line chart showing the trend of average `Residual_Risk_Rating` over simulated `Assessment_Cycle`s.
        - Style: `seaborn.lineplot`. Color-blind friendly palette. Font size >= 12 pt. Clear title, labeled axes, and legend.
        - Interactivity/Fallback: As above.
    - **Invocation:** Call the plotting functions with the processed DataFrame.

## 4. Additional Notes or Instructions

### 4.1. Assumptions

- The operational risk ratings (Inherent Risk, Control Effectiveness, Residual Risk) are categorical and can be mapped to discrete numerical values for calculation.
- The relationships between these risk components, as specified in the PRMIA handbook's sample tables, are considered the ground truth for this simulation.
- Synthetic data generated will sufficiently represent realistic operational risk scenarios for the purpose of demonstrating the concepts.
- The 'Assessment_Cycle' field, if generated, implies a sequential progression of risk assessments over time.

### 4.2. Customization and User Interaction

- **Parameters:** All key parameters for data generation (e.g., number of risk units) and risk calculation (e.g., `calculation_method`, `impact_of_key_controls_multiplier`, `regulatory_emphasis_factor`) will be exposed via `ipywidgets` (sliders, dropdowns, text inputs) to allow learners to rerun analyses with different settings.
- **Inline Help:** Comprehensive inline help text or tooltips will be provided for each interactive control to describe its function and impact.
- **Modularity:** Functions will be clearly defined to allow for easy modification or extension (e.g., adding new calculation methods or visualization types).

### 4.3. References

The theoretical underpinnings of this simulator are primarily drawn from the PRMIA Operational Risk Manager Handbook, Updated November, 2015:

- [1] Introduction to Operational Risk.
- [3] Risk Assessment Lifecycle.
- [4] Determining Risk Assessment Units: the Functional vs. Process Approach.
- [6] Control Assessment.
- [8] Residual Risk.

Additional references for Python libraries used:
- `pandas` documentation
- `numpy` documentation
- `matplotlib` documentation
- `seaborn` documentation
- `ipywidgets` documentation

