from playwright.sync_api import sync_playwright
import os, base64

username = os.getenv("LINKEDIN_USERNAME")
password = os.getenv("LINKEDIN_PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.linkedin.com/login")
    page.fill("input#username", username)
    page.fill("input#password", password)
    page.click("button[type=submit]")

    page.wait_for_timeout(5000)  # wait for login

    # Save fresh session
    context.storage_state(path="auth.json")

    # Encode auth.json for GitHub secret usage
    with open("auth.json", "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
        print("::set-output name=auth::" + encoded)

    print("✅ auth.json refreshed successfully")
    browser.close()
