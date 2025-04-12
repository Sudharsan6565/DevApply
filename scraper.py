import json

# Mocked list for now — replace this with real scraped data
results = [
    {
        "name": "Alice Founder",
        "role": "CTO",
        "email": "alice@cooltech.com",
        "company": "CoolTech",
        "posted": "3 days ago",
        "remote": "Yes",
        "company_email": "hello@cooltech.com",
        "linkedin": "https://linkedin.com/in/alice",
        "twitter": "https://twitter.com/alice_f"
    },
    {
        "name": "Bob Builder",
        "role": "Founder",
        "email": "",
        "company": "NextGen",
        "posted": "1 week ago",
        "remote": "No",
        "company_email": "",
        "linkedin": "https://linkedin.com/in/bob",
        "twitter": ""
    }
]

with open("linkedin_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Exported LinkedIn data to linkedin_results.json")

