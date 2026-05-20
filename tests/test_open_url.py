from playwright.sync_api import Page, expect
import time

def test_open_url(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice")
    expect(page).to_have_title("Test Automation Practice Page")
    page.get_by_role("radio", name="Option A").click()
    time.sleep(3)

"""
Comandos no terminal:
pip install pytest-playwright
playwright install
pytest
pytest --headed
pytest --headed --browser firefox
pytest --headed --browser webkit
pytest --headed --browser webkit --browser firefox
playwright codegen
pytest --headed .\tests\test_examples.py
pytest --headed -k test_login_successful
playwright codegen --viewport-size="800,600" https://leogcarvalho.github.io/test-automation-practice
playwright codegen --device="iPhone 15" https://leogcarvalho.github.io/test-automation-practice
pytest --headed -k test_login_successful --device="iPhone 15"
pytest --headed .\tests\test_open_url.py
pytest --headed .\tests\test_open_url.py .\tests\test_login_successful.py
pip install pytest-xdist
pytest --numprocesses 2
pytest --numprocesses 2 --headed
pytest --headed -k test_open_url
"""