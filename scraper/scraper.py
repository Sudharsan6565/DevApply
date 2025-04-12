import json
import os
from core.session import launch_with_cookies
from playwright.sync_api import sync_playwright

def extract_recruiter_posts():
    with sync_playwright() as p:
        browser, context, page = launch_with_cookies(p)

        hashtag = "hiring"
        url = f"https://www.linkedin.com/feed/hashtag/{hashtag}/"

        print(f"🔍 Visiting {url}")
        page.goto(url)
        page.wait_for_timeout(3000)

        posts = page.query_selector_all('div.feed-shared-update-v2')
        recruiter_posts = []

        for post in posts:
            text = post.inner_text()
            if any(keyword in text.lower() for keyword in ["we're hiring", "hiring", "join us"]):
                try:
                    author = post.query_selector('span.feed-shared-actor__name').inner_text()
                    profile_url = post.query_selector('a.feed-shared-actor__container-link').get_attribute('href')
                    timestamp = post.query_selector('span.feed-shared-actor__sub-description').inner_text()
                    recruiter_posts.append({
                        "author": author,
                        "profile_url": f"https://linkedin.com{profile_url}",
                        "timestamp": timestamp,
                        "matched_keywords": True
                    })
                except Exception as e:
                    continue

        return recruiter_posts


def main():
    posts = extract_recruiter_posts()

    # Reformat to Prospect-style for Go
    structured = []
    for post in posts:
        structured.append({
            "name": post.get("author"),
            "role": "Recruiter",
            "email": "",
            "company": "",
            "posted": post.get("timestamp"),
            "remote": "",
            "company_email": "",
            "linkedin": post.get("profile_url"),
            "twitter": ""
        })

    with open("linkedin_results.json", "w") as f:
        json.dump(structured, f, indent=2)

    print(f"✅ Wrote {len(structured)} results to linkedin_results.json")


if __name__ == "__main__":
    main()

