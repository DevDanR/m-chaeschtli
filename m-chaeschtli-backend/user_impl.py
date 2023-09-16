class FoodStore:
    def __init__(self):
        self.available_products: list[dict] | None = None

    def add_product(self, product):
        self.available_products.append(product)


class User:
    def __init__(self, customer_id="100007"):
        self.customer_id = customer_id
        self.food_store = FoodStore()
