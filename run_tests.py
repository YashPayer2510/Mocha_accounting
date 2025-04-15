import pytest
import subprocess

if __name__ == "__main__":
    # Run tests and collect allure results
    pytest.main(["--alluredir=allure-results", "tests"])  # adjust "tests" to your test folder

    # Generate allure HTML report
    subprocess.run(["allure", "generate", "allure-results", "-o", "allure-report", "--clean"], check=True)

    # (Optional) Automatically open report in browser
    # subprocess.run(["allure", "open", "allure-report"])
