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

def onecategorybooks():
    books_of_category = []
    url = "https://books.toscrape.com/catalogue/category/books/young-adult_21/index.html"
    links = []
    request = request_parser(url)
    for book in request.select('h3 > a'):
        end_link = book['href']
        full_link = "https://books.toscrape.com/catalogue/" + end_link.replace('../', '')
        links.append(full_link)
    for numb in range(2, 10):
        all_pages = url.replace("index.html", f'page-{numb}.html')
        request2 = requests.get(all_pages)
        if not request2.ok:
            break
        books_of_category.append(url)
        books_of_category.append(all_pages)
        soup = BeautifulSoup(request2.content, 'html.parser')
        for additional_book in soup.select('h3 > a'):
            end_link_add = additional_book['href']
            full_add_link = "https://books.toscrape.com/catalogue/" + end_link_add.replace('../', '')
            links.append(full_add_link)
    return links


def get_book_bycategory():
    with open("onecategory.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        rows = []
        for link in onecategorybooks():
            page_soup = request_parser(link)
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
            rows.append(new_list)
        writer.writerows(rows)


get_book_bycategory()
