from playwright.sync_api import Page, expect
import time

def test_login_successful(page: Page) -> None:
    # page.set_viewport_size({"width": 800, "height": 600})
    page.goto("https://leogcarvalho.github.io/test-automation-practice")
    page.get_by_role("textbox", name="Username: (admin)").click()
    page.get_by_role("textbox", name="Username: (admin)").fill("admin")
    page.get_by_role("textbox", name="Password: (1234)").click()
    page.get_by_role("textbox", name="Password: (1234)").fill("1234")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Login successful!")).to_be_visible()
    time.sleep(3)

"""
Comandos no terminal:
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
"""