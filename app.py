
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
