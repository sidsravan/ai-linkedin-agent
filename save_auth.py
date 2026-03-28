from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # 🔥 IMPORTANT: persistent context
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
    )

    page = context.new_page()
    page.goto("https://www.linkedin.com/login")

    input("👉 Login completely, wait 10 seconds, then press ENTER...")

    context.storage_state(path="auth.json")

    print("✅ auth.json created successfully")
    browser.close()