# sinoxi_ad_conversion_ab_test/src/metrics.py

def conversion_rate(data, group_col='test_group', outcome_col='converted'):
    """Calculate conversion rate by group."""
    return data.groupby(group_col)[outcome_col].mean()

def lift_rate(base_rate, new_rate):
    """Calculate lift between base and new conversion rates."""
    return (new_rate - base_rate) / base_rate
