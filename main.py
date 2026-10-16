
def calculate_future_value(
    principal: float,
    monthly_contribution: float,
    annual_rate: float,
    years: int,
) -> dict:
    """计算本金和每月月末追加资金的未来估算价值。

    annual_rate 使用小数表示，例如 4% 应传入 0.04。
    假设月利率等于年收益率除以 12。
    """
    if principal < 0:
        raise ValueError("初始本金不能为负数")

    if monthly_contribution < 0:
        raise ValueError("每月追加金额不能为负数")

    if annual_rate < 0:
        raise ValueError("年收益率不能为负数")

    if not isinstance(years, int) or isinstance(years, bool) or years < 1:
        raise ValueError("年限必须是大于等于 1 的整数")

    monthly_rate = annual_rate / 12
    total_months = years * 12
    balance = principal

    for _ in range(total_months):
        balance = balance * (1 + monthly_rate)
        balance += monthly_contribution

    total_contributions = principal + monthly_contribution * total_months
    estimated_gain = balance - total_contributions

    return {
        "future_value": round(balance, 2),
        "total_contributions": round(total_contributions, 2),
        "estimated_gain": round(estimated_gain, 2),
    }


def compare_investment_periods(
    principal: float,
    monthly_contribution: float,
    annual_rate: float,
    years_list: list[int],
) -> list[dict]:
    """比较多个投资期限下的估算资产与收益。"""
    if not years_list:
        raise ValueError("投资期限列表不能为空")

    results = []

    for years in years_list:
        result = calculate_future_value(
            principal=principal,
            monthly_contribution=monthly_contribution,
            annual_rate=annual_rate,
            years=years,
        )

        results.append({
            "years": years,
            **result,
        })

    return results


if __name__ == "__main__":
    results = compare_investment_periods(
        principal=50000,
        monthly_contribution=400,
        annual_rate=0.04,
        years_list=[10, 20],
    )

    for result in results:
        print(f"\n投资期限：{result['years']} 年")
        print(f"期末估算资产：{result['future_value']:.2f} 元")
        print(f"累计投入：{result['total_contributions']:.2f} 元")
        print(f"估算收益：{result['estimated_gain']:.2f} 元")
