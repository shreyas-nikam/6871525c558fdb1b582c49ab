import pytest
from definition_9a0c13edf76c4f259df127dbd6ac30b2 import generate_synthetic_data
import pandas as pd

def is_dataframe(obj):
    return isinstance(obj, pd.DataFrame)

def has_required_columns(df):
    required_columns = ['Risk_Assessment_Unit_ID', 'Risk_Assessment_Unit_Type', 'Inherent_Risk_Rating', 'Control_Effectiveness_Rating', 'Control_Type', 'Control_Key_Status', 'Process_Complexity', 'Operational_Metric_1', 'Operational_Metric_2']
    return all(col in df.columns for col in required_columns)

def are_columns_populated(df):
    for col in ['Risk_Assessment_Unit_ID', 'Risk_Assessment_Unit_Type', 'Inherent_Risk_Rating', 'Control_Effectiveness_Rating']:
        if df[col].isnull().any():
            return False
    return True

def check_time_series_column(df):
     return 'Assessment_Cycle' in df.columns

def check_correct_time_series_column(df):
    if 'Assessment_Cycle' in df.columns:
      return pd.api.types.is_integer_dtype(df['Assessment_Cycle'])
    else:
      return True

@pytest.mark.parametrize("num_units, has_time_series, expected_type, expected_columns, time_series_column", [
    (10, False, pd.DataFrame, True, False),
    (0, False, pd.DataFrame, True, False),
    (5, True, pd.DataFrame, True, True),
    (5, 'incorrect', TypeError, None, None),

])
def test_generate_synthetic_data(num_units, has_time_series, expected_type, expected_columns, time_series_column):
    try:
        df = generate_synthetic_data(num_units, has_time_series)
        assert isinstance(df, expected_type)
        if expected_columns:
            assert has_required_columns(df)
            assert are_columns_populated(df)
        if time_series_column:
          assert check_time_series_column(df)
          assert check_correct_time_series_column(df)
        else:
          assert not check_time_series_column(df)


    except Exception as e:

        assert type(e) == expected_type
