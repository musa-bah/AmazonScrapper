from bs4 import BeautifulSoup
import requests

# GET THE COMPUTER USER AGENT.
agent = {'UserAgent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
         "Chrome/75.0.3770.142 Safari/537.36"}


class VerticalListings:
    def __init__(self, product_name):
        self.product_name = product_name
        self.product_names_list = []
        self.product_prices_list = []
        self.URL = "https://www.amazon.com/s?k={}&ref=nb_sb_noss_2".format(product_name)
        self.site = requests.get(self.URL, headers=agent)
        self.soup = BeautifulSoup(self.site.content, "lxml")
        self.product_listings = self.soup.findAll("div", {"class": "sg-col-20-of-24 s-result-item sg-col-0-of-12 "
                                                                   "sg-col-28-of-32 sg-col-16-of-20 sg-col "
                                                                   "sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"})

    def product_names(self):
        product_listings = self.product_listings
        for products in range(len(product_listings)):
            try:
                single_product_name = product_listings[products].find('span', {'class': 'a-size-medium a-color-base '
                                                                                        'a-text-normal'}).text
            except AttributeError:
                continue

            self.product_names_list.append(single_product_name)
        return '\n'.join(self.product_names_list)


    def product_price(self):
        product_listings = self.product_listings
        for products in range(len(product_listings)):
            try:
                single_product_price = product_listings[products].find('span', {'data-a-size': 'l'}).find('span',
                                                                               {'class': 'a-offscreen'}).text
            except AttributeError:
                continue

            self.product_prices_list.append(single_product_price)
        return '\n'.join(self.product_prices_list)


class HorizontalListings:
    def __init__(self, product_name):
        self.product_name = product_name
        self.product_names_list = []
        self.product_prices_list = []
        self.URL = "https://www.amazon.com/s?k={}&ref=nb_sb_noss_1".format(product_name)
        self.site = requests.get(self.URL, headers=agent)
        self.soup = BeautifulSoup(self.site.content, "lxml")
        self.product_listings = self.soup.findAll("div", {"class": "sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 "
                                                          "s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col "
                                                          "sg-col-4-of-20 sg-col-4-of-32"})

    def product_names(self):
        product_listings = self.product_listings
        for products in range(len(product_listings)):
            try:
                single_product_name = product_listings[products].find('span', {'class': 'a-size-base-plus '
                                                                               'a-color-base a-text-normal'}).text
            except AttributeError:
                continue

            self.product_names_list.append(single_product_name)
        return '\n'.join(self.product_names_list)

    def product_price(self):
        product_listings = self.product_listings
        for products in range(len(product_listings)):
            try:
                single_product_price = product_listings[products].find('span', {'data-a-size': 'l'}).find('span',
                                                                               {'class': 'a-offscreen'}).text
            except AttributeError:
                continue

            self.product_prices_list.append(single_product_price)
        return '\n'.join(self.product_prices_list)


product = input('What product are you searching for?')
productsH = HorizontalListings(product)
productV = VerticalListings(product)

print(productsH.product_names())
print(productsH.product_price())
print(productV.product_names())
print(productV.product_price())




# wrap applications which are running a browser inside them

# A search for phone cases returns nill. Add a costume class for this.
#
# agent = {"UerAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
#
# URL = "https://en.wikipedia.org/wiki/ADFS"
# site = requests.get(URL, headers=agent)
# soup = BeautifulSoup(site.content, "lxml")
# print(soup)
