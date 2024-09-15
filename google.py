import requests
from bs4 import BeautifulSoup
import csv

# URL of the Flipkart product page to scrape
url = 'https://www.flipkart.com/canon-r100-mirrorless-camera-rf-s-18-45mm-f-4-5-6-3-stm/p/itm3bc65ea11d81b?pid=DLLGQAQYNT39ZJTG&lid=LSTDLLGQAQYNT39ZJTGZBMZBW&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_1&otracker=browse&fm=organic&iid=40a9c68c-e9c0-4fc6-ba6c-eb16361f7c64.DLLGQAQYNT39ZJTG.SEARCH&ppt=browse&ppn=browse&ssid=5gkdlbgrts0000001726297160272'

session = requests.Session()

# Add headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
}

# Send a GET request with the session
response = session.get(url, headers=headers)
# Check if the request was successful
if response.status_code == 200:
    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title of the product
    title_tag = soup.find('span', class_='VU-ZEz')
    title = title_tag.text if title_tag else 'No title found'

    # Find the price of the product
    price_tag = soup.find('div', class_='Nx9bqj CxhGGd')
    price = price_tag.text if price_tag else 'No price found'

    # Print the data
    print(f'Title: {title}')
    print(f'Price: {price}')
    print('-' * 40)

    # Define CSV file path
    csv_file = 'flipkart_products.csv'

    # Open the CSV file in write mode
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        # Create a writer object
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['Title', 'Price'])

        # Write the product details
        writer.writerow([title, price])

    print(f'Data has been written to {csv_file}')

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
