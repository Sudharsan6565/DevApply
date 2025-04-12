# devapply_agent/core/session.py

from playwright.sync_api import sync_playwright
import json
import os

COOKIE_PATH = os.path.join(os.path.dirname(__file__), "..", "cookies.json")

LINKEDIN_URL = "https://www.linkedin.com/"
def cookies_exist():
    return os.path.exists(COOKIE_PATH) and os.path.getsize(COOKIE_PATH) > 0
def save_cookies(context):
    cookies = context.cookies()
    with open(COOKIE_PATH, "w") as f:
        json.dump(cookies, f)
    print("✅ Cookies saved successfully.")

def load_cookies(context):
    if not os.path.exists(COOKIE_PATH):
        print("❌ Cookie file not found.")
        return False
    with open(COOKIE_PATH, "r") as f:
        cookies = json.load(f)
        context.add_cookies(cookies)
    print("✅ Cookies loaded successfully.")
    return True

def manual_login():
    from playwright.sync_api import sync_playwright
    import time

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=None)
        page = context.new_page()

        page.goto("https://www.linkedin.com/login")  # force direct login, skip home
        print("🔐 Please log in using EMAIL + PASSWORD.")

        input("🟢 Press Enter after logging in and reaching your homepage...")

        cookies = context.cookies()
        print(f"🍪 Cookie count: {len(cookies)}")

        if cookies:
            save_cookies(context)
            print("✅ Cookies saved successfully.")
        else:
            print("⚠️ No cookies found!")

        browser.close()


def launch_with_cookies(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    if not load_cookies(context):
        print("⚠️ No cookies found. Please run manual_login() first.")
        browser.close()
        return None, None, None

    page = context.new_page()
    page.goto(LINKEDIN_URL)
    print("🟢 Launched LinkedIn with saved session cookies.")
    return browser, context, page

