class FoodStore:
    def __init__(self):
        self.available_products: list[dict] | None = []

    def add_products(self, products):
        self.available_products.extend(products)

    def remove_products(self, products):
        prod_ids = [prd['id'] for prd in products]
        remove_prods = []
        for k in range(len(self.available_products)):
            if self.available_products[k]['id'] in prod_ids:
                remove_prods.append(self.available_products[k])

        for prod in remove_prods:
            self.available_products.remove(prod)

    def get_product_by_id(self, prod_id):
        found_prod = {}
        for prod in self.available_products:
            if prod['id'] == prod_id:
                found_prod = prod
                break
        return found_prod


class User:
    def __init__(self, customer_id="100007"):
        self.customer_id = customer_id
        self.food_store = FoodStore()
        self.co2_footprint = 0
        self.food_waste_indicator = 0

    def eat_product(self, prod_id):
        prod = self.food_store.get_product_by_id(prod_id)
        self.update_food_waste_indicator(prod, trashed=False)

    def trash_product(self, prod_id):
        prod = self.food_store.get_product_by_id(prod_id)
        self.update_food_waste_indicator(prod, trashed=True)

    def add_products_to_food_store(self, products):
        self.food_store.add_products(products)

    def update_food_waste_indicator(self, product, trashed):
        keys = ['carbon_footprint', 'ground_and_sea_cargo', 'kg_co2']
        co2_footprint = product.get('m_check2', None)
        for key in keys:
            if co2_footprint is not None:
                co2_footprint = co2_footprint.get(key, None)
            else:
                break
        if co2_footprint is None:
            co2_footprint = 2.6  # Average value
        if trashed:
            co2_footprint_val = -co2_footprint
        else:
            co2_footprint_val = co2_footprint

        self.food_waste_indicator += co2_footprint_val
        self.food_store.remove_products([product])


