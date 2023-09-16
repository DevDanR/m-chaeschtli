from flask import Flask, request
from db_operations import MigrosDb
from user_impl import User

from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

migros_db = MigrosDb(load_all=False)
customer = User()


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


@app.route('/get_purchases_of_last_week')
@cross_origin()
def list_programming_languages():
    return {"programming_languages": "test"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
