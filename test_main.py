
import pytest

from main import calculate_future_value, compare_investment_periods


def test_zero_interest_rate():
    result = calculate_future_value(1000, 100, 0, 1)

    assert result["future_value"] == 2200.00
    assert result["total_contributions"] == 2200.00
    assert result["estimated_gain"] == 0.00


def test_no_monthly_contribution():
    result = calculate_future_value(1000, 0, 0.12, 1)

    assert result["future_value"] > 1000
    assert result["total_contributions"] == 1000.00


def test_zero_principal_and_contribution():
    result = calculate_future_value(0, 0, 0.04, 1)

    assert result["future_value"] == 0.00
    assert result["estimated_gain"] == 0.00


@pytest.mark.parametrize(
    "principal, monthly_contribution, annual_rate, years",
    [
        (-1, 100, 0.04, 1),
        (1000, -1, 0.04, 1),
        (1000, 100, -0.01, 1),
        (1000, 100, 0.04, 0),
        (1000, 100, 0.04, 1.5),
        (1000, 100, 0.04, True),
    ],
)
def test_invalid_inputs(
    principal,
    monthly_contribution,
    annual_rate,
    years,
):
    with pytest.raises(ValueError):
        calculate_future_value(
            principal,
            monthly_contribution,
            annual_rate,
            years,
        )

def test_compare_investment_periods():
    results = compare_investment_periods(
        principal=50000,
        monthly_contribution=400,
        annual_rate=0.04,
        years_list=[10, 20],
    )

    assert len(results) == 2

    assert results[0]["years"] == 10
    assert results[0]["future_value"] == 133441.56
    assert results[0]["total_contributions"] == 98000
    assert results[0]["estimated_gain"] == 35441.56

    assert results[1]["years"] == 20
    assert results[1]["future_value"] == 257838.95
    assert results[1]["total_contributions"] == 146000
    assert results[1]["estimated_gain"] == 111838.95


def test_compare_investment_periods_empty_list():
    with pytest.raises(ValueError):
        compare_investment_periods(
            principal=50000,
            monthly_contribution=400,
            annual_rate=0.04,
            years_list=[],
        )
