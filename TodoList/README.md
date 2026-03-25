# TodoList Assignment

## Setup
1. Create virtual environment
   - python -m venv .venv
2. Activate it 
   - .venv\Scripts\activate
3. Install dependencies
   - pip install -r requirements.txt
4. Run server 
   - uvicorn main:app --reload

## * config.py file excluded as it contains root password
```python
config.py
class Conf:
    host = "localhost"
    database = "TodoDB"
    port = 3306
    user = "root"
    password = "** Insert root password here **"