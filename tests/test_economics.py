import pytest
from advisory_engine.tco_calculator import EnterpriseTCOEngine

def test_tco_calculation_logic():
    engine = EnterpriseTCOEngine(node_count=1)
    result = engine.calculate_3yr_tco(power_kwh_rate=0.10)
    assert result["CapEx_Investment"] > 0
    assert result["Total_3Yr_TCO"] > result["CapEx_Investment"]
