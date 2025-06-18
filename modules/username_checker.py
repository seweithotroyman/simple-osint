import requests
from bs4 import BeautifulSoup

def check_username(username):
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Youtube": f"https://www.youtube.com/@{username}/"
    }
    result = {}
    for platform, url in platforms.items():
        r = requests.get(url)
        result[platform] = 'Found' if r.status_code == 200 else 'Not Found'
    return result
