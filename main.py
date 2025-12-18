import json
import os

from products import data_products

DEFAULT_FILE = "defaultSettings.json"
PRODUCTS = "products.json"


options = [
"1 — посмотреть баланс и репутацию",
"2 — изменить цену товара",
"3 — закупить товары",
"4 — улучшить сервис (−500 денег, +1 сервис)",
"5 — вложиться в рекламу (−300 денег, +1 реклама)",
"6 — завершить день",
"0 — выход из игры"
]


class Shop:
    def __init__(self, nameShop="", balance=10000, reputation=50, service=1, advertising=0):
        self.nameShop = nameShop
        self.balance = balance
        self.reputation = reputation
        self.service = service
        self.advertising = advertising
        self.products = {}


        if os.path.exists(DEFAULT_FILE):
            self.load()
        else:
            self.products = data_products
            self.save()

    def save(self):
        # Данные состояния магазина (основные параметры игрока)
        data = {
            "nameShop": self.nameShop,      # название магазина
            "balance": self.balance,        # текущий баланс магазина
            "reputation": self.reputation,  # репутация магазина (влияет на выбор покупателей)
            "service": self.service,        # уровень сервиса магазина
            "advertising": self.advertising # уровень рекламы магазина
        }


        # Сохранение основных параметров магазина в файл defaultSettings.json
        with open(DEFAULT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        # Сохранение информации о товарах в файл products.json
        with open(PRODUCTS, "w", encoding="utf-8") as f:
            json.dump(self.products, f, ensure_ascii=False, indent=4)


    def load(self):
        with open(DEFAULT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        with open(PRODUCTS, "r", encoding="utf-8") as fp:
            data_product = json.load(fp)
            self.products = data_product


        self.nameShop = data.get("nameShop", "")
        self.balance = data.get("balance", 10000)
        self.reputation = data.get("reputation", 50)
        self.service = data.get("service", 1)
        self.advertising = data.get("advertising", 0)

    def indicator(self):
        print("\nТекущее состояние магазина")
        print(f"Баланс: {self.balance}")
        print(f"Репутация: {self.reputation}")
        print(f"Сервис: {self.service}")
        print(f"Реклама: {self.advertising}")

    def pricing(self):
        print("Изменение цен у продуктов в разработке")

    def purchase(self):
        print("\nЗакупка товаров:\n")

        products = list(self.products.keys())

        for i, product in enumerate(products, start=1):
            details = self.products[product]
            print(f"{i}. {product} - {details['cost_price']}")

        print()

        try:
            assortment = int(input("Товар: "))
        except ValueError:
            print("Ошибка: введите номер товара")
            return

        if 1 <= assortment <= len(products):
            product_name = products[assortment - 1]
            product_data = self.products[product_name]

            print(
                f"\nВы выбрали: {product_name}\n"
                f"Цена закупки: {product_data['cost_price']}"
            )

            quantity = int(input("Количество продукта: "))

            if not self.balance <= 0:
                if product_data['cost_price'] * quantity > self.balance:
                    print("Недосаточн денег")
                else:
                    self.balance -= product_data['cost_price'] * quantity
                    print(
                        f"\nУспешно!\n"
                        f"Списано: {product_data['cost_price']*quantity}\n"
                        f"Баланс: {self.balance}\n"
                    )

        else:
            print("Ошибка: такого товара нет")
    def upgrade_service(self):
        print("Улучшение сервиса в разработке")

    def reklama(self):
        print("Вложеиние в рекламу в разработке")

    def end_day(self):
        print("Завершение дня в разработке")

    def show_menu(self):
        print("═" * 30)
        for opt in options:
            print(opt)
        print("═" * 30)

    def start(self):
        if self.nameShop == "":
            self.nameShop = input("Введите название магазина: ")
            self.balance -= 9000
            self.save()
        else:
            print(f"\nМагазин «{self.nameShop}» успешно загружен\n")

        while self.balance > 0:
            self.show_menu()

            if self.balance > 120000 and self.reputation > 80:
                print("Ваш магазин популярный, вы прошли игру")
                exit()

            try:
                option = int(input("Выберите номер действия: "))
            except ValueError:
                print("Ошибка: введите число\n")
                continue
            except Exception as e:
                print(f"Error: {e}")

            match option:
                case 1:
                    self.indicator()

                case 2:
                    self.pricing()

                case 3:
                    self.purchase()

                case 4:
                    self.upgrade_service()

                case 5:
                    self.reklama()
                
                case 6:
                    self.end_day()
                
                case 0:
                    print("Вы завершили работу программы.")
                    break 

                case _:
                    print("\nНеверный пункт меню")
        print("У вас не остаось денег и вы умерли с голоду")

if __name__ == "__main__":
    shop = Shop()
    shop.start()
