import os
from playwright.sync_api import sync_playwright

def load_auth():
    if not os.path.exists("auth.json"):
        raise Exception("❌ auth.json not found. Run save_auth.py first.")
    print("✅ Loaded auth.json")

def post_to_linkedin(content):
    load_auth()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()

        page.goto("https://www.linkedin.com/feed/")
        page.wait_for_timeout(5000)

        if "login" in page.url:
            print("⚠️ Login failed, skipping post")
            return

        page.get_by_role("button", name="Start a post").click()
        page.wait_for_timeout(3000)
        page.locator("div[role='textbox']").first.fill(content)
        page.wait_for_timeout(2000)
        page.locator("button.share-actions__primary-action").click()
        page.wait_for_timeout(5000)

        print("✅ Post submitted successfully")
        browser.close()
