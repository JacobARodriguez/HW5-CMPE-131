# Homework- Name: Jacob Rodriguez

## Question 1) Define the following unit, integration, regression tests and when you would use each?

- Unit test: A unit test checks one small, isolated piece of code to make sure it behaves correctly for different inputs and edge cases, without involving files, networks, or other modules.

- Integration test: An integration test checks how multiple units work together as a group. You use integration tests to verify that data flows correctly across boundaries, e.g., reading an order from a file, computing totals, and writing a receipt.

- Regression test: A regression test is created after a bug is found to reproduce that bug and then verify the fix. You use regression tests to ensure that the same bug never comes back in future changes.

## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is.

Pytest discovers tests by naming conventions. It looks for files named test_*.py or *_test.py, then collects functions that start with 'test_' and classes named 'Test*'. When you run pytest in the project root, it walks the directories, finds these files and functions, and automatically runs them.

A fixture in pytest is a reusable setup function marked with @pytest.fixture that provides data or state to tests. Tests receive fixtures simply by listing them as function parameters, which lets you share setup/teardown logic across many tests in a clean and repeatable way.
