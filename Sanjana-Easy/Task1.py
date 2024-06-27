import requests
from bs4 import BeautifulSoup
import csv
import json

# URL to fetch
url = "https://www.techadvisor.com/article/724318/best-smartphone.html"

# Perform the HTTP GET request
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the phone names
phones = soup.find_all(class_='product-chart-item__title-wrapper--title')
phone_names = [h2.get_text(strip=True) for h2 in phones]

# Initialize lists for pros and cons
all_pros = []
all_cons = []

# Extract the pros and cons lists
pros_divs = soup.find_all('div', class_='product-chart-column')
for div in pros_divs:
    title = div.find('p', class_='product-chart-subTitle').get_text(strip=True)
    ul = div.find('ul', class_='product-pros-cons-list')
    if title == 'Pros':
        pros = [li.get_text(strip=True) for li in ul.find_all('li')]
        all_pros.append(pros)
    elif title == 'Cons':
        cons = [li.get_text(strip=True) for li in ul.find_all('li')]
        all_cons.append(cons)

# Combine the phone names, pros, and cons into a structured format
phones_data = []
for phone_name, pros, cons in zip(phone_names, all_pros, all_cons):
    phone_data = {
        "phone": phone_name,
        "pros": pros,
        "cons": cons
    }
    phones_data.append(phone_data)

# Print the combined data
for phone in phones_data:
    print(f"Phone: {phone['phone']}")
    print("Pros:")
    for pro in phone['pros']:
        print(f"  - {pro}")
    print("Cons:")
    for con in phone['cons']:
        print(f"  - {con}")
    print('-------------------')

# Save the structured data to JSON
with open('phones_data.json', 'w',encoding='utf-8') as jsonfile:
    json.dump(phones_data, jsonfile, indent=4)

print("Extracted data saved to phones_data.json")

# Save the structured data to CSV
with open('phones_data.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Phone", "Pros", "Cons"])
    for phone in phones_data:
        pros = "; ".join(phone["pros"])
        cons = "; ".join(phone["cons"])
        writer.writerow([phone["phone"], pros, cons])

print("Extracted data saved to phones_data.csv")