# src/save_auth.py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.linkedin.com/login")
    print("Log in manually in the opened browser. After you see your feed, press ENTER here.")
    input("Press ENTER once logged in and feed is visible...")
    context.storage_state(path="auth.json")
    page.screenshot(path="debug_manual.png")
    print("✅ auth.json created")
    browser.close()
