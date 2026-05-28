from playwright.sync_api import Page, expect
import time

def test_actions(page: Page) -> None:
    # page.set_viewport_size({"width": 800, "height": 600})
    page.goto("https://leogcarvalho.github.io/test-automation-practice")
    # page.get_by_role("textbox", name="Username: (admin)").fill("admin")
    # page.get_by_role("textbox", name="Password: (1234)").fill("1234")
    page.get_by_role("textbox", name="Username: (admin)").press_sequentially('admin', delay=500)
    page.get_by_role("textbox", name="Password: (1234)").press_sequentially('1234', delay=500)
    page.get_by_role("textbox", name="Select a date:").press_sequentially('01012030', delay=500)


"""
pytest --headed --slowmo 1000 -k test_actions
Esse --slowmo é interessante
playwright codegen https://leogcarvalho.github.io/test-automation-practice
"""