import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page.pause()
    page.goto("https://www.booking.com/")

    page.wait_for_load_state("domcontentloaded")

    page.get_by_label("Dismiss sign-in info.").click()
    page.get_by_test_id("header-sign-in-button").click()
    page.get_by_placeholder("Enter your email address").click()
    page.get_by_placeholder("Enter your email address").fill("cocnballz@gmail.com")
    page.get_by_placeholder("Enter your email address").press("Tab")
    page.get_by_role("button", name="Continue with email").click()

    print("YAAAAAAAAAAAAAAAAY!")
    page.pause()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
