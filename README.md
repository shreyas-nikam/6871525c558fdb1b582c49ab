# QuLab: Operational Risk Assessment with Streamlit

![QuLab Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Title

**QuLab: Interactive Operational Risk Assessment Application**

## Description

QuLab is a Streamlit-based web application designed to provide a hands-on experience for understanding and managing operational risk. It utilizes synthetic data to simulate risk assessment scenarios, allowing users to generate, validate, calculate, and visualize operational risk metrics. This application is a valuable tool for learning the critical steps involved in maintaining financial stability, ensuring regulatory compliance, and enhancing overall organizational resilience within a risk management context.

The application guides users through the following key stages:

*   **Synthetic Data Generation**: Create a dataset mimicking real-world operational risk attributes.
    $$\text{Synthetic Data} = \{ \text{randomly sampled attributes for each unit} \}$$
*   **Data Validation**: Ensure the integrity and quality of the generated data based on predefined rules.
    $$\text{Data Validation} = \{ \text{Column Presence} \} \cap \{ \text{Data Type Correctness} \} \cap \{ \text{PK Uniqueness} \} \cap \{ \text{No Missing Values} \}$$
*   **Residual Risk Calculation**: Compute residual risk based on inherent risk and control effectiveness, using different methodologies.
    $$\text{Residual Risk} = f(\text{Inherent Risk}, \text{Control Effectiveness})$$
*   **Risk Visualization**: Explore relationships and trends within the risk data through interactive charts.

## Features

*   **Interactive Data Generation**:
    *   Generate synthetic operational risk data with configurable parameters (number of risk units, inclusion of time-series data).
    *   Simulate various risk attributes such as risk unit type, inherent risk rating, control effectiveness, control type, process complexity, and operational metrics.
*   **Robust Data Validation**:
    *   Automated checks for required column presence.
    *   Verification of data type correctness for all columns.
    *   Ensuring primary key (Risk\_Assessment\_Unit\_ID) uniqueness.
    *   Detection of any missing values within the dataset.
*   **Flexible Risk Calculation**:
    *   Choose between "Basic" (Inherent Risk - Control Effectiveness) and "Weighted" (Inherent Risk / Control Effectiveness) methods for residual risk calculation.
    *   Mapping of qualitative risk ratings (Low, Medium, High, Very High) to quantitative scores for calculation.
    *   Dynamic mapping of calculated scores back to qualitative residual risk ratings.
*   **Insightful Visualizations**:
    *   **Relationship Scatter Plot**: Visualize the relationship between Process Complexity and Residual Risk Rating.
    *   **Trend Line Plot**: Analyze the trend of average Residual Risk Rating over different Assessment Cycles (if time-series data is included).
    *   **Risk Heatmap**: Display the average Residual Risk across combinations of Inherent Risk and Control Effectiveness ratings, providing a matrix view of risk profiles.
*   **Session State Management**: Data generated and calculated on one page is seamlessly carried over to subsequent pages using Streamlit's session state, ensuring a cohesive user experience.
*   **User-Friendly Interface**: Built with Streamlit for an intuitive and responsive web interface.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.7+
*   `pip` (Python package installer)
*   `git` (for cloning the repository)

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/quolab-operational-risk.git
    cd quolab-operational-risk
    ```
    *(Note: Replace `https://github.com/your-username/quolab-operational-risk.git` with the actual repository URL if it exists.)*

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    The required Python libraries are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

    **`requirements.txt` content:**
    ```
    streamlit>=1.0
    pandas>=1.0
    numpy>=1.20
    matplotlib>=3.0
    seaborn>=0.11
    ```

## Usage

1.  **Run the Streamlit Application:**
    Navigate to the project's root directory in your terminal (where `app.py` is located) and run:
    ```bash
    streamlit run app.py
    ```

2.  **Access the Application:**
    Your web browser should automatically open to `http://localhost:8501` (or a similar address).

3.  **Navigate and Interact:**
    *   Use the **sidebar navigation** to switch between "Data Generation and Validation", "Risk Calculation", and "Visualizations" pages.
    *   On the **"Data Generation and Validation"** page, adjust parameters like "Number of Risk Units" and "Include Time Series Data" using the sidebar controls. The generated data will be displayed, followed by a validation status. Ensure validation is successful before proceeding.
    *   On the **"Risk Calculation"** page, choose between "Basic" and "Weighted" calculation methods for residual risk. The calculated residual risk scores and ratings will be displayed.
    *   On the **"Visualizations"** page, explore various plots showing relationships between risk factors. Note that the "Trend Plot" requires "Include Time Series Data" to be checked on the first page.

## Project Structure

The project is organized into a modular structure for better maintainability and readability.

```
.
├── app.py                      # Main Streamlit application entry point
├── application_pages/          # Directory containing individual page modules
│   ├── __init__.py             # Initializes the application_pages package
│   ├── page1.py                # Handles Data Generation and Validation logic
│   ├── page2.py                # Handles Residual Risk Calculation logic
│   └── page3.py                # Handles Visualization logic
└── requirements.txt            # Lists all Python dependencies
```

*   `app.py`: Sets up the main Streamlit layout, navigation, and serves as the entry point for the multi-page application by calling functions from `application_pages`.
*   `application_pages/`: This directory contains separate Python files for each distinct section (page) of the application. This modular approach keeps the codebase clean and organized.

## Technology Stack

*   **Python**: The core programming language.
*   **Streamlit**: For building the interactive web application and its user interface.
*   **Pandas**: Essential for data manipulation and analysis, particularly with DataFrames.
*   **NumPy**: Used for numerical operations and efficient generation of synthetic data.
*   **Matplotlib**: A plotting library used for creating static, interactive, and animated visualizations.
*   **Seaborn**: A data visualization library based on matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics.

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature` or `bugfix/FixBug`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file (if present) for details. If not explicitly present, it is intended to be open source under the MIT license.

## Contact

For any questions or suggestions, please feel free to reach out:

*   **Organization**: QuantUniversity (as implied by the "QuLab" name and logo)
*   **Email/Website**: [info@quantuniversity.com](mailto:info@quantuniversity.com) / [www.quantuniversity.com](https://www.quantuniversity.com)
*   **GitHub Issues**: [https://github.com/your-username/quolab-operational-risk/issues](https://github.com/your-username/quolab-operational-risk/issues) *(Replace with actual repository link)*
