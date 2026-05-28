from playwright.sync_api import Page, expect
import time

def test_actions(page: Page) -> None:
    page.goto("https://leogcarvalho.github.io/test-automation-practice")

    # fill
    # page.get_by_role("textbox", name="Username: (admin)").fill("admin")
    # page.get_by_role("textbox", name="Password: (1234)").fill("1234")

    # press_sequentially
    # page.get_by_role("textbox", name="Username: (admin)").press_sequentially('admin', delay=500)
    # page.get_by_role("textbox", name="Password: (1234)").press_sequentially('1234', delay=500)
    # page.get_by_role("textbox", name="Select a date:").press_sequentially('01012030', delay=500)

    # check
    # get_by_role("checkbox", name="Feature 1")
    # get_by_role("radio", name="Option B")
    page.get_by_text("Feature 1").check()
    expect(page.get_by_text("Feature 1")).to_be_checked()
    page.get_by_text("Option B").check()


"""
pytest --headed --slowmo 1000 -k test_actions
Esse --slowmo é interessante
playwright codegen https://leogcarvalho.github.io/test-automation-practice
"""