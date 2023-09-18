import numpy as np
from db_operations import ProductsDb, check_nested_key_exists


class FoodStore:
    def __init__(self):
        self.available_products: list[dict] | None = []
        self.co2_footprint = 0
        self.co2_footprint_best = 0
        self.recommended_products = {}

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

    def calc_co2_footprint(self):
        keys = ["m_check2", "carbon_footprint", "ground_and_sea_cargo", "kg_co2"]
        co2_footprints_filt = list(
            filter(lambda v: check_nested_key_exists(v, keys) is not None, self.available_products))
        co2_values = [p["m_check2"]["carbon_footprint"]["ground_and_sea_cargo"]["kg_co2"] for p in co2_footprints_filt]
        self.co2_footprint = np.sum(co2_values) + 2.6 * len(list(
            filter(lambda v: check_nested_key_exists(v, keys) is None, self.available_products)))

    def look_for_lower_co2_footprint_products(self, product_db: ProductsDb):
        related_prods = product_db.check_for_similar_articles_with_lower_co2_footprint(self.available_products)
        # Calculate the lower CO2 footprint if the customer would change
        co2_vals = []
        for prod in self.available_products:
            if check_nested_key_exists(prod,
                                       ["m_check2", "carbon_footprint", "ground_and_sea_cargo", "kg_co2"]) is not None:
                if prod['id'] in related_prods.keys():
                    co2_val = np.min(
                        [rel_prod["m_check2"]["carbon_footprint"]["ground_and_sea_cargo"]["kg_co2"] for rel_prod in
                         related_prods[prod['id']]])
                else:
                    co2_val = prod["m_check2"]["carbon_footprint"]["ground_and_sea_cargo"]["kg_co2"]
            else:
                co2_val = 2.6  # Average value
            co2_vals.append(co2_val)

        prod_recommendations = [(self.get_product_by_id(prod_id), items) for prod_id, items in related_prods.items()]
        self.recommended_products = prod_recommendations
        self.co2_footprint_best = np.sum(co2_vals)


class User:
    def __init__(self, customer_id="100007"):
        self.customer_id = customer_id
        self.food_store = FoodStore()
        self.food_waste_indicator = 5  # Initial value

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

        self.food_waste_indicator += co2_footprint_val*10  # *10 for demonstration to make it a bit more visible
        self.food_store.remove_products([product])
