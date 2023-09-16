from pyunpack import Archive
import os
from tqdm import tqdm
import shutil
import json
import pandas as pd


class ProductsDb:
    def __init__(self, data_folder="Migros_case", amount_to_load=2000):
        self.data_folder = data_folder
        products_folder = r"products"
        data_extract_folder = os.path.join(os.path.dirname(__file__), "..", "..")

        for path in os.walk(data_folder):
            create_path = os.path.join(data_extract_folder, path[0])
            if not os.path.exists(create_path):
                os.mkdir(create_path)
            for subfolder in path[1]:
                if not os.path.exists(os.path.join(create_path, subfolder)):
                    os.mkdir(os.path.join(create_path, subfolder))
            print(f"Checking files to extract:\n{path[2]}\n")
            for file in tqdm(path[2]):
                if file.split('.')[1] == '7z':
                    extract_path = os.path.join(create_path, file.split('.')[0])
                    if not os.path.exists(extract_path):
                        os.mkdir(extract_path)
                        Archive(os.path.join(path[0], file)).extractall(extract_path)
                else:
                    extract_path = os.path.join(create_path, file)
                    shutil.copyfile(os.path.join(path[0], file), extract_path)

        products_files_folder = os.path.join(data_extract_folder, data_folder, products_folder, 'products_de', 'de')
        print("Loading products\n")
        self.products = []
        for file in tqdm(os.listdir(products_files_folder)[:amount_to_load]):
            file_path = os.path.join(products_files_folder, file)
            with open(file_path, encoding="utf8") as fp:
                try:
                    self.products.append(json.load(fp))
                except Exception as e:
                    print(e)
                    print(f"Exception when loading {file} file.")

    def get_articles_from_ids(self, article_ids):
        articles = [p for p in self.products if p['id'] in article_ids]
        if len(articles) < len(article_ids):
            print("Not all articles found ind DB!")
        return articles


class ShoppingCartsDb:
    def __init__(self, data_folder="Migros_case", amount_to_load=5):
        self.data_folder = data_folder
        shopping_cart_folder = r"Shoppin_Cart"
        data_extract_folder = os.path.join(os.path.dirname(__file__), "..", "..")

        for path in os.walk(data_folder):
            create_path = os.path.join(data_extract_folder, path[0])
            if not os.path.exists(create_path):
                os.mkdir(create_path)
            for subfolder in path[1]:
                if not os.path.exists(os.path.join(create_path, subfolder)):
                    os.mkdir(os.path.join(create_path, subfolder))
            print(f"Checking files to extract:\n{path[2]}\n")
            for file in tqdm(path[2]):
                if file.split('.')[1] == '7z':
                    extract_path = os.path.join(create_path, file.split('.')[0])
                    if not os.path.exists(extract_path):
                        os.mkdir(extract_path)
                        Archive(os.path.join(path[0], file)).extractall(extract_path)
                else:
                    extract_path = os.path.join(create_path, file)
                    shutil.copyfile(os.path.join(path[0], file), extract_path)

        carts_files_folder = os.path.join(data_extract_folder, data_folder, shopping_cart_folder)
        print("Loading shopping carts\n")
        self.shopping_carts_df = None
        for file in tqdm(os.listdir(carts_files_folder)[:amount_to_load]):
            file_path = os.path.join(carts_files_folder, file, file + ".csv")
            try:
                if self.shopping_carts_df is None:
                    self.shopping_carts_df = pd.read_csv(file_path)
                else:
                    df = pd.read_csv(file_path)
                    self.shopping_carts_df = pd.concat([self.shopping_carts_df, df], axis=0)
            except Exception as e:
                print(e)
                print(f"Exception when loading {file} file.")
        self.shopping_carts_df.reset_index(inplace=True)

    def get_customer_purchases(self, customer_id: int):
        return json.loads(self.shopping_carts_df[self.shopping_carts_df["KundeID"] == customer_id].to_json(orient="records"))


class MigrosDb:
    def __init__(self, product_db=None, shopping_cart_db=None, load_all=False):
        if load_all:
            self.product_db = ProductsDb(amount_to_load=40000) if product_db is None else product_db
            self.shopping_cart_db = ShoppingCartsDb(amount_to_load=20) if shopping_cart_db is None else shopping_cart_db
        else:
            self.product_db = ProductsDb() if product_db is None else product_db
            self.shopping_cart_db = ShoppingCartsDb() if shopping_cart_db is None else shopping_cart_db

    def get_purchased_articles_of_customer(self, customer_id):
        purchases = self.shopping_cart_db.get_customer_purchases(customer_id)
        article_ids = [str(p["ArtikelID"]) for p in purchases]
        return self.product_db.get_articles_from_ids(article_ids)

    def get_categories_of_articles(self):
        pass

