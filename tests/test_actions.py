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
    # page.get_by_text("Feature 1").check()
    # expect(page.get_by_text("Feature 1")).to_be_checked()
    # page.get_by_text("Option B").check()

    # select_option
    # page.get_by_label("Choose an option:").select_option("Option 3")
    # page.get_by_label("Choose an option:").select_option(value="option2")

    # click actions
    page.get_by_text('Single Click').click()
    expect(page.get_by_text('Single click button clicked successfully!')).to_be_visible()
    page.get_by_text('Double Click').dblclick()
    expect(page.get_by_text('Double click button clicked successfully!')).to_be_visible()
    page.get_by_text('Right Click').click(button="right")
    expect(page.get_by_text('Right click button clicked successfully!')).to_be_visible()
    page.get_by_text('Shift + Click').click(modifiers=["Shift"])
    expect(page.get_by_text('Shift + click button clicked successfully!')).to_be_visible()
    page.get_by_text('Hover Menu').hover()
    # page.locator('//*[@class="dropdown-content"]/*[text()="Option 1"]').click()
    page.locator('.hover-menu a[href="#option1"]').click()
    expect(page).to_have_url('https://leogcarvalho.github.io/test-automation-practice/#option1')
    page.get_by_text('Single Click').click(position={'x': 0, 'y': 0})


"""
pytest --headed --slowmo 1000 -k test_actions
Esse --slowmo é interessante
playwright codegen https://leogcarvalho.github.io/test-automation-practice
"""