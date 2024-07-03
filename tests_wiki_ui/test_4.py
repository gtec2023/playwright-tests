from playwright.sync_api import Playwright, sync_playwright, expect
from pom.dark_knight_elements import DarkKnightPage
import pytest

#TODO needs to start with 'test_' for pytest to find it and run it - DON'T NEED TO IMPORT ANYTHING FOR pytest!
@pytest.mark.xfail(reason="bad URL")
def test_dark_knight_page_two(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)  #TODO add slow_mo to see whats happening - waits these ms on each step
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(
        5000)  #todo set to 5 seconds instead of default 30 - Does NOT apply to expect() which is 5 seconds unless overridden directly

    page.goto("https://www.wikipediaXXX.org/")
    page.wait_for_load_state("networkidle")

    assert page.is_visible("text=WILL_NOT_BE_THERE")

    print("Test expected to fail: XFAIL")
    # ---------------------
    context.close()
    browser.close()
@pytest.mark.skip(reason="TO DEMO HOW TO SKIP")
def test_dark_knight_page_three(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)  #TODO add slow_mo to see whats happening - waits these ms on each step
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(
        5000)  #todo set to 5 seconds instead of default 30 - Does NOT apply to expect() which is 5 seconds unless overridden directly

    page.goto("https://www.wikipedia.org/")
    page.wait_for_load_state("networkidle")

    page.get_by_label("Search Wikipedia").click(timeout=3000)  #TODO add timeout to overide default of 30 seconds
    page.get_by_label("Search Wikipedia").fill("batman films")
    page.get_by_role("link", name="Batman in film Film").click()
    page.locator("li:nth-child(11) > i > a").first.click()
    page.wait_for_load_state("networkidle")

    #use class - to avoid repetition of text
    dark_knight_page = DarkKnightPage(page)
    expect(dark_knight_page.dk_link).to_be_visible()

    #same as this
    expect(page.get_by_role("link", name="In the background, a building")).to_be_visible()

    expect(page.get_by_role("link", name="The Dark Knight (disambiguation)"),
           "missing the expected link!!!").to_be_visible()

    # todo use nth(i) to get by index
    expect(page.locator("text=The Dark Knight").nth(1)).to_be_visible()

    page.get_by_role("link", name="James Gordon").first.click()
    #page.pause()
    gordon_text = page.get_by_role("cell", name="Jim Gordon", exact=True).text_content()
    assert gordon_text == "Jim Gordon"
    print(gordon_text)

    #todo get all links
    all_links = page.get_by_role("link").all()
    print(str(all_links.__sizeof__()) + " links!")
    #todo show links containing 'the Joker'
    # WORKS BUT TOO MANY OF THEM!
    # for link in all_links:
    #     if "the Joker" in link.text_content():
    #         print(link.text_content())

    print("Test finished")
    # ---------------------
    context.close()
    browser.close()

# with sync_playwright() as playwright:
#     run(playwright)   TODO DONT NEED TO RUN HERE AS pytest WILL FIND IT AND RUN IT as name starts with 'test_'
