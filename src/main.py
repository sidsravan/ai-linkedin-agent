from news_collector import fetch_news
from content_generator import generate_post
from linkedin_poster import post_to_linkedin
import json
import os

def save_post(post):
    os.makedirs("data", exist_ok=True)

    with open("data/posts_history.json", "a") as f:
        json.dump({"post": post}, f)
        f.write("\n")

def main():
    news = fetch_news()
    post = generate_post(news)

    post_to_linkedin(post)
    save_post(post)

if __name__ == "__main__":
    main()