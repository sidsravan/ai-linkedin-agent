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
        page.screenshot(path="debug_feed.png")

        if "login" in page.url:
            print("⚠️ Login failed, screenshot saved as debug_feed.png")
            return

        page.get_by_role("button", name="Start a post").click()
        page.wait_for_timeout(3000)
        page.screenshot(path="debug_post_dialog.png")

        page.locator("div[role='textbox']").first.fill(content)
        page.wait_for_timeout(2000)

        # Scoped selector for Post button
        page.locator("button.share-actions__primary-action").click()
        page.wait_for_timeout(5000)
        page.screenshot(path="debug_post_done.png")

        print("✅ Post submitted successfully")
        browser.close()