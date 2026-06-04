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
    def __init__(self, restaurant_name, rating=3):
        super().__init__(restaurant_name,"Кафе-мороженное", rating)
        self.flavors=["шоколадное","ванильное","клубничное","фисташковое"]
    def show_flavors(self):
       print("Вкусы мороженого")
       for flavor in self.flavors:
           print(f" - {flavor}")
cafe=IceCreamStand("siuuuu", 5)
cafe.describe_restaurant()
cafe.show_flavors()