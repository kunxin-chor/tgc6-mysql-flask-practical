# Setting up Python to interface with MySQL

1. Install the following dependencies

```
pip3 install pymysql
pip3 install python-dotenv
```

2. Create an .env file in the same folder as your `app.py`

3. Enter the following:

```
DB_USER=gitpod
DB_PASSWORD=
```

4. Add a `.gitignore` file and set it to ignore `.env`

5. Import in `dotenv` 

```
from dotenv import load_dotenv
load_env()
```

This will allows us to access the `DB_USER` and `DB_PASSWORD` environment variables set in step 3 above.

6. Add in the following function that allows us to connect to the database

```
def get_connection(db_name):
    conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', db_name)
```

