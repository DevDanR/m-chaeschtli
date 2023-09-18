# m-chaeschtli

## Setup the python backend
Anaconda is used as package manager and flask for the implementation of the REST API. The enviroment was created with:

```
conda create --name hackzurich23 python
conda activate hackzurich23
conda install pip tqdm
pip install flask pyunpack patool pandas flask-cors
```

Next the Flask framework needs to know the main file of the app. Run in your terminal:
```
export FLASK_APP=main.py  # Linux
set FLASK_APP=main.py  # Windows
```

To run the app unpack the data Migros_case.7z to the m-chaeschtli-backend folder. Then app can then be started by (make sure you have the correct enviroment active):
```
python main.py
```
Note the first time will take longer since the subfolders will be unzipped and the data will be loaded.

If you run into issues when using pycharm try to deactivate the flask integration (see [https://youtrack.jetbrains.com/issue/PY-55759/Flask-console-start-failed-No-module-named-wsgi](here))

## Setup the frontend
To start the app please be sure you already have installed node and npm.

```
cd .\m-chaeschtli-frontend\
npm install
ng serve
```
Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.
