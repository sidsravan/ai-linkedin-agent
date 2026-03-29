from playwright.sync_api import sync_playwright
import os

username = os.getenv("LINKEDIN_USERNAME")
password = os.getenv("LINKEDIN_PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.linkedin.com/login")
    page.wait_for_selector("input#username")
    page.fill("input#username", username)
    page.fill("input#password", password)
    page.click("button[type=submit]")

    page.wait_for_timeout(5000)
    page.screenshot(path="debug_login.png")
    print("Current URL after login:", page.url)

    context.storage_state(path="auth.json")
    print("✅ auth.json refreshed successfully")
    browser.close()