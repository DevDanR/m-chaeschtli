from flask import Flask, request
from pyunpack import Archive
import os
from tqdm import tqdm
import shutil
import json

app = Flask(__name__)

data_folder = r"Migros_case"
products_folder = r"products"
shopping_cart_folder = r"Shoppin_Cart"
data_extract_folder = os.path.join("..", "..")

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
products = []
for file in tqdm(os.listdir(products_files_folder)[:1000]):
    file_path = os.path.join(products_files_folder, file)
    with open(file_path, encoding="utf8") as fp:
        try:
            products.append(json.load(fp))
        except Exception as e:
            print(e)
            print(f"Exception when loading {file} file.")


@app.get('/products')
def home_data():
    amount = int(request.args.get('amount'))
    return {"prodcuts_list": products[:amount]}


@app.get('/programming_languages')
def list_programming_languages():
    return {"programming_languages": "test"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
