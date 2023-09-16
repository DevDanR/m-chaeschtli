# m-chaeschtli

## Setup the python backend
Anaconda is used as package manager and flask for the implementation of the REST API. The enviroment was created with:

```
conda create --name hackzurich23 python
conda install pip
pip install flask
pip install pyunpack
pip install patool
conda install tqdm
pip install pandas
```

To run the backend first run:
```
export FLASK_APP=main.py  # Linux
set FLASK_APP=main.py  # Windows
```
If you run into issues try to deactivate the flask integration (see [https://youtrack.jetbrains.com/issue/PY-55759/Flask-console-start-failed-No-module-named-wsgi](here))
