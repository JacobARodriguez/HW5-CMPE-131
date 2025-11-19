from src.pricing import apply_discount


def test_apply_discount_regression_percentage():
    """
    Regression test for the original bug in apply_discount where
    the percent was treated as a raw multiplier instead of a percentage.
    """
    result = apply_discount(100.0, 10)
    # Correct behavior: 10% off of 100 = 90
    assert result == 90.0


def test_apply_discount_regression_large_percent():
    """
    Another regression example: 50% off should halve the price.
    """
    result = apply_discount(200.0, 50)
    assert result == 100.0
