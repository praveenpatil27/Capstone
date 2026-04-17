Certainly! Below is a complete Python file that includes a function `DB_Connection()` to establish a connection to a SQL Server database. Additionally, I've included a configuration file structure for different environments (Development, QA, and Production).

### Python File: `db_connection.py`

```python
import pyodbc
import json

def DB_Connection():
    # SQL Server connection details
    URL = "your_sql_server_url"  # Replace with your SQL Server URL
    UserName = "your_username"    # Replace with your username
    Password = "your_password"     # Replace with your password
    Database = "your_database"     # Replace with your database name

    # Create a connection string
    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={URL};DATABASE={Database};UID={UserName};PWD={Password}"

    # Establish the connection
    try:
        conn = pyodbc.connect(connection_string)
        print("Connection successful")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

if __name__ == "__main__":
    # Test the DB_Connection function
    connection = DB_Connection()
    if connection:
        connection.close()
```

### Configuration File: `config.json`

You can create a JSON configuration file named `config.json` to store the connection details for different environments. Here’s an example structure:

```json
{
    "Development": {
        "URL": "dev_sql_server_url",
        "UserName": "dev_username",
        "Password": "dev_password",
        "Database": "dev_database"
    },
    "QA": {
        "URL": "qa_sql_server_url",
        "UserName": "qa_username",
        "Password": "qa_password",
        "Database": "qa_database"
    },
    "Production": {
        "URL": "prod_sql_server_url",
        "UserName": "prod_username",
        "Password": "prod_password",
        "Database": "prod_database"
    }
}
```

### Usage

To use the configuration file in your `DB_Connection()` function, you can modify the function to read from the `config.json` file based on the environment you want to connect to. Here’s how you can do that:

```python
import pyodbc
import json

def DB_Connection(env='Development'):
    # Load configuration from JSON file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Get the connection details for the specified environment
    db_config = config.get(env)
    if not db_config:
        print(f"Environment '{env}' not found in configuration.")
        return None

    # SQL Server connection details
    URL = db_config["URL"]
    UserName = db_config["UserName"]
    Password = db_config["Password"]
    Database = db_config["Database"]

    # Create a connection string
    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={URL};DATABASE={Database};UID={UserName};PWD={Password}"

    # Establish the connection
    try:
        conn = pyodbc.connect(connection_string)
        print("Connection successful")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

if __name__ == "__main__":
    # Test the DB_Connection function for Development environment
    connection = DB_Connection('Development')
    if connection:
        connection.close()
```

### Notes
- Make sure to install the `pyodbc` library if you haven't already. You can do this using pip:
  ```bash
  pip install pyodbc
  ```
- Replace the placeholders in the `config.json` file with your actual SQL Server connection details.
- Ensure that the ODBC Driver for SQL Server is installed on your machine. The example uses "ODBC Driver 17 for SQL Server". Adjust the driver version as necessary.