from flask import Flask, request
from db_operations import MigrosDb
from user_impl import User

app = Flask(__name__)

migros_db = MigrosDb(load_all=True)
customer = User()

@app.get('/customer_purchases')
def customer_purchase_data():
    customer_id = int(request.args.get('KundeID') or 100007)
    return {"products_list": migros_db.get_purchased_articles_of_customer(customer_id)}


@app.get('/get_purchases_of_last_week')
def list_programming_languages():
    return {"programming_languages": "test"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
