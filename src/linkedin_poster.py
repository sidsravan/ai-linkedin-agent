import base64, os
from playwright.sync_api import sync_playwright

def load_auth():
    auth = os.getenv("LINKEDIN_AUTH")
    with open("auth.json", "wb") as f:
        f.write(base64.b64decode(auth))

def post_to_linkedin(content):
    load_auth()
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()

        page.goto("https://www.linkedin.com/feed/")
        page.wait_for_timeout(5000)
        page.screenshot(path="debug_post.png")

        if "login" in page.url:
            print("⚠️ Login failed, skipping post")
            return

        page.get_by_role("button", name="Start a post").click()
        page.wait_for_timeout(3000)
        page.locator("div[role='textbox']").first.fill(content)
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="Post").click()
        page.wait_for_timeout(5000)
        browser.close()
