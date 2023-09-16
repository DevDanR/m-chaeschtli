from flask import Flask, request
from db_operations import MigrosDb
from user_impl import User
from flask_cors import CORS, cross_origin
import numpy as np

app = Flask(__name__)
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

migros_db = MigrosDb(load_all=False)


# Create a dummy user and add some dummy data for demonstration
dummy_customer_id = 100007
current_date_str = "2022-03-26"
user = User(customer_id=dummy_customer_id)
purchased_prods = migros_db.get_purchases_of_last_week(dummy_customer_id, current_date_str)
user.add_products_to_food_store(purchased_prods)


@app.route('/customer_food_store', methods=['GET', 'POST'])
def customer_food_store():
    customer_id = int(request.args.get('KundeID') or 100007)
    return {"products_list": migros_db.get_purchased_articles_of_customer(customer_id)}


@app.route('/customer_purchases', methods=['GET', 'POST'])
def customer_purchase_data():
    customer_id = int(request.args.get('KundeID') or 100007)
    return {"products_list": migros_db.get_purchased_articles_of_customer(customer_id)}


@app.route('/set_keepability', methods=['GET', 'POST'])
def set_keepability():
    product_id = request.args.get('product_id') or None
    if product_id is not None:
        new_keepability = int(request.args.get('new_keepability'))
        migros_db.set_keepability(product_id, new_keepability)


@app.route('/get_purchases_of_last_week', methods=['GET', 'POST'])
def get_purchases_of_last_week():
    customer_id = int(request.args.get('KundeID') or 100007)
    return {"programming_languages": "test"}


@app.route('/get_co2_footprint_trashed', methods=['GET', 'POST'])
def get_co2_footprint_trashed():
    prod_id = request.args.get('prodID')
    print(f"Received prod_id: {prod_id}")
    rnd = np.random.random(1)[0]
    return {"co2_footprint_customer": rnd}


@app.route('/get_co2_footprint_eaten', methods=['GET', 'POST'])
def get_co2_footprint_eaten():
    prod_id = request.args.get('prodID')
    print(f"Received prod_id: {prod_id}")
    rnd = np.random.random(1)[0]
    return {"co2_footprint_customer": rnd}


@app.route('/get_food_waste_indicator_trashed', methods=['GET', 'POST'])
def get_food_waste_indicator_trashed():
    prod_id = request.args.get('prodID')
    print(f"Received prod_id: {prod_id}")
    rnd = np.random.random(1)[0]
    return {"food_waste_indicator_value": rnd}


@app.route('/get_food_waste_indicator_eaten', methods=['GET', 'POST'])
def get_food_waste_indicator_eaten():
    prod_id = request.args.get('prodID')
    print(f"Received prod_id: {prod_id}")
    rnd = np.random.random(1)[0]
    return {"food_waste_indicator_value": rnd}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
