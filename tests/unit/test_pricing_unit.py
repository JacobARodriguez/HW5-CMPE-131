import pytest
from src.pricing import (
    parse_price,
    format_currency,
    apply_discount,
    add_tax,
    bulk_total,
)

# ---------- parse_price ----------

@pytest.mark.parametrize(
    "text, expected",
    [
        ("$1,234.50", 1234.50),
        ("12.5", 12.5),
        (" $0.99 ", 0.99),
    ],
)
def test_parse_price_valid(text, expected):
    result = parse_price(text)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize(
    "text",
    [
        "",
        "abc",
        "$12,34,56",  # treated as invalid per assignment description
    ],
)
def test_parse_price_invalid(text):
    with pytest.raises(ValueError):
        parse_price(text)


# ---------- format_currency ----------

@pytest.mark.parametrize(
    "value, expected",
    [
        (1, "$1.00"),
        (1.234, "$1.23"),
        (1.235, "$1.24"),  # rounding
    ],
)
def test_format_currency(value, expected):
    assert format_currency(value) == expected


# ---------- apply_discount ----------

@pytest.mark.parametrize(
    "price, percent, expected",
    [
        (100.0, 0, 100.0),
        (100.0, 10, 90.0),     # 10% off
        (200.0, 50, 100.0),    # 50% off
    ],
)
def test_apply_discount_normal(price, percent, expected):
    result = apply_discount(price, percent)
    assert result == pytest.approx(expected)


def test_apply_discount_negative_percent_raises():
    with pytest.raises(ValueError):
        apply_discount(100.0, -1)


# ---------- add_tax ----------

@pytest.mark.parametrize(
    "price, rate, expected",
    [
        (100.0, 0.07, 107.0),   # default-ish example
        (100.0, 0.10, 110.0),   # 10% tax
        (50.0, 0.0, 50.0),      # no tax
    ],
)
def test_add_tax(price, rate, expected):
    result = add_tax(price, rate)
    assert result == pytest.approx(expected)


def test_add_tax_negative_rate_raises():
    with pytest.raises(ValueError):
        add_tax(100.0, -0.05)


# ---------- bulk_total ----------

@pytest.fixture
def sample_prices():
    # simple fixture to reuse in multiple tests
    return [10.0, 20.0, 30.0]


def test_bulk_total_no_discount_default_tax(sample_prices):
    # subtotal = 60, default tax 7% => 60 * 1.07 = 64.2
    result = bulk_total(sample_prices)  # uses default discount=0, tax_rate=0.07
    assert result == pytest.approx(60.0 * 1.07)


def test_bulk_total_with_discount_and_tax():
    prices = [100.0, 50.0]  # subtotal = 150
    # 10% discount => 150 * 0.9 = 135
    # 5% tax => 135 * 1.05 = 141.75
    result = bulk_total(prices, discount_percent=10, tax_rate=0.05)
    assert result == pytest.approx(141.75)


def test_bulk_total_no_tax_with_discount():
    prices = [100.0]
    # 10% discount, no tax => 90
    result = bulk_total(prices, discount_percent=10, tax_rate=0.0)
    assert result == pytest.approx(90.0)
