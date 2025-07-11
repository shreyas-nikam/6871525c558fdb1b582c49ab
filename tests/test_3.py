import pytest
import pandas as pd
from definition_2784457361864556b5e7c231c59a2f7e import plot_risk_heatmap
import matplotlib.pyplot as plt
import io

def create_sample_dataframe():
    data = {'Inherent_Risk_Rating': ['High', 'Medium', 'Low', 'High', 'Medium'],
            'Control_Effectiveness_Rating': ['Ineffective', 'Partially Effective', 'Effective', 'Effective', 'Ineffective'],
            'Residual_Risk_Rating': ['High', 'Medium', 'Low', 'Low', 'High']}
    return pd.DataFrame(data)

def test_plot_risk_heatmap_valid_data():
    df = create_sample_dataframe()
    try:
        plot_risk_heatmap(df)
        plt.close()
    except Exception as e:
        pytest.fail(f"plot_risk_heatmap raised an exception: {e}")

def test_plot_risk_heatmap_empty_dataframe():
    df = pd.DataFrame()
    try:
        plot_risk_heatmap(df)
        plt.close()
    except Exception as e:
        pytest.fail(f"plot_risk_heatmap raised an exception with empty dataframe: {e}")

def test_plot_risk_heatmap_missing_columns():
    df = pd.DataFrame({'Some_Other_Column': [1, 2, 3]})
    with pytest.raises(KeyError):
         plot_risk_heatmap(df)
         plt.close()

def test_plot_risk_heatmap_non_dataframe_input():
    with pytest.raises(AttributeError):
        plot_risk_heatmap([1,2,3])
        plt.close()

def test_plot_risk_heatmap_all_same_risk_level():
    data = {'Inherent_Risk_Rating': ['High', 'High', 'High', 'High', 'High'],
            'Control_Effectiveness_Rating': ['Ineffective', 'Partially Effective', 'Effective', 'Effective', 'Ineffective'],
            'Residual_Risk_Rating': ['High', 'Medium', 'Low', 'Low', 'High']}
    df = pd.DataFrame(data)
    try:
        plot_risk_heatmap(df)
        plt.close()
    except Exception as e:
        pytest.fail(f"plot_risk_heatmap raised an exception with same risk level: {e}")
