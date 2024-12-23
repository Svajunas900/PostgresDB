import psycopg2
from dotenv import load_dotenv
import os 


load_dotenv()
PG_USERNAME = os.getenv('PG_USERNAME')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_DATABASE = os.getenv('PG_DATABASE')


class DbConnection:
    _instance = None

    def cursor(cls):
        cls._instance = cls._instance.cursor()
        return cls._instance
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance = psycopg2.connect(database=PG_DATABASE, user=PG_USERNAME, password=PG_PASSWORD, host="localhost", port=5432)
        return cls._instance


connection = DbConnection()
cursor = connection.cursor()


def insert_to_balance(id, user_id, active_balance, last_operation_id):
    cursor.execute(f"""
    INSERT INTO balance (id, user_id, active_balance, last_operation_id)
    VALUES ({id}, {user_id}, {active_balance}, {last_operation_id})
    """)
    connection.commit()


def insert_to_history(id, user_id, url, date, time_spend):
    cursor.execute(f"""
    INSERT INTO history (id, user_id, url, date, time_spend)
    VALUES ({id}, {user_id}, '{url}', '{date}', '{time_spend}')
    """)
    connection.commit()


def insert_to_transactions(id, user_id, transaction_type):
    cursor.execute(f"""
    INSERT INTO transactions (id, user_id, transaction_type)
    VALUES ({id}, {user_id}, '{transaction_type}')
    """)
    connection.commit()


def insert_to_type_transactions(id, t_type):
    cursor.execute(f"""
    INSERT INTO type_transactions (id, t_type)
    VALUES ({id}, '{t_type}')
    """)
    connection.commit()


def insert_to_users(id, name, email):
    cursor.execute(f"""
    INSERT INTO users (id, name, email)
    VALUES ({id}, '{name}', '{email}')
    """)
    connection.commit()


# insert_to_history(3, 2, 'asdasd', '2000-12-22', '2000-02-03')
# insert_to_type_transactions(3, 'ok12')
# insert_to_transactions(4, 1, "Hello")
insert_to_users(4, "Svajus", "Svajus@gma")