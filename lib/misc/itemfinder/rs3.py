from bs4 import BeautifulSoup
import requests
from time import time
import os
import urllib.request

BASE_URL = "https://runescape.wiki"
IMAGE_DIR = "/home/droop/Documents/Python/images/"
LIST_DIR = "/home/droop/Documents/Python/item_list.txt"

def grab_page_links(cur_url):
    try:
        r = requests.get(BASE_URL + cur_url)
        soup = BeautifulSoup(r.text)

        next_page_section = soup.find(class_="mw-allpages-nav")
        if next_page_section is None:
            next_page = ""
        else:
            a_tag = next_page_section.find_all("a")[-1]
            if "Previous" in a_tag.string:
                next_page = ""
            else:
                next_page = a_tag.get("href")

        table = soup.find(class_="mw-allpages-body")

        items = table.find_all("li")

        resp = {i.a.get('href') for i in items if i.a is not None}
        return next_page, sorted(resp)
    except Exception as ex:
        print("Error {ex} on page {pg}".format(ex=str(ex), pg=cur_url))
        raise


def parse_page(url):
    try:
        r = requests.get(BASE_URL + url)
        soup = BeautifulSoup(r.text)

        name = url.replace("/w/Exchange:", "").replace("_", " ")
        itemID = soup.find(class_="gemw-property gemw-id").dd.string
        imageURL = soup.find(class_="gemw-image inventory-image").img['src']
        result = {"name": name, "itemID": itemID, "imageURL": imageURL}
        return result
    except:
        return None

def download_image(id, url):
    print(BASE_URL + url)
    # urllib.request.urlretrieve(BASE_URL + url, IMAGE_DIR + id + ".png")
    page = requests.get(BASE_URL + url)

    f_name = '{}{}.png'.format(IMAGE_DIR, id)
    with open(f_name, 'wb') as f:
        f.write(page.content)


def do_parse():
    with open(LIST_DIR, "r") as f:
        existing = {a.strip() for a in f.readlines() if "/nil/" not in a}
        names = []
        ids = []
        for line in existing:
            if len(line) == 0:
                continue
            split_line = line.split('/')
            names.append(split_line[1])
            ids.append(split_line[0])

    start = time()
    i = 0
    next_page = "/w/Special:AllPages?from=&to=&namespace=112"

    while next_page != "":
        next_page, full_index = grab_page_links(next_page)
        for page in full_index:

            i += 1
            if i % 500 == 0:
                x = (time() - start)
                print("After {I} items, it has been {x} seconds, {y} seconds per item".format(I=i, x=x,
                                                                                              y=round(x / i, 3)))

            tmp_name = page.replace("/w/Exchange:", "").replace("_", " ").replace("%27", "'").replace("%26", "&").replace("%2B", "+")
            in_list = tmp_name in names
            if in_list:
                continue

            item = parse_page(page)
            if item is None:
                continue

            in_list = item['itemID'] in ids
            if in_list:
                continue

            item['name'] = item['name'].replace("%27", "'").replace("%26", "&").replace("%2B", "+").replace("_", " ")

            download_image(item['itemID'], item['imageURL'])

            with open(LIST_DIR, "a") as f:
                f.write(
                    "{name}={id}\r\n".format(id=item['itemID'], name=item['name']))


do_parse()