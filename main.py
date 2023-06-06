from customer import Customer
from restaurant import Restaurant
from review import Review

customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Pizza Place")
restaurant2 = Restaurant("Burger Joint")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer1, restaurant2, 5)
review3 = Review(customer2, restaurant1, 3)

print(customer1.restaurants())
print(restaurant1.customers())
print(restaurant1.average_star_rating())
