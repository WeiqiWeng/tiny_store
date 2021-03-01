# Tiny Store: A Hands-on Flask App

## 1. Local Development Environment
### 1.1 MySQL
This project leverages MySQL as database. Before the server and running environment is set up, we want to first make sure MySQL is working locally. 
#### 1.1.1 Windows
For Chinese reader, you can find plenty of resources talking about how to set up MySQL as local database service. Thanks to Winton's awesome work, here is an [example](https://www.cnblogs.com/winton-nfs/p/11524007.html). 

### 1.2 Python 3.7
Here we use Python 3.7 virtual environment to activate local server. Make sure you have Python 3.7 installed and path to Python binary file added into your environment variable. Assuming the Python packages involved in the virtual environment will be installed in folder `venv` under local directory, run the following commands sequentially, first create `venv` with 
```
virtualenv -p python3.7 venv
```
. Then activate virtual environment with
```
source ./venv/bin/activate
```
. Within virtual environment, packages are installed through
```
pip install -r requirements.txt
```
.

## 2. Local Server
This part walks through how to set up local server and interact with the app. Make sure local MySQL service is activated. Within virtual environment, run
```python
python run_server.py
```
to initiate local server. Then you can interact with the app in browser at http://127.0.0.1:5000/. 

