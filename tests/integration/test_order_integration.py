from src.order_io import load_order, write_receipt
from src.pricing import bulk_total, format_currency


def test_order_integration(tmp_path):
    # 1) Create a temporary CSV order file
    input_file = tmp_path / "order.csv"
    input_file.write_text(
        "widget,$10.00\n"
        "gizmo,$5.50\n",
        encoding="utf-8",
    )

    # 2) Load items from the file
    items = load_order(input_file)
    # items = [("widget", 10.0), ("gizmo", 5.5)]

    # 3) Compute the expected total with discount + tax
    prices = [price for (_name, price) in items]
    discount_percent = 10   # 10% off
    tax_rate = 0.10         # 10% tax
    expected_total = bulk_total(prices, discount_percent, tax_rate)

    # 4) Write the receipt to an output file
    output_file = tmp_path / "receipt.txt"
    write_receipt(output_file, items, discount_percent, tax_rate)

    # 5) Read and verify the receipt contents
    output_text = output_file.read_text(encoding="utf-8")

    # Each item line appears
    assert "widget: $10.00" in output_text
    assert "gizmo: $5.50" in output_text

    # TOTAL line is present and correctly formatted
    assert "TOTAL:" in output_text
    assert f"TOTAL: {format_currency(expected_total)}" in output_text

