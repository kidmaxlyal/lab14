class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=3):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.rating=rating
    def describe_restaurant(self):
        print(f"Ресторан называется {self.restaurant_name}")
        print(f"Тип кухни {self.cuisine_type}")
        print(f"Рейтинг {self.rating}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} открыт!")
    def update_rating(self, newrate):
        self.rating=newrate
        print(f"Рейтинг ресторана {self.restaurant_name} обновлен на {self.rating}")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, adres, time, rating=3):
        super().__init__(restaurant_name, "Кафе-мороженное", rating)
        self.flavors = ["шоколадное", "ванильное", "клубничное", "фисташковое"]
        self.adres=adres
        self.time=time
        self.tip={"На полочке":["Эскимо","Фруктовый лед"], "Мягкое":["в стаканчике","в рожке"]}
    def show_flavors(self):
       print("Вкусы мороженого")
       for flavor in self.flavors:
           print(f" - {flavor}")
    def upflavor(self,nowflavor):
        self.flavors.append(nowflavor)
        print(f"Добавлен новый вкус: {nowflavor}")
    def delflavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"{flavor} вкус удален")
        else:
            print(f"{flavor} вкус не найден")
    def findflavor(self,flavor):
        if flavor in self.flavors:
            print(f"{flavor} есть в наличии")
        else:
            print(f"{flavor} нет в наличии")
    def showadres(self):
        print(f"Адрес:{self.adres}")
        print(f"Время работы:{self.time}")
cafe=IceCreamStand("siuuu", "ул. Грибинюка 69","10:00-22:00","4.9")
cafe.describe_restaurant()
cafe.showadres()
cafe.show_flavors()
cafe.upflavor("Баблгам")
cafe.delflavor("Туттифрутти")
cafe.findflavor("фисташковое")