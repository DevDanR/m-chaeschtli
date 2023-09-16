from flask import Flask, request
from db_operations import MigrosDb
from user_impl import User
from flask_cors import CORS, cross_origin
import numpy as np

app = Flask(__name__)
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

migros_db = MigrosDb(load_all=True)

# Create a dummy user and add some dummy data for demonstration
dummy_customer_id = "100007"
current_date_str = "2022-03-10"
user = User(customer_id=dummy_customer_id)
purchased_prods = migros_db.get_purchases_of_last_week(dummy_customer_id, current_date_str)
user.add_products_to_food_store(purchased_prods)
user.food_store.calc_co2_footprint()

# migros_db.product_db.check_for_similar_articles_with_lower_co2_footprint(user.food_store.available_products)
user.food_store.look_for_lower_co2_footprint_products(product_db=migros_db.product_db)

print(f"user co2 footprint: {user.food_store.co2_footprint}")
print(f"user co2 footprint best: {user.food_store.co2_footprint_best}")


@app.route('/customer_food_store', methods=['GET', 'POST'])
def customer_food_store():
    customer_id = request.args.get('KundeID') or dummy_customer_id
    return {"products_list": user.food_store.available_products}


@app.route('/customer_purchases', methods=['GET', 'POST'])
def customer_purchase_data():
    customer_id = request.args.get('KundeID') or dummy_customer_id
    return {"products_list": migros_db.get_purchased_articles_of_customer(customer_id)}


@app.route('/set_keepability', methods=['GET', 'POST'])
def set_keepability():
    product_id = request.data.decode('utf-8') or None
    if product_id is not None:
        new_keepability = int(request.args.get('new_keepability'))
        migros_db.set_keepability(product_id, new_keepability)


# @app.route('/get_purchases_of_last_week', methods=['GET', 'POST'])
# def get_purchases_of_last_week():
#     customer_id = int(request.args.get('KundeID') or 100007)
#     return {"test": "test"}


@app.route('/get_co2_footprint_trashed', methods=['GET', 'POST'])
def get_co2_footprint_trashed():
    prod_id = request.data.decode('utf-8')
    print(f"Received prod_id: {prod_id}")
    rnd = np.random.random(1)[0]
    return {"co2_footprint_customer": rnd}


@app.route('/get_co2_footprint_eaten', methods=['GET', 'POST'])
def get_co2_footprint_eaten():
    prod_id = request.data.decode('utf-8') or "100124500000"
    print(f"Received prod_id: {prod_id}")
    user.update_food_waste_indicator(prod_id)
    return {"co2_footprint_customer": user.food_waste_indicator}


@app.route('/get_food_waste_indicator_trashed', methods=['GET', 'POST'])
def get_food_waste_indicator_trashed():
    prod_id = request.data.decode('utf-8') or "100124500000"
    print(f"Received prod_id: {prod_id}")
    user.trash_product(prod_id)
    return {"food_waste_indicator_value": user.food_waste_indicator}


@app.route('/get_food_waste_indicator_eaten', methods=['GET', 'POST'])
def get_food_waste_indicator_eaten():
    prod_id = request.data.decode('utf-8')
    print(f"Received prod_id: {prod_id}")
    user.eat_product(prod_id)
    return {"food_waste_indicator_value": user.food_waste_indicator}


@app.route('/get_customer_co2_footprint', methods=['GET', 'POST'])
def get_customer_co2_footprint():
    customer_id = request.data.decode('utf-8') or dummy_customer_id
    print(f"Received customer_id: {customer_id}")
    return {"customer_co2_footprint": user.food_store.co2_footprint}


@app.route('/get_customer_co2_footprint_best', methods=['GET', 'POST'])
def get_customer_co2_footprint_best():
    customer_id = request.args.get('KundeID') or dummy_customer_id
    print(f"Received customer_id: {customer_id}")
    return {"customer_co2_footprint_best": user.food_store.co2_footprint_best}


@app.route('/get_product_recommendations', methods=['GET', 'POST'])
def get_product_recommendations():
    customer_id = request.args.get('KundeID') or dummy_customer_id
    print(f"Received customer_id: {customer_id}")
    return {"product_recommendations": user.food_store.recommended_products}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
