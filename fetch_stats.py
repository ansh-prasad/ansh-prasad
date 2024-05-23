import requests
import json
from bs4 import BeautifulSoup

def fetch_leetcode_stats(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch LeetCode stats")

def fetch_gfg_stats(username):
    url = f"https://auth.geeksforgeeks.org/user/{username}/practice/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        stats = {
            "problems_solved": soup.find('div', class_='score_card_value').text.strip(),
            "coding_score": soup.find_all('div', class_='score_card_value')[1].text.strip(),
            "rank": soup.find_all('div', class_='score_card_value')[2].text.strip()
        }
        return stats
    else:
        raise Exception("Failed to fetch GeeksforGeeks stats")

if __name__ == "__main__":
    leetcode_username = "anshprasad01"
    gfg_username = "anshprasad01"

    leetcode_stats = fetch_leetcode_stats(leetcode_username)
    with open("leetcode_stats.json", "w") as f:
        json.dump(leetcode_stats, f)

    gfg_stats = fetch_gfg_stats(gfg_username)
    with open("gfg_stats.json", "w") as f:
        json.dump(gfg_stats, f)
