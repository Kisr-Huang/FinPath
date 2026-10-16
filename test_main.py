
import pytest

from main import calculate_future_value


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
