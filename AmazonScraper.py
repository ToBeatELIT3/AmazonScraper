#ToBeatElite
from urllib.request import urlopen as u_Req
from bs4 import BeautifulSoup as soup

def start():
    search_query = input("Amazon Web Scraper V1\nEnter \"00QUIT00\" To Exit\nEnter Query: ").replace(" ", "")

    if search_query == "00QUIT00": quit()

    try: main(search_query)
    except: print("An Error Occured, Sorry!\n")

def main(query):

    u_Client = u_Req(f"https://www.amazon.ca/s?k={query}")
    page_html = u_Client.read()
    u_Client.close()

    page_soup = soup(page_html, "html.parser")

    item_name = page_soup.findAll("span", class_="a-size-medium a-color-base a-text-normal")
    item_rating = page_soup.findAll("span", class_="a-icon-alt")
    item_price = page_soup.findAll("span", class_="a-offscreen")

    for x in range(len(item_name)):
        print(f"******\nItem Name   : {item_name[x].text.strip()}\nItem Cost   : {item_price[x].text.strip()}\nItem Rating : {item_rating[x].text.strip()}\n")

if __name__ == "__main__":
    while True: start()
    