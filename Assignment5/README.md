### Installing necessary packages:  
* `pip install fastapi`
* `pip install "uvicorn[standard]"`  
* `pip install sqlalchemy`  
* `pip install pymysql`
* `pip install pytest`
* `pip install pytest-mock`
* `pip install httpx`
* `pip install cryptography`
### Run the server:
`uvicorn api.main:app --reload`
### Test API by built-in docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## * config.py file excluded as it contains root password
```python
config.py
class Conf:
    host = "localhost"
    database = "sandwich_maker_api"
    port = 3306
    user = "root"
    password = "** Insert root password here **"