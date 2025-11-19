## Coverage Summary (latest run)

From the most recent run:

- `src/pricing.py`: **93%** coverage (43 statements, 3 missing)
- `src/order_io.py`: **90%** coverage (20 statements, 2 missing)
- `src/__init__.py`: **100%** coverage  
- **TOTAL**: **92%** coverage (63 statements, 5 missing)

## Uncovered Lines / Functions

According to `pytest --cov=src --cov-report=term-missing`, the following lines are not covered:

- `src/order_io.py`: lines **12**, **15**
- `src/pricing.py`: lines **7**, **21**, **32**

## Analysis of Uncovered Parts

The uncovered lines are in less critical or uncommon paths (such as setup or edge/error handling).  
All core pricing behavior (`parse_price`, `format_currency`, `apply_discount`, `add_tax`, `bulk_total`) and the main I/O flow (`load_order`, `write_receipt` via integration tests) are covered by tests, so the remaining uncovered lines are acceptable for this assignment.
::contentReference[oaicite:0]{index=0}
