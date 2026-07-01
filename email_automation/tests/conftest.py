"""
Tests conftest – loads all shared fixtures from the fixtures package.
pytest discovers this file automatically when running email_automation/tests/.
"""
# Tell pytest to also load conftest.py from the fixtures package
pytest_plugins = ["email_automation.fixtures.conftest"]
