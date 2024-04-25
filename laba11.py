class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("Ресторан: ", self.restaurant_name)
        print("Тип кухни: ", self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан открыт!")
newRestaurant = Restaurant("Pappone", "Европейская кухня")
print("Название ресторана:", newRestaurant.restaurant_name)
print("Тип кухни:", newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
#11.2
res1 = Restaurant("Olivka", "Итальянская")
res2 = Restaurant("Geraldine", "Французская")
res3 = Restaurant("Sintoho", "Китайская")
res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()


#11.3
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, initial_rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.initial_rating = initial_rating
    def describe_restaurant(self):
        print("Ресторан: ", self.restaurant_name)
        print("Тип кухни: ", self.cuisine_type)
        print("Рейтинг: ", self.initial_rating)
    def open_restaurant(self):
        print("Ресторан открыт!")
    def rating(self):
        print("Первоначальный рейтинг:", self.initial_rating)
    def update_rating(self, new_rating):
        self.initial_rating = new_rating
        print("Новый рейтинг:", new_rating)
newRestaurant = Restaurant("Pappone", "Европейская кухня", 3)
print("Название ресторана:", newRestaurant.restaurant_name)
print("Тип кухни:", newRestaurant.cuisine_type)
print("Рейтинг:", newRestaurant.initial_rating)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
newRestaurant.rating()
newRating = 5
newRestaurant.update_rating(newRating)
newRestaurant.rating()