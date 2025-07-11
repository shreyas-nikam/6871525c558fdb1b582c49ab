import pytest
import pandas as pd
from definition_bd06a8a38ccf44a78080119f38417dc3 import calculate_residual_risk

@pytest.fixture
def sample_df():
    data = {'Inherent_Risk_Rating': ['High', 'Medium', 'Low', 'High', 'Medium'],
            'Control_Effectiveness_Rating': ['Ineffective', 'Partially Effective', 'Effective', 'Effective', 'Ineffective']}
    return pd.DataFrame(data)

def test_calculate_residual_risk_basic(sample_df):
    df = calculate_residual_risk(sample_df.copy(), 'Basic')
    assert 'Residual_Risk_Rating' in df.columns
    assert 'Residual_Risk_Score' in df.columns
    assert df['Residual_Risk_Rating'].tolist() == ['High', 'Medium', 'Low', 'Low', 'Medium']

def test_calculate_residual_risk_weighted(sample_df):
    df = calculate_residual_risk(sample_df.copy(), 'Weighted')
    assert 'Residual_Risk_Rating' in df.columns
    assert 'Residual_Risk_Score' in df.columns
    assert df['Residual_Risk_Rating'].tolist() == ['High', 'Medium', 'Low', 'Low', 'High']

def test_calculate_residual_risk_empty_df():
    df = pd.DataFrame({'Inherent_Risk_Rating': [], 'Control_Effectiveness_Rating': []})
    df = calculate_residual_risk(df, 'Basic')
    assert 'Residual_Risk_Rating' in df.columns
    assert 'Residual_Risk_Score' in df.columns
    assert len(df) == 0

def test_calculate_residual_risk_invalid_method(sample_df):
    with pytest.raises(ValueError) as excinfo:
        calculate_residual_risk(sample_df.copy(), 'InvalidMethod')
    assert "Invalid calculation_method. Choose 'Basic' or 'Weighted'." in str(excinfo.value)

def test_calculate_residual_risk_invalid_ratings(sample_df):
    sample_df['Inherent_Risk_Rating'] = ['Invalid', 'Medium', 'Low', 'High', 'Medium']
    with pytest.raises(ValueError) as excinfo:
        calculate_residual_risk(sample_df.copy(), 'Basic')
    assert "Invalid Inherent_Risk_Rating value: Invalid. Allowed values are: Low, Medium, High" in str(excinfo.value)
