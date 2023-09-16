from flask import Flask, request
from db_operations import MigrosDb
from user_impl import User
from flask_cors import CORS, cross_origin
import numpy as np

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

migros_db = MigrosDb(load_all=False)
customer = User()


@app.route('/customer_food_store')
@cross_origin()
def customer_food_store():
    customer_id = int(request.args.get('KundeID') or 100007)
    return {"products_list": migros_db.get_purchased_articles_of_customer(customer_id)}


@app.route('/customer_purchases')
@cross_origin()
def customer_purchase_data():
    customer_id = int(request.args.get('KundeID') or 100007)
    return {"products_list": migros_db.get_purchased_articles_of_customer(customer_id)}


@app.route('/set_keepability')
@cross_origin()
def set_keepability():
    product_id = request.args.get('product_id') or None
    if product_id is not None:
        new_keepability = int(request.args.get('new_keepability'))
        migros_db.set_keepability(product_id, new_keepability)


@app.route('/get_purchases_of_last_week')
@cross_origin()
def get_purchases_of_last_week():
    customer_id = int(request.args.get('KundeID') or 100007)
    return {"programming_languages": "test"}


@app.route('/get_co2_footprint_trashed')
@cross_origin()
def get_co2_footprint_trashed():
    prod_id = request.args.get('prodID')
    rnd = np.random.random(1)[0]
    return {"co2_footprint_customer": rnd}


@app.route('/get_co2_footprint_eaten')
@cross_origin()
def get_co2_footprint_eaten():
    prod_id = request.args.get('prodID')
    rnd = np.random.random(1)[0]
    return {"co2_footprint_customer": rnd}


@app.route('/get_food_waste_indicator_trashed')
@cross_origin()
def get_food_waste_indicator_trashed():
    prod_id = request.args.get('prodID')
    rnd = np.random.random(1)[0]
    return {"food_waste_indicator_value": rnd}


@app.route('/get_food_waste_indicator_eaten')
@cross_origin()
def get_food_waste_indicator_eaten():
    prod_id = request.args.get('prodID')
    rnd = np.random.random(1)[0]
    return {"food_waste_indicator_value": rnd}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
