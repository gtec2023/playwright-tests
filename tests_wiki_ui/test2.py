from playwright.sync_api import Playwright, sync_playwright, expect
from pom.dark_knight_elements import DarkKnightPage

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500) #TODO add slow_mo to see whats happening - waits these ms on each step
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(5000) #todo set to 5 seconds instead of default 30 - Does NOT apply to expect() which is 5 seconds unless overridden directly

    page.goto("https://www.wikipedia.org/")
    page.wait_for_load_state("networkidle")

    page.get_by_label("Search Wikipedia").click(timeout=3000) #TODO add timeout to overide default of 30 seconds
    page.get_by_label("Search Wikipedia").fill("batman films")
    page.get_by_role("link", name="Batman in film Film").click()
    page.locator("li:nth-child(11) > i > a").first.click()
    page.wait_for_load_state("networkidle")

    #use class - to avoid repetition of text
    dark_knight_page = DarkKnightPage(page)
    expect(dark_knight_page.dk_link).to_be_visible()

    #same as this
    expect(page.get_by_role("link", name="In the background, a building")).to_be_visible()

    expect(page.get_by_role("link", name="The Dark Knight (disambiguation)"), "missing the expected link!!!").to_be_visible()

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


with sync_playwright() as playwright:
    run(playwright)
