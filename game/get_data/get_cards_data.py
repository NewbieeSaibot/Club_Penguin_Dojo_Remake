from selenium.webdriver import Firefox
from time import sleep
import pandas as pd
import requests

cards_dict = {
    "id_card": [],
    "name": [],
    "element": [],
    "force": [],
    "comment": [],
    "set": [],
    "image_path": [],
    "power": [],
}

normal_cards_link = "https://clubpenguin.fandom.com/wiki/List_of_Regular_Card-Jitsu_Cards_(series_1-4)#card_2"
power_cards_link = "https://clubpenguin.fandom.com/wiki/List_of_Card-Jitsu_Power_Cards"
image_path = "../data/images/cards/"
browser = Firefox()

browser.get(normal_cards_link)
tbody = browser.find_elements_by_tag_name("tbody")[1]

trs = tbody.find_elements_by_tag_name("tr")

for i in range(len(trs)):
    tds = trs[i].find_elements_by_tag_name("td")

    cards_dict["id_card"].append(tds[0].text)
    cards_dict["name"].append(tds[1].text)
    cards_dict["set"].append(tds[7].text)
    cards_dict["comment"].append(tds[8].text)

    cards_dict["power"].append(False)
    a = tds[4].find_element_by_tag_name("a")
    element = a.get_attribute("title")
    cards_dict["element"].append(element)
    img = tds[5].find_element_by_tag_name("img")
    force = str(img.get_attribute("alt")).split(sep=' ')[1].split(sep='.')[0]
    cards_dict["force"].append(force)
    a = tds[3].find_element_by_tag_name("a")
    card_image_link = a.get_attribute("href")
    image_name = card_image_link.split(sep="/")[7]
    cards_dict["image_path"].append("./data/images/cards/" + image_name)
    response = requests.get(card_image_link)
    file = open(image_path + image_name, "wb")
    file.write(response.content)
    file.close()

browser.get(power_cards_link)
sleep(4)
tbody = browser.find_elements_by_tag_name("tbody")[1]

trs = tbody.find_elements_by_tag_name("tr")

for i in range(len(trs)):
    tds = trs[i].find_elements_by_tag_name("td")

    cards_dict["id_card"].append(tds[0].text)
    cards_dict["name"].append(tds[1].text)
    cards_dict["set"].append(tds[8].text)
    cards_dict["comment"].append(tds[9].text)
    cards_dict["power"].append(True)
    a = tds[4].find_element_by_tag_name("a")
    element = a.get_attribute("title")
    cards_dict["element"].append(element)
    img = tds[5].find_element_by_tag_name("img")
    force = str(img.get_attribute("alt")).split(sep=' ')[1].split(sep='.')[0]
    cards_dict["force"].append(force)
    a = tds[3].find_element_by_tag_name("a")
    card_image_link = a.get_attribute("href")
    image_name = card_image_link.split(sep="/")[7]
    cards_dict["image_path"].append("./data/images/cards/" + image_name)
    response = requests.get(card_image_link)
    file = open(image_path + image_name, "wb")
    file.write(response.content)
    file.close()

df = pd.DataFrame(cards_dict)
df.to_csv("../data/info/cards.csv")
