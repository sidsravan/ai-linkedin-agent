import base64
import os
from playwright.sync_api import sync_playwright

def load_auth():
    auth = os.getenv("LINKEDIN_AUTH")

    with open("auth.json", "wb") as f:
        f.write(base64.b64decode(auth))

def post_to_linkedin(content):
    load_auth()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()

        page.goto("https://www.linkedin.com/feed/")
        page.wait_for_timeout(5000)

        page.click("text=Start a post")
        page.wait_for_timeout(2000)

        page.fill("div[role='textbox']", content)

        page.wait_for_timeout(1000)
        #page.click("text=Post")

        page.wait_for_timeout(5000)

        browser.close()