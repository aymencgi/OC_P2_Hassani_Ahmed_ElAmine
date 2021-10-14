import requests
import csv
from bs4 import BeautifulSoup
import os


def request_parser(url):
    request = requests.get(url)
    if request.ok:
        return BeautifulSoup(request.content, 'html.parser')


special_characters = ['../', ';', ' ']
headers = ["Title", "UPC", "Price including tax", "Price excluding tax", "Avaibility", "product Description", "Tax",
           "book_category", "review_rating", "image_url"]


def onebook():
    url = "https://books.toscrape.com/catalogue/the-requiem-red_995/index.html"
    page_soup = request_parser(url)
    bookshelf = page_soup.find_all("td")
    title = page_soup.find("h1").text
    new_list = [x.text for x in bookshelf]
    new_list.insert(0, title)
    review_rating = page_soup.find_all("p", class_="star-rating")[0].get("class")[1]
    if review_rating:
        new_list.append(review_rating)
    else:
        new_list.append("No star review")

    image_url = page_soup.find('div', class_="item active").img['src']
    image_url = "http://books.toscrape.com/" + image_url.replace('../', '')
    new_list.append(image_url)
    with open(f"{title}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        rows = []
        rows.append(new_list)
        writer.writerows(rows)


onebook()
