import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://www.flipkart.com/audio-video/pr?sid=0pm&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_7d53d7a7-553f-42ac-910a-8ec7439f8267_1_372UD5BXDFYS_MC.9JGNW7M0TUHD&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Electronics~Audio~All_9JGNW7M0TUHD&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=9JGNW7M0TUHD"

params = {
    "wjcEIp": "value"  
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}

response = requests.get(base_url, headers=headers, params=params)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    links = [link.get('href') for link in soup.find_all('a') if link.get('href')]

    with open('scraped_links.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Links"])

        for link in links:
            writer.writerow([link])

    print("Links scraped and saved to CSV successfully!")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
