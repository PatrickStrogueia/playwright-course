from playwright.sync_api import Page, expect
import time

def test_all_locators(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/playwright-locators.html")

def test_get_by_role(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/playwright-locators.html")

    # get_by_role
    expect(page.get_by_role("button", name="Explicit Role Button")).to_be_visible()
    expect(page.get_by_role("link", name="Explicit Role Link")).to_be_visible()
    expect(page.get_by_role("img", name="robot icon")).to_be_visible()
    expect(page.get_by_role("button", name="Implicit Button")).to_be_visible()
    expect(page.get_by_role("link", name="Implicit Link")).to_be_visible()
    time.sleep(3)
    page.pause()

def test_get_by_text(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/playwright-locators.html")

    #get_by_text
    expect(page.get_by_text("Locate elements by their visible text content.", exact=True)).to_be_visible()
    time.sleep(3)

def test_get_by_label(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/playwright-locators.html")

    #get_by_label
    expect(page.get_by_label("Email Address", exact=True)).to_be_visible()
    page.get_by_label("Email Address", exact=True).click()
    expect(page.get_by_label("Accept Terms and Conditions", exact=True)).to_be_visible()
    page.get_by_label("Accept Terms and Conditions", exact=True).click()
    time.sleep(3)

def test_get_by_placeholder(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/playwright-locators.html")

    #get_by_placeholder
    page.get_by_placeholder("Search for items...", exact=True).click()
    time.sleep(3)
    page.get_by_placeholder("Enter your password").fill("123456")
    time.sleep(3)

def test_get_by_alt_text(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/playwright-locators.html")

    #get_by_alt_text
    expect(page.get_by_alt_text("python logo")).to_be_visible()
    expect(page.get_by_alt_text("javascript logo")).to_be_visible()

def test_get_by_title(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/playwright-locators.html")

    #get_by_title
    expect(page.get_by_title("Save your changes")).to_be_visible()
    expect(page.get_by_title("Go to homepage")).to_be_visible()

def test_get_by_test_id(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/playwright-locators.html")

    #get_by_test_id
    expect(page.get_by_test_id("submit-button")).to_be_visible()
    expect(page.get_by_test_id("status-message")).to_be_visible()

"""
pytest --headed -k test_all_locators
pytest --headed -k test_get_by_role
pytest --headed -k test_get_by_text
pytest --headed -k test_get_by_label
pytest --headed --slowmo 2000 -k test_get_by_alt_text
pytest --headed --slowmo 2000
pytest --headed --slowmo 2000 -k test_get_by_title
pytest --headed --slowmo 2000 -k get_by_test_id
"""