import requests
import csv
from bs4 import BeautifulSoup
import os

def request_parser(url):
    # url = "https://books.toscrape.com/index.html"
    request = requests.get(url)
    if request.ok:
        return BeautifulSoup(request.content, 'html.parser')


special_characters = ['../', ';', ' ']
headers = ["Title", "UPC", "Price including tax", "Price excluding tax", "Avaibility", "product Description", "Tax",
           "book_category", "review_rating", "image_url"]
categories_name = ["Travel", "Mystery", "Historical Fiction", "Sequential Art", "Classics", "Philosophy", "Romance",
                   "Womens Fiction", "Fiction", "Childrens", "Religion", "Nonfiction",
                   "Music", "Default", "Science Fiction", "Sports and Games", "Add a comment", "Fantasy",
                   "New Adult", "Young Adult", "Science", "Poetry", "Paranormal", "Art", "Psychology",
                   "Autobiography", "Parenting", "Adult Fiction", "Humor", "Horror", "History", "Food and Drink",
                   "Christian Fiction", "Business", "Biography", "Thriller", "Contemporary",
                   "Spirituality", "Academic", "Self Help", "Historical", "Christian", "Suspense", "Short Stories",
                   "Novels", "Health", "Politics", "Cultural", "Erotica", "Crime"
                   ]


# fonction qui renvoie les liens des catégories
def category():
    url = "https://books.toscrape.com/index.html"
    category_link_short = []
    category_link = []
    for a in request_parser(url).select('li > a'):
        category_link.append("https://books.toscrape.com/" + a['href'])
        category_link_short.append(a['href'])
    category_link_short.pop(1)
    category_link.pop(1)
    category_link_short.pop(0)
    category_link.pop(0)
    category_link_short.pop()
    category_link.pop()
    return category_link_short, category_link


all_link_short_categories, all_link_categories = category()

# fonction qui scan les liens des catégories, fait la pagination et retour tout les liens des livres


def onecategorybooks(categoryUrl):
    books_of_category = []
    url = categoryUrl
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


pages = []
for category in all_link_categories:
    pages.append(onecategorybooks(category))


# print(pages[0][0])

def get_book_bycategory():
    for index, row in enumerate(pages):
        with open("{}.csv".format(categories_name[index]), "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            rows = []
            for link in pages[index]:
                page_soup = request_parser(link)
                # print(page_soup)
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


def get_images():
    all_title = []
    all_images = []
    path = os.getcwd()
    os.mkdir("images")
    os.chdir(os.path.join(path, "images"))
    for index, row in enumerate(pages):
        for link in pages[index]:
            page_soup = request_parser(link)
            title = page_soup.find("h1").text
            image_url = page_soup.find('div', class_="item active").img['src']
            image_url = "http://books.toscrape.com/" + image_url.replace('../', '')
            all_images.append(image_url)
            all_title.append(title)
            with open(f'{title}.jpg', 'ab') as file:
                for image in all_images:
                    r = requests.get(image).content
                file.write(r)


get_images()


