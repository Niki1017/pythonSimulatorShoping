import json
import os

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

        if os.path.exists(DEFAULT_FILE):
            self.load()
        else:
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

        # Данные о товарах магазина
        data_products = {
            "Хлеб": {
                "our_price": 50,                 # цена товара в магазине игрока
                "avg_market_price": 48,          # средняя рыночная цена товара
                "avg_competitor_price": 52,      # средняя цена товара у конкурентов
                "cost_price": 30,                # себестоимость (цена закупки товара)
                "quantity": 30                   # количество товара на складе
            },
            "Молоко": {
                "our_price": 80,                 # цена товара в магазине игрока
                "avg_market_price": 78,          # средняя рыночная цена товара
                "avg_competitor_price": 82,      # средняя цена товара у конкурентов
                "cost_price": 50,                # себестоимость (цена закупки товара)
                "quantity": 20                   # количество товара на складе
            },
            "Шоколад": {
                "our_price": 120,                # цена товара в магазине игрока
                "avg_market_price": 115,         # средняя рыночная цена товара
                "avg_competitor_price": 125,     # средняя цена товара у конкурентов
                "cost_price": 80,                # себестоимость (цена закупки товара)
                "quantity": 10                   # количество товара на складе
            }
        }

        # Сохранение основных параметров магазина в файл defaultSettings.json
        with open(DEFAULT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        # Сохранение информации о товарах в файл products.json
        with open(PRODUCTS, "w", encoding="utf-8") as f:
            json.dump(data_products, f, ensure_ascii=False, indent=4)


    def load(self):
        with open(DEFAULT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        with open(PRODUCTS, "r", encoding="utf-8") as fp:
            data_product = json.load(fp)

        self.nameShop = data.get("nameShop", "")
        self.balance = data.get("balance", 10000)
        self.reputation = data.get("reputation", 50)
        self.service = data.get("service", 1)
        self.advertising = data.get("advertising", 0)

    def indicator(self):
        print("Просмотр баланса и репутации в разработке")

    def pricing(self):
        print("Изменение цен у продуктов в разработке")

    def purchase(self):
        print("Закупка товаров в разработке")

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
                    exit()

                case _:
                    print("\nНеверный пункт меню")


if __name__ == "__main__":
    shop = Shop()
    shop.start()
