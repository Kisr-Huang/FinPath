
def calculate_future_value(
    principal: float,
    monthly_contribution: float,
    annual_rate: float,
    years: int,
) -> dict:
    """计算初始本金加每月月末追加资金的未来估算价值。

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


if __name__ == "__main__":
    result = calculate_future_value(
        principal=50000,
        monthly_contribution=400,
        annual_rate=0.04,
        years=20,
    )

    print("期末估算资产：", result["future_value"], "元")
    print("累计投入：", result["total_contributions"], "元")
    print("估算收益：", result["estimated_gain"], "元")

def run_basic_tests():
    # 测试 1：零利率，只计算本金与追加金额
    result = calculate_future_value(1000, 100, 0, 1)
    assert result["future_value"] == 2200.00
    assert result["total_contributions"] == 2200.00
    assert result["estimated_gain"] == 0.00

    # 测试 2：没有每月追加金额
    result = calculate_future_value(1000, 0, 0.12, 1)
    assert result["future_value"] > 1000
    assert result["total_contributions"] == 1000.00

    # 测试 3：本金与追加金额都为零
    result = calculate_future_value(0, 0, 0.04, 1)
    assert result["future_value"] == 0.00
    assert result["estimated_gain"] == 0.00

    # 测试 4：负本金应当报错
    try:
        calculate_future_value(-1, 100, 0.04, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("负本金应该触发 ValueError")

    print("全部基础测试通过！")


if __name__ == "__main__":
    run_basic_tests()
