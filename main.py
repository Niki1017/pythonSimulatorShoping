import json
import os

DEFAULT_FILE = "defaultSettings.json"

class Shop:
    def __init__(self, nameShop="", balance=10000, reputation=50, service=1, advertising=0):
        self.nameShop = nameShop
        self.balance = balance
        self.reputation = reputation
        self.service = service
        self.advertising = advertising

        if not os.path.exists(DEFAULT_FILE):
            self.save()
        else:
            self.load()

    def save(self):
        data = {
            "nameShop": self.nameShop,
            "balance": self.balance,
            "reputation": self.reputation,
            "service": self.service,
            "advertising": self.advertising
        }
        with open(DEFAULT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self):
        with open(DEFAULT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.nameShop = data["nameShop"]
        self.balance = data["balance"]
        self.reputation = data["reputation"]
        self.service = data["service"]
        self.advertising = data["advertising"]



    def start(self):
        if self.nameShop == "":
            self.nameShop = input("Ввелите название магазина: ")
            self.save()
        print(f"Импортирован магазн {self.nameShop}")

if __name__ == "__main__":
    shop = Shop()
    shop.start()
    shop.load()

























# class Products:
#     def __init__(self, products, product_price, cost_price, quantity): 
#         товар,цена ытовара,себестоимость,количество
#         self.products = products
#         self.product_price = product_price
#         self.cost_price = cost_price
#         self.quantity = quantity

#     def all_products(self): 
#         products = self.products
