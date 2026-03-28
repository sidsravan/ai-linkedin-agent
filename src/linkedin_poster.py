import base64
import os
from playwright.sync_api import sync_playwright

def load_auth():
    auth = os.getenv("LINKEDIN_AUTH")

    with open("auth.json", "wb") as f:
        f.write(base64.b64decode(auth))

def post_to_linkedin(content):
    load_auth()

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )

        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()

        page.goto("https://www.linkedin.com/feed/")
        page.wait_for_timeout(5000)

        # Debug screenshot
        page.screenshot(path="debug.png")

        # Check login
        if "login" in page.url:
            raise Exception("❌ LinkedIn session expired. Recreate auth.json")

        # Click start post
        page.get_by_role("button", name="Start a post").click()
        page.wait_for_timeout(3000)

        # Fill content
        page.locator("div[role='textbox']").first.fill(content)

        page.wait_for_timeout(2000)

        # Click post
        page.get_by_role("button", name="Post").click()

        page.wait_for_timeout(5000)
        browser.close()