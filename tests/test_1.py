import pytest
import pandas as pd
from definition_e457de9c59664d558f6c99b1f0d4351e import validate_data

def test_validate_data_valid_dataframe():
    df = pd.DataFrame({
        'Risk_Assessment_Unit_ID': [1, 2],
        'Risk_Assessment_Unit_Type': ['Functional', 'Process-based'],
        'Inherent_Risk_Rating': ['Low', 'Medium'],
        'Control_Effectiveness_Rating': ['Effective', 'Partially Effective'],
        'Control_Type': ['Preventative', 'Detective'],
        'Control_Key_Status': ['Key', 'Non-Key'],
        'Process_Complexity': [1.0, 2.0],
        'Operational_Metric_1': [3.0, 4.0],
        'Operational_Metric_2': [5.0, 6.0]
    })
    try:
        validate_data(df)
        assert True  # If no exception is raised, the test passes
    except Exception:
        assert False  # Fail if any exception is raised

def test_validate_data_missing_column():
    df = pd.DataFrame({
        'Risk_Assessment_Unit_ID': [1, 2],
        'Inherent_Risk_Rating': ['Low', 'Medium'],
        'Control_Effectiveness_Rating': ['Effective', 'Partially Effective'],
        'Control_Type': ['Preventative', 'Detective'],
        'Control_Key_Status': ['Key', 'Non-Key'],
        'Process_Complexity': [1.0, 2.0],
        'Operational_Metric_1': [3.0, 4.0],
        'Operational_Metric_2': [5.0, 6.0]
    })
    with pytest.raises(KeyError):
        validate_data(df)

def test_validate_data_duplicate_risk_unit_id():
    df = pd.DataFrame({
        'Risk_Assessment_Unit_ID': [1, 1],
        'Risk_Assessment_Unit_Type': ['Functional', 'Process-based'],
        'Inherent_Risk_Rating': ['Low', 'Medium'],
        'Control_Effectiveness_Rating': ['Effective', 'Partially Effective'],
        'Control_Type': ['Preventative', 'Detective'],
        'Control_Key_Status': ['Key', 'Non-Key'],
        'Process_Complexity': [1.0, 2.0],
        'Operational_Metric_1': [3.0, 4.0],
        'Operational_Metric_2': [5.0, 6.0]
    })
    with pytest.raises(ValueError):  # Assuming the function raises ValueError
         validate_data(df)

def test_validate_data_missing_values():
    df = pd.DataFrame({
        'Risk_Assessment_Unit_ID': [1, 2],
        'Risk_Assessment_Unit_Type': ['Functional', 'Process-based'],
        'Inherent_Risk_Rating': ['Low', None],
        'Control_Effectiveness_Rating': ['Effective', 'Partially Effective'],
        'Control_Type': ['Preventative', 'Detective'],
        'Control_Key_Status': ['Key', 'Non-Key'],
        'Process_Complexity': [1.0, 2.0],
        'Operational_Metric_1': [3.0, 4.0],
        'Operational_Metric_2': [5.0, 6.0]
    })
    with pytest.raises(ValueError):
        validate_data(df)

def test_validate_data_invalid_data_type():
    df = pd.DataFrame({
        'Risk_Assessment_Unit_ID': [1, 2],
        'Risk_Assessment_Unit_Type': ['Functional', 'Process-based'],
        'Inherent_Risk_Rating': ['Low', 'Medium'],
        'Control_Effectiveness_Rating': ['Effective', 'Partially Effective'],
        'Control_Type': ['Preventative', 'Detective'],
        'Control_Key_Status': ['Key', 'Non-Key'],
        'Process_Complexity': ['a', 'b'],
        'Operational_Metric_1': [3.0, 4.0],
        'Operational_Metric_2': [5.0, 6.0]
    })
    with pytest.raises(TypeError):
        validate_data(df)
