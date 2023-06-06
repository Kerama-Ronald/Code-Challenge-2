from review import Review

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        customer_list = []
        for review in self.reviews:
            customer = review.customer()
            if customer not in customer_list:
                customer_list.append(customer)
        return customer_list

    def average_star_rating(self):
        total_rating = sum(review.rating for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews > 0:
            return total_rating / num_reviews
        return 0

    @classmethod
    def all(cls):
        return cls.all_restaurants
