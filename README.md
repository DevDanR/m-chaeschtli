# m-chaeschtli

## Setup the python backend
Anaconda is used as package manager and flask for the implementation of the REST API. The enviroment was created with:

```
conda create --name hackzurich23 python
conda install pip tqdm
pip install flask pyunpack patool pandas flask-cors
```

To run the backend first run:
```
export FLASK_APP=main.py  # Linux
set FLASK_APP=main.py  # Windows
```
If you run into issues try to deactivate the flask integration (see [https://youtrack.jetbrains.com/issue/PY-55759/Flask-console-start-failed-No-module-named-wsgi](here))

## Setup the frontend
To start the app please be sure you already have installed node and npm.

```
cd .\m-chaeschtli-frontend\
npm install
ng serve
```
Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.
