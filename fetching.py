import requests
from bs4 import BeautifulSoup
import json

# Step 1: Send a GET request to the website with headers
url = "https://www.flipkart.com/syga-thumb-piano-kalimba-17-tone-keys-finger-kalingba-musical-instrument-analog-portable-keyboard/p/itm50b469e76dc05?pid=MKDGEBEMRY6UKTYK&lid=LSTMKDGEBEMRY6UKTYKGNK53U&hl_lid=&marketplace=FLIPKART"

# Setting user-agent to simulate a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}


response = requests.get(url, headers=headers)

# Step 2: Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Saving the title and some links to a text file
    title = soup.title.text
    links = [link.get('href') for link in soup.find_all('a')]

    with open('scraped_data.txt', 'w', encoding='utf-8') as file:
        file.write(f"Page Title: {title}\n")
        file.write("Links:\n")
        for link in links:
            file.write(f"{link}\n")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")